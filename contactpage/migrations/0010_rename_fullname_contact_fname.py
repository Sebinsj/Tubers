# Generated by Django 5.0 on 2024-01-07 18:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contactpage', '0009_remove_contact_user_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='fullname',
            new_name='fname',
        ),
    ]