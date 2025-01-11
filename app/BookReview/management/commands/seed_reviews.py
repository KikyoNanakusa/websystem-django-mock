from django.core.management.base import BaseCommand
from BookReview.models import User, Product, Review


class Command(BaseCommand):
    help = 'Add initial review data'

    def handle(self, *args, **kwargs):
        # ユーザーと商品が存在する前提でレビューを作成しました。
        user1 = User.objects.filter(email="john@example.com").first()
        user2 = User.objects.filter(email="jane@example.com").first()
        product1 = Product.objects.filter(name="The Great Gatsby").first()
        product2 = Product.objects.filter(name="To Kill a Mockingbird").first()

        if not (user1 and user2 and product1 and product2):
            self.stdout.write(self.style.ERROR('Required users or products are missing. Run seed_users and seed_products first.'))
            return

        reviews = [
            {
                "user": user1,
                "product": product1,
                "title": "最高の本でした！",
                "content": "心に響くストーリーで、とても満足しました。",
                "evaluation_point": 5,
            },
            {
                "user": user2,
                "product": product2,
                "title": "感動しました",
                "content": "これまで読んだ中で最も感動的な本でした。",
                "evaluation_point": 4,
            },
        ]
        for review_data in reviews:
            Review.objects.get_or_create(**review_data)
        self.stdout.write(self.style.SUCCESS('Successfully seeded reviews!'))
