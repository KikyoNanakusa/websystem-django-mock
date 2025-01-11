from django.core.management.base import BaseCommand
from BookReview.models import Product


class Command(BaseCommand):
    help = 'Add initial product data'

    def handle(self, *args, **kwargs):
        products = [
            {
                "name": "The Great Gatsby",
                "description": "ジャズ時代を舞台にした名作小説。",
                "price": 10.99,
                "isbn": "9780743273565",
            },
            {
                "name": "To Kill a Mockingbird",
                "description": "人種差別をテーマにした感動的な物語。",
                "price": 8.99,
                "isbn": "9780060935467",
            },
        ]
        for product_data in products:
            Product.objects.get_or_create(**product_data)
        self.stdout.write(self.style.SUCCESS('Successfully seeded products!'))
