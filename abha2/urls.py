from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

    # روابط التطبيقات
    path('products/', include('products.urls')),     # تطبيق المنتجات
    path('orders/', include('orders.urls')),         # تطبيق الطلبات
    path('', include('storefront.urls')),            # الصفحة الرئيسية
    path('accounts/', include('accounts.urls')),     # ✅ تسجيل المستخدمين
]

# تفعيل عرض ملفات الوسائط أثناء التطوير
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
