# Generated by Django 3.2.9 on 2021-12-07 23:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20211208_0222'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='username',
            field=models.CharField(default='user', max_length=50, unique=True),
        ),
    ]