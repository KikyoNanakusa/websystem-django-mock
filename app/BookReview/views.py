from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Review, User   # Reviewモデルをインポート
from .forms import ReviewForm  # フォームをインポート


def index(request):
    # データベースから全てのProductデータを取得
    products = Product.objects.all()
    return render(request, 'index.html', {'books': products})

def product_detail(request, product_id):
    # 特定の商品の詳細情報を取得
    product = get_object_or_404(Product, id=product_id)
    # 対象商品のレビューを取得
    reviews = Review.objects.filter(product=product)

    # モックユーザー（仮のユーザー）を取得
    mock_user, created = User.objects.get_or_create(
        name="MockUser",
        email="mockuser@example.com",
        defaults={"password": "mockpassword"}
    )

    # フォームの処理
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            # 同じユーザーが同じ商品にレビューを投稿しているか確認
            existing_review = Review.objects.filter(user=mock_user, product=product).first()
            if existing_review:
                # すでにレビューが存在する場合のエラーメッセージ
                return render(request, 'product_detail.html', {
                    'product': product,
                    'reviews': reviews,
                    'form': form,
                    'error': "この商品には既にレビューを投稿しています。",
                })

            # 新しいレビューを保存
            review = form.save(commit=False)
            review.product = product
            review.user = mock_user
            review.save()
            return redirect('product_detail', product_id=product_id)
    else:
        form = ReviewForm()

    return render(request, 'product_detail.html', {
        'product': product,
        'reviews': reviews,
        'form': form,
    })