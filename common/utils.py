from django.conf import settings
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.utils import timezone
from supabase import Client, create_client


def get_supabase_client():
    supabase: Client = create_client(
        settings.SUPABASE_URL, settings.SUPABASE_SERVICE_ROLE_KEY
    )
    return supabase


def upload_to_supabase_bucket(image_file):
    supabase = get_supabase_client()

    file_name = f"media/-{timezone.now()}-{image_file.name}"
    file_content = image_file.read()

    _ = supabase.storage.from_(settings.SUPABASE_BUCKET).upload(file_name, file_content)

    return supabase.storage.from_(settings.SUPABASE_BUCKET).get_public_url(file_name)


def send_profile_update_reminders():
    users_to_notify = User.objects.filter(first_name="", last_name="")

    for user in users_to_notify:
        subject = "Wera | Reminder to Update Your Profile"
        message = f"""Dear {user.username},
        \n\nIt looks like you haven't updated your first name or last name in your profile.
        Please take a moment to update your profile information.
        \n\nBest regards,
        \n Edwin from Wera
        """

        send_mail(
            subject,
            message,
            settings.DEFAULT_FROM_EMAIL,
            [user.email],
            fail_silently=False,  # Set to True to avoid exceptions in case of failure
        )

    print(f"Reminder emails sent to {users_to_notify.count()} users.")


def send_check_back_reminder():
    users = User.objects.all()

    for user in users:
        if user.email:
            subject = "We Miss You! Come Back and Check Out What's New"
            message = f"""
            Dear {user.username},\n\n
            We noticed you haven't <a href='https://wera.co.ke'>www.wera.co.ke</a> in a while.
            We’ve added some exciting new features and updates. Come back and check them out!\n\n
            We look forward to seeing you again!
            \n\nBest regards,
            \n Edwin from Wera
            """

            try:
                send_mail(
                    subject,
                    message,
                    settings.DEFAULT_FROM_EMAIL,
                    [user.email],
                    fail_silently=False,  # Will raise exceptions if email sending fails
                )
                print(f"Reminder email sent to {user.username} ({user.email})")
            except Exception as e:
                print(
                    f"Failed to send email to {user.username} ({user.email}): {str(e)}"
                )

    print(f"Reminder emails sent to {users.count()} users.")
