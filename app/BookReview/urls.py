"""
URL configuration for BookReview project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from BookReview import views  # views モジュールをインポート
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),  # トップページ
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('product/<uuid:product_id>/', views.product_detail, name='product_detail'),  # 商品詳細ページ
    path('product/<uuid:product_id>/review/', views.post_review, name='post_review'),  # レビュー投稿処理用エンドポイント
    path('login/', views.login_view, name='login'),  # ログインページ
    path('logout/', views.logout_view, name='logout'),  # ログアウトページ
    path('signup/', views.signup_view, name='signup'),  # ユーザー登録ページ
    path('category/<uuid:category_id>/', views.category_products, name='category_products')  # カテゴリ別商品ページ
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
