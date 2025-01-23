from django.core.management.base import BaseCommand
from BookReview.models import User, Category, Product, ProductCategory, Review
import random
from faker import Faker

class Command(BaseCommand):
    help = 'モックデータを挿入する'

    def handle(self, *args, **kwargs):
        # Fakerのインスタンスを生成
        fake = Faker()

        # カテゴリを作成
        categories = ["本", "ゲーム", "DVD"]
        category_objects = []
        for category_name in categories:
            category = Category.objects.create(name=category_name)
            category_objects.append(category)
        self.stdout.write(self.style.SUCCESS('カテゴリを作成しました。'))

        # ユーザーを作成
        users = []
        for _ in range(5):  # ユーザー5人作成
            user = User.objects.create(
                name=fake.name(),
                email=fake.email(),
                password=fake.password(),
            )
            users.append(user)
        self.stdout.write(self.style.SUCCESS('ユーザーを作成しました。'))

        # 商品を作成
        products = []
        for _ in range(10):  # 商品10個作成
            product = Product.objects.create(
                name=fake.word(),
                description=fake.text(),
                isbn=fake.isbn13()[:13],
                price=round(random.uniform(100, 1000), 2),
            )
            products.append(product)
        self.stdout.write(self.style.SUCCESS('商品を作成しました。'))

        # 商品とカテゴリの関連付け
        for product in products:
            for category in random.sample(category_objects, random.randint(1, len(category_objects))):
                ProductCategory.objects.create(product=product, category=category)
        self.stdout.write(self.style.SUCCESS('商品とカテゴリを関連付けました。'))

        # レビューを作成
        for user in users:
            for product in random.sample(products, random.randint(1, 3)):
                Review.objects.create(
                    user=user,
                    product=product,
                    title=fake.sentence(),
                    content=fake.text(),
                    evaluation_point=random.randint(1, 5),
                )
        self.stdout.write(self.style.SUCCESS('レビューを作成しました。'))

        self.stdout.write(self.style.SUCCESS('モックデータの挿入が完了しました！'))
