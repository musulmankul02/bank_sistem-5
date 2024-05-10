from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    phone = models.CharField(
        max_length=255, verbose_name= "Номер телефона"
    )
    age = models.CharField(
        max_length=3,
        verbose_name="Возраст"
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )    
    password_confirm = models.CharField(
        max_length=255,
        verbose_name="Подтвердите пароль"
    )
    balance = models.PositiveIntegerField(
        default = 0,
        verbose_name='Баланс'
    )
    wallet_address = models.CharField(
        max_length=12,
        verbose_name="ID кошелка",
        unique=True,
        blank=True,
    )
    
    def __str__(self):
        return f"""{self.wallet_address}            Имя пользователя: {self.username}"""
    
    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"