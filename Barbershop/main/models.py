from datetime import date

from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

User = get_user_model()


class Customers(models.Model):
    """Заказчики"""
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=25)
    surname = models.CharField(max_length=25)
    info = models.TextField(default="Informations")

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


class Roles(models.Model):
    """Роли"""
    ROLE_NAMES = (
        ('Barber', 'Barber'),
        ('Admin', 'Admin')
    )

    role = models.CharField(max_length=15, choices=ROLE_NAMES)
    name = models.CharField(max_length=15, null=True)
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Роль'
        verbose_name_plural = 'Роли'


class Days(models.Model):
    """Дни записи"""
    day = models.DateField(default=date.today)
    role_id = models.ForeignKey(Roles, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'День записи'
        verbose_name_plural = 'Дни записи'


class Times(models.Model):
    """Время записи"""
    time_start = models.TimeField()
    time_end = models.TimeField()
    day_id = models.ForeignKey(Days, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Время записи'
        verbose_name_plural = 'Время записей'


class Order(models.Model):
    """Заказ"""
    TIME = (
        ('Morning', 'Morning'),
        ('Lunch Time', 'Lunch Time'),
        ('Evening', 'Evening'),
        ('Night', 'Night'),
    )
    HAIRCUTS = (
        ('Haircut and Shaving 10$', 'Haircut and Shaving 10$'),
        ('Haircut and Trimming 8$', 'Haircut and Trimming 8$'),
        ('Haircut 7$', 'Haircut 7$'),
    )
    BARBERS = (
        ('Antey', 'Antey'),
        ('Ruslan', 'Ruslan'),
        ('Alex', 'Alex'),
        ('Anatoliy', 'Anatoliy'),
    )
    barber = models.CharField(max_length=20, choices=BARBERS)
    day = models.DateField()
    time = models.CharField(max_length=50, choices=TIME)
    haircut_name = models.CharField(max_length=50, choices=HAIRCUTS)
    customer = models.ForeignKey(Customers, null=True, on_delete=models.SET_NULL)
    role = models.ForeignKey(Roles, null=True, on_delete=models.SET_NULL)

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'


