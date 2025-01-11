from django.shortcuts import render, get_object_or_404
from .models import Product


def index(request):
    # データベースから全てのProductデータを取得
    products = Product.objects.all()
    return render(request, 'index.html', {'books': products})


def product_detail(request, product_id):
    # 特定の商品の詳細情報を取得
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'product_detail.html', {'product': product})