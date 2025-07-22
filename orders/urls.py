from django.urls import path
from django.http import HttpResponse

def orders_home(request):
    return HttpResponse("مرحبًا بك في قسم الطلبات")

urlpatterns = [
    path('', orders_home, name='orders_home'),
]
