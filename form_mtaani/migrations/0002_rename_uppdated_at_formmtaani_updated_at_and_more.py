# Generated by Django 5.1.4 on 2024-12-29 13:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('form_mtaani', '0001_initial'),
        ('wera', '0002_location_alter_wera_location'),
    ]

    operations = [
        migrations.RenameField(
            model_name='formmtaani',
            old_name='uppdated_at',
            new_name='updated_at',
        ),
        migrations.RemoveField(
            model_name='formmtaani',
            name='Wera_type',
        ),
        migrations.AlterField(
            model_name='formmtaani',
            name='location',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='wera.location'),
        ),
    ]