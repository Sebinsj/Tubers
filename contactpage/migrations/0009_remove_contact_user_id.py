# Generated by Django 5.0 on 2024-01-07 18:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contactpage', '0008_rename_full_name_contact_fullname'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='user_id',
        ),
    ]