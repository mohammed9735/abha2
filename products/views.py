from django.shortcuts import render
from .models import Product

def product_list(request):
    """
    عرض قائمة المنتجات باستخدام القالب الموجود products.html
    """
    products = Product.objects.all()
    return render(request, "products/products.html", {"products": products})
