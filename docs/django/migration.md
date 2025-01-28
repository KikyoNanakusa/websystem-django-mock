# migration

本ドキュメントではマイグレーションに関する情報を記述します.

## How to migrate

ローカルで開発を行っている場合, `docker-compose.yaml` の記述により, コンテナを立ち上げた際に自動的にマイグレーションが行われます.  
`models.py` に変更を加えた際には, コンテナを再起動してください.  

### 手動マイグレーション

もし, 手動でマイグレーションを行いたい場合には, `django_web` コンテナ内で以下のコマンドを実行してください. 

```bash
cd /app
python manage.py makemigrations
python manage.py migrate
```