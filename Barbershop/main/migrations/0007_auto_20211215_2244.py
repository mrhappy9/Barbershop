# Generated by Django 3.2.9 on 2021-12-15 19:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20211215_2233'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='roles_id',
        ),
        migrations.RemoveField(
            model_name='order',
            name='user_id',
        ),
    ]