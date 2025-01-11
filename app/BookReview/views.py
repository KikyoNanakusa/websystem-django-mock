from django.shortcuts import render
from .models import Product


def index(request):
    # データベースから全てのProductデータを取得
    products = Product.objects.all()
    return render(request, 'index.html', {'books': products})
