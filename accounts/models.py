from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class CustomUser(AbstractUser):
    phone = models.CharField(max_length=15, unique=True, verbose_name="رقم الجوال")
    email = models.EmailField(unique=True, verbose_name="البريد الإلكتروني")
    username = models.CharField(max_length=150, unique=True, verbose_name="اسم المستخدم")

    # ✅ إصلاح التعارض بإضافة related_name مخصص
    groups = models.ManyToManyField(
        Group,
        related_name="customuser_groups",
        blank=True,
        help_text="The groups this user belongs to.",
        verbose_name="المجموعات"
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name="customuser_permissions",
        blank=True,
        help_text="Specific permissions for this user.",
        verbose_name="صلاحيات المستخدم"
    )

    def __str__(self):
        return self.username
