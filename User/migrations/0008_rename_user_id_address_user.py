# Generated by Django 4.2.5 on 2023-09-19 07:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0007_rename_useraddress_address'),
    ]

    operations = [
        migrations.RenameField(
            model_name='address',
            old_name='user_id',
            new_name='user',
        ),
    ]
