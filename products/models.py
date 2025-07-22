from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name="اسم التصنيف")
    description = models.TextField(blank=True, null=True, verbose_name="وصف التصنيف")

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=200, verbose_name="اسم المنتج")
    description = models.TextField(blank=True, null=True, verbose_name="وصف المنتج")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="السعر")
    stock = models.PositiveIntegerField(default=0, verbose_name="المخزون")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="products", verbose_name="التصنيف")

    def __str__(self):
        return self.name

class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="images")
    image = models.ImageField(upload_to='products/', verbose_name="صورة المنتج")

    def __str__(self):
        return f"صورة لـ {self.product.name}"

# انتهى وصف models.py لتطبيق المنتجات (Products App)
