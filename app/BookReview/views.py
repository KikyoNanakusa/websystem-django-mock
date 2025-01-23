from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.hashers import check_password, make_password
from .models import Product, Review, User, Category, ProductCategory  # モデルのインポート
from .forms import ReviewForm, LoginForm, SignupForm  # フォームのインポート


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
    """商品詳細ページ - レビュー投稿機能"""
    product = get_object_or_404(Product, id=product_id)
    reviews = product.reviews.all()  # 商品に関連するレビューを取得
    form = None  # レビュー投稿用フォーム（例: レビュー用フォームを追加する場合）

    # ログインしていない場合
    logged_in_user = None
    if 'user_id' in request.session:
        # ログイン中のユーザーを取得
        logged_in_user = User.objects.get(id=request.session['user_id'])

    if not logged_in_user:
        # ログインしていない場合、nextパラメータをURLに追加してログインページにリダイレクト
        return redirect(f"{reverse('login')}?next={request.path}")

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
        'logged_in_user': request.user if request.user.is_authenticated else None,  # ログイン中のユーザー情報を渡す
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
                    request.session['user_id'] = str(user.id)  # UUIDを文字列に変換して保存
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
    return redirect('index')  # 'login' から 'index' に変更


def signup_view(request):
    """ユーザー登録ページ"""
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            # 新しいユーザーを作成
            user = form.save(commit=False)
            user.password = make_password(form.cleaned_data['password'])  # パスワードをハッシュ化
            user.save()
            messages.success(request, "アカウントが作成されました。ログインしてください。")
            return redirect('login')  # ログインページにリダイレクト
        else:
            messages.error(request, "入力内容に誤りがあります。")
    else:
        form = SignupForm()

    return render(request, 'signup.html', {'form': form})


def about(request):
    return render(request, 'about.html')


def contact(request):
    if request.method == 'POST':
        # フォームのデータ処理（例：送信内容をメールで送信するなど）
        # 必要に応じて処理を追加してください
        pass

    return render(request, 'contact.html')
