# Generated by Django 5.0.2 on 2024-03-01 10:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('workmeuve', '0002_user_created_date_user_email_user_last_login_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='last_login',
        ),
    ]
