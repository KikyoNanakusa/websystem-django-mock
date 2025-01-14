from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.hashers import check_password, make_password
from .models import Product, Review, User  # モデルのインポート
from .forms import ReviewForm, LoginForm  # フォームのインポート


def index(request):
    """トップページ - 商品一覧を表示"""
    products = Product.objects.all()
    return render(request, 'index.html', {'books': products})


def product_detail(request, product_id):
    """商品詳細ページ - レビュー投稿機能"""
    # ユーザーがログインしているか確認
    if 'user_id' not in request.session:
        return redirect('login')  # ログインページへリダイレクト

    product = get_object_or_404(Product, id=product_id)
    reviews = Review.objects.filter(product=product)

    # ログイン中のユーザーを取得
    logged_in_user = User.objects.get(id=request.session['user_id'])

    if request.method == 'POST':
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
    })


def login_view(request):
    """ログインページ"""
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
                    return redirect('index')
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
