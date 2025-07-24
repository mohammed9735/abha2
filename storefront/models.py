from django.db import models
from django.conf import settings
from products.models import Product

class Cart(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="cart", verbose_name="المستخدم")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="تاريخ الإنشاء")

    def __str__(self):
        return f"سلة {self.user.username}"


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name="items")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="المنتج")
    quantity = models.PositiveIntegerField(default=1, verbose_name="الكمية")

    def __str__(self):
        return f"{self.quantity} × {self.product.name}"

    def get_total_price(self):
        return self.quantity * self.product.price
