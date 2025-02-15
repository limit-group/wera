# Generated by Django 5.1.5 on 2025-02-09 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("wera", "0008_wera_slug"),
    ]

    operations = [
        migrations.AddField(
            model_name="category",
            name="active",
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name="contact",
            name="active",
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name="location",
            name="active",
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name="newsletter",
            name="active",
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name="wera",
            name="active",
            field=models.BooleanField(default=True),
        ),
    ]
