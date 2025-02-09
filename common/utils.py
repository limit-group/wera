from django.conf import settings
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.utils import timezone
from supabase import Client, create_client

from contact.models import Profile


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
        p = Profile.objects.filter(user=user).first()
        if p:
            update_profile_url = f"https://www.wera.co.ke/contacts/{p.id}"
        subject = f"Let’s Complete Your Profile."
        message = f"""
<!DOCTYPE html>
<html>
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Complete Your Profile</title>
</head>
<body style="margin: 0; padding: 0; font-family: Arial, sans-serif; background-color: #f4f4f4;">
    <table role="presentation" width="100%" cellspacing="0" cellpadding="0" border="0">
        <tr>
            <td align="center" style="padding: 20px 0;">
                <table role="presentation" width="600px" cellspacing="0" cellpadding="0" border="0" style="background-color: #ffffff; border-radius: 8px; padding: 20px; box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);">
                    <tr>
                        <td align="center" style="padding: 20px 0;">
                            <h2 style="color: #333;">Complete Your Profile, {user.first_name}! 🎉</h2>
                            <p style="color: #555; font-size: 16px; line-height: 1.5;">
                                We noticed your profile is almost complete! Just one small thing—your first and last name are missing.
                            </p>
                            <p style="color: #555; font-size: 16px; line-height: 1.5;">
                                Adding your name helps personalize your experience on <strong>Wera</strong>. Plus, it makes interactions smoother for everyone.
                            </p>
                            <a href="{update_profile_url}" style="display: inline-block; padding: 12px 20px; background-color: #007BFF; color: #ffffff; text-decoration: none; font-size: 16px; border-radius: 5px; margin-top: 10px;">
                                Update My Profile
                            </a>
                        </td>
                    </tr>
                    <tr>
                        <td align="center" style="padding: 20px; font-size: 14px; color: #777;">
                            If you need any help, feel free to reply—we’ve got you covered!
                            <br><br>Best Regards,
                            <br><strong>Edwin from wera.co.ke</strong>
                        </td>
                    </tr>
                </table>
                <p style="font-size: 12px; color: #aaa; margin-top: 20px;">
                    You are receiving this email because you have an account on Wera. If you didn’t request this, you can safely ignore it.
                </p>
            </td>
        </tr>
    </table>
</body>
</html>
        """

        send_mail(
            subject=subject,
            message="",
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[user.email],
            html_message=message,
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
