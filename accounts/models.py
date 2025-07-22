from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    phone = models.CharField(max_length=15, unique=True, verbose_name="رقم الجوال")
    email = models.EmailField(unique=True, verbose_name="البريد الإلكتروني")
    username = models.CharField(max_length=150, unique=True, verbose_name="اسم المستخدم")

    def __str__(self):
        return self.username
