# Generated by Django 4.1.5 on 2023-01-17 21:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_rename_password1_users_password_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Users',
        ),
    ]