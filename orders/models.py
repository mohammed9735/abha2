from django.db import models
from django.conf import settings  # ✅ استبدلنا استيراد User
from products.models import Product

class Order(models.Model):
    STATUS_CHOICES = (
        ('pending', 'قيد المعالجة'),
        ('completed', 'مكتمل'),
        ('canceled', 'ملغي'),
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,   # ✅ تعديل العلاقة مع المستخدم
        on_delete=models.CASCADE,
        related_name="orders",
        verbose_name="المستخدم"
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="تاريخ الإنشاء")
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending', verbose_name="حالة الطلب")

    def __str__(self):
        return f"طلب رقم {self.id} للمستخدم {self.user.username}"

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="items")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="المنتج")
    quantity = models.PositiveIntegerField(default=1, verbose_name="الكمية")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="سعر الوحدة وقت الشراء")

    def __str__(self):
        return f"{self.quantity} × {self.product.name}"
