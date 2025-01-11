from django.shortcuts import render


def index(request):
    # 書籍データをPythonの辞書で定義
    books = [
        {
            "title": "The Great Gatsby",
            "description": "ジャズ時代を舞台に、富、愛、アメリカンドリームをテーマにした小説。",
            "price": 10.99,
            "isbn": "978-0743273565",
            "created_at": "2023-01-10",
            "updated_at": "2023-06-15",
        },
        {
            "title": "To Kill a Mockingbird",
            "description": "ディープサウスにおける人種と正義についての古典的な物語。",
            "price": 8.99,
            "isbn": "978-0060935467",
            "created_at": "2023-02-20",
            "updated_at": "2023-07-01",
        },
    ]
    # テンプレートにデータを渡す
    return render(request, 'index.html', {'books': books})