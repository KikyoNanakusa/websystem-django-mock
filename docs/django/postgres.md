# How to connect to postgreSQL
本ドキュメントでは, DjangoとpostgreSQLを接続するかについて記述されます.

## settings.py
Djangoはデフォルトで, SQLiteを使用する設定となっています. そのため, これについて変更を行う必要があります. 
`settings.py` の以下の記述がこの変更に当たります. 

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('POSTGRES_DB'),
        'USER': os.getenv('POSTGRES_USER'),
        'PASSWORD': os.getenv('POSTGRES_PASSWORD'),
        'HOST': os.getenv('DATABASE_HOST'),
        'PORT': os.getenv('DATABASE_PORT')
    }
}
```

データベースに関する情報は機密情報であるため, 環境変数で管理します. 
環境変数は `load_dotenv()` により, `.env` ファイルから読み込まれます. 
詳しくは環境変数に関するドキュメントを参照してください. 