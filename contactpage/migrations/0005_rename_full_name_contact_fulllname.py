# Generated by Django 5.0 on 2023-12-23 18:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contactpage', '0004_rename_fullname_contact_full_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='full_name',
            new_name='fulllname',
        ),
    ]
