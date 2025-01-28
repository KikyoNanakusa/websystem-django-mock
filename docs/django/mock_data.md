# mock data management
Djangoの開発環境用に本プロジェクトではモックデータを用意しています.
本ドキュメントではモックデータを挿入する方法について記述します. 

## How to insert mock data
### 開発環境の場合
開発環境の場合は, まず以下のコマンドを使用して, dockerコンテナを立ち上げてください.
```bash
docker compose up --build
```

次に以下のコマンド, もしくはdocker Desktop等を用いて, コンテナに対話形式で入ってください.
```bash
docker run --it django_web bash
```

最後にコンテナ内で以下のコマンドを実行してください
```bash
cd /app
python manage.py makemigrations
python manage.py migrate
python manage.py insert_mock_data
```
