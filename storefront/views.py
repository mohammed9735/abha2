from django.shortcuts import render

def home(request):
    """
    الصفحة الرئيسية للمتجر الإلكتروني
    """
    return render(request, "home.html")
