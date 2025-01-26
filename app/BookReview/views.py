from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.hashers import check_password, make_password
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .models import Product, Review, User, Category, ProductCategory
from .forms import ReviewForm, LoginForm, SignupForm
from django.contrib.auth import login, authenticate


def index(request):
    """トップページ - 商品カテゴリ一覧を表示"""
    categories = Category.objects.all()  # カテゴリをデータベースから取得するコード
    return render(request, 'index.html', {'categories': categories})


def category_products(request, category_id):
    """カテゴリ内の商品一覧ページ"""
    category = get_object_or_404(Category, id=category_id)
    product_categories = ProductCategory.objects.filter(category=category).select_related('product')
    products = [pc.product for pc in product_categories]

    return render(request, 'category_products.html', {
        'category_key': category.name,
        'products': products,
    })


def product_detail(request, product_id):
    """商品詳細ページ"""
    product = get_object_or_404(Product, id=product_id)
    reviews = product.reviews.all()  # 商品に関連するレビューを取得
    form = ReviewForm() if request.user.is_authenticated else None

    return render(request, 'product_detail.html', {
        'product': product,
        'reviews': reviews,
        'form': form,
    })


@login_required(login_url='login')
def post_review(request, product_id):
    """レビュー投稿処理（ログイン必須）"""
    product = get_object_or_404(Product, id=product_id)

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            # 同じユーザーが同じ商品にレビューを投稿しているか確認
            existing_review = Review.objects.filter(user=request.user, product=product).first()
            if existing_review:
                messages.error(request, "この商品には既にレビューを投稿しています。")
                return redirect('product_detail', product_id=product_id)

            # 新しいレビューを保存
            review = form.save(commit=False)
            review.product = product
            review.user = request.user
            review.save()
            messages.success(request, "レビューが投稿されました！")
            return redirect('product_detail', product_id=product_id)

    return redirect('product_detail', product_id=product_id)


def login_view(request):
    """ログインページ"""
    next_url = request.GET.get('next', 'index')

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            # ユーザー認証
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)  # Djangoのlogin関数でログイン処理
                messages.success(request, "ログインに成功しました！")
                return redirect(next_url)
            else:
                messages.error(request, "メールアドレスまたはパスワードが間違っています。")
    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form})


def logout_view(request):
    """ログアウト処理"""
    # セッションからユーザー情報を削除
    request.session.flush()
    messages.success(request, "ログアウトしました。")
    return redirect('index')


def signup_view(request):
    """ユーザー登録ページ"""
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            # 新しいユーザーを作成
            user = form.save(commit=False)
            user.password = make_password(form.cleaned_data['password'])  #パスワードをハッシュ化
            user.save()
            messages.success(request, "アカウントが作成されました。ログインしてください。")
            return redirect('login')  # ログインページにリダイレクト
        else:
            messages.error(request, "入力内容に誤りがあります。")
    else:
        form = SignupForm()

    return render(request, 'signup.html', {'form': form})


def about(request):
    """Aboutページ"""
    return render(request, 'about.html')


def contact(request):
    """お問い合わせページ"""
    if request.method == 'POST':
        # フォームのデータ処理（例：送信内容をメールで送信するなど）
        pass

    return render(request, 'contact.html')
