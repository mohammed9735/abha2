from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),             # لوحة التحكم
    path('products/', include('products.urls')), # المنتجات
    path('orders/', include('orders.urls')),     # الطلبات
    path('', include('storefront.urls')),        # الصفحة الرئيسية (واجهة المتجر)
    path('accounts/', include('accounts.urls'))  # تسجيل الدخول والتسجيل
]

# تفعيل عرض ملفات الوسائط أثناء التطوير
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
