from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.hashers import check_password, make_password
from .models import Product, Review, User  # モデルのインポート
from .forms import ReviewForm, LoginForm  # フォームのインポート
from django.urls import reverse


def index(request):
    """トップページ - 商品カテゴリ一覧を表示"""
    categories = [
        {'key': 'book', 'name': '本'},
        {'key': 'game', 'name': 'ゲーム'},
        {'key': 'dvd', 'name': 'DVD'},
    ]
    return render(request, 'index.html', {'categories': categories})


def category_products(request, category_key):
    """カテゴリごとの商品一覧を表示"""
    # カテゴリに基づいた商品を取得
    products = Product.objects.filter(category=category_key)
    return render(request, 'category_products.html', {'products': products, 'category_key': category_key})


def product_detail(request, product_id):
    """商品詳細ページ - レビュー投稿機能"""
    product = get_object_or_404(Product, id=product_id)
    reviews = Review.objects.filter(product=product)

    # ログインしていない場合でも商品詳細ページにはアクセスできる
    logged_in_user = None
    if 'user_id' in request.session:
        # ログイン中のユーザーを取得
        logged_in_user = User.objects.get(id=request.session['user_id'])

    if request.method == 'POST' and logged_in_user:
        form = ReviewForm(request.POST)
        if form.is_valid():
            # 同じユーザーが同じ商品にレビューを投稿しているか確認
            existing_review = Review.objects.filter(user=logged_in_user, product=product).first()
            if existing_review:
                # すでにレビューが存在する場合
                return render(request, 'product_detail.html', {
                    'product': product,
                    'reviews': reviews,
                    'form': form,
                    'error': "この商品には既にレビューを投稿しています。",
                })

            # 新しいレビューを保存
            review = form.save(commit=False)
            review.product = product
            review.user = logged_in_user
            review.save()
            messages.success(request, "レビューが投稿されました！")
            return redirect('product_detail', product_id=product_id)
    else:
        form = ReviewForm()

    return render(request, 'product_detail.html', {
        'product': product,
        'reviews': reviews,
        'form': form,
        'logged_in_user': logged_in_user,  # ログイン中のユーザー情報を渡す
    })


def login_view(request):
    """ログインページ"""
    # nextパラメータを取得、デフォルトは'index'（トップページ）
    next_url = request.GET.get('next', 'index')

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            # ユーザー認証
            try:
                user = User.objects.get(email=email)
                if check_password(password, user.password):
                    # セッションにユーザー情報を保存
                    request.session['user_id'] = user.id
                    request.session['user_name'] = user.name
                    messages.success(request, "ログインに成功しました！")
                    return redirect(next_url)  # ログイン後にnext_urlにリダイレクト
                else:
                    messages.error(request, "パスワードが間違っています。")
            except User.DoesNotExist:
                messages.error(request, "該当するメールアドレスが見つかりません。")
    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form})


def logout_view(request):
    """ログアウト処理"""
    request.session.flush()  # セッションをクリア
    messages.success(request, "ログアウトしました。")
    return redirect('login')
