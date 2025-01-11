from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=100)  # 商品名
    description = models.TextField()         # 商品説明
    price = models.DecimalField(max_digits=10, decimal_places=2)  # 商品価格
    isbn = models.CharField(max_length=13, blank=True, null=True)  # ISBN番号
    created_at = models.DateTimeField(auto_now_add=True)  # 作成日時
    updated_at = models.DateTimeField(auto_now=True)      # 更新日時

    def __str__(self):
        return self.name
