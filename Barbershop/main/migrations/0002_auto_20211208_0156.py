# Generated by Django 3.2.9 on 2021-12-07 22:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='days',
            options={'verbose_name': 'День записи', 'verbose_name_plural': 'Дни записи'},
        ),
        migrations.AlterModelOptions(
            name='order',
            options={'verbose_name': 'Заказ', 'verbose_name_plural': 'Заказы'},
        ),
        migrations.AlterModelOptions(
            name='roles',
            options={'verbose_name': 'Роль', 'verbose_name_plural': 'Роли'},
        ),
        migrations.AlterModelOptions(
            name='times',
            options={'verbose_name': 'Время записи', 'verbose_name_plural': 'Время записей'},
        ),
        migrations.AlterModelOptions(
            name='users',
            options={'verbose_name': 'Пользователь', 'verbose_name_plural': 'Пользователи'},
        ),
        migrations.AddField(
            model_name='order',
            name='haircut_name',
            field=models.CharField(default='Мужская стрижка', max_length=50),
        ),
    ]
