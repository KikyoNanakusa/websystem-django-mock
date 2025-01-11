from django.core.management.base import BaseCommand
from BookReview.models import User


class Command(BaseCommand):
    help = 'Add initial user data'

    def handle(self, *args, **kwargs):
        users = [
            {
                "name": "John Doe",
                "email": "john@example.com",
                "password": "hashed_password1",  # ハッシュ化されたパスワードを使用することを推奨
            },
            {
                "name": "Jane Smith",
                "email": "jane@example.com",
                "password": "hashed_password2",  # ハッシュ化されたパスワードを使用することを推奨
            },
        ]
        for user_data in users:
            User.objects.get_or_create(**user_data)
        self.stdout.write(self.style.SUCCESS('Successfully seeded users!'))
