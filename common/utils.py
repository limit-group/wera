from supabase import Client, create_client
from django.conf import settings
from django.utils import timezone


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
