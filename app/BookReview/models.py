from django.db import models


class User(models.Model):
    """ユーザーを表すモデル"""
    name = models.CharField(max_length=100)  # ユーザー名
    email = models.EmailField(unique=True)  # ユニークなメールアドレス
    password = models.CharField(max_length=128)  # ハッシュ化されたパスワード
    created_at = models.DateTimeField(auto_now_add=True)  # 作成日時
    updated_at = models.DateTimeField(auto_now=True)  # 更新日時

    def __str__(self):
        return self.name


class Product(models.Model):
    """商品を表すモデル"""
    name = models.CharField(max_length=100)  # 商品名
    description = models.TextField()  # 商品説明
    isbn = models.CharField(max_length=13, blank=True, null=True)  # ISBN番号
    price = models.DecimalField(max_digits=10, decimal_places=2)  # 商品価格
    created_at = models.DateTimeField(auto_now_add=True)  # 作成日時
    updated_at = models.DateTimeField(auto_now=True)  # 更新日時

    def __str__(self):
        return self.name


class Review(models.Model):
    """レビューを表すモデル"""
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="reviews")  # ユーザーとの外部キー
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="reviews")  # 商品との外部キー
    title = models.CharField(max_length=100)  # レビューのタイトル
    content = models.TextField()  # レビュー内容
    evaluation_point = models.PositiveIntegerField()  # 評価ポイント（例: 1~5）
    created_at = models.DateTimeField(auto_now_add=True)  # 作成日時
    updated_at = models.DateTimeField(auto_now=True)  # 更新日時

    def __str__(self):
        return f"{self.title} - {self.user.name}"

    class Meta:
        """カスタム設定"""
        unique_together = ('user', 'product')  # ユーザーと商品の組み合わせで重複を禁止
        ordering = ['-created_at']  # 作成日時の降順でソート