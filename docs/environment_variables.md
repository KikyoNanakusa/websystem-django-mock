# environment variables
本ドキュメントでは, プロジェクトで使用する環境変数について記述されます.

## 環境変数の管理
環境変数は基本的に, プロジェクトのルートに配置された, `.env` ファイルによって管理されます. 
機密情報を安全に管理するために `.env` を使用するため, 当然このファイルはgitの追跡対象外となります. 
プロジェクト管理者と連絡を取って, 適切に開発者に共有してください. 

## .env
`.env`ファイルの内容は以下のようになります.

```yaml
DATABASE_HOST= # postgreSQLのhost名を代入します. ローカルでdockerを使って開発する際は, "db" となります. 本番環境ではRDSのエンドポイントを記載してください.
DATABASE_PORT= # postgreSQLで使用するポート番号を代入します. 基本的には5432となります.
POSTGRES_USER= # postgreSQLのユーザー名を代入します
POSTGRES_PASSWORD= # postgreSQLのパスワードを代入します
POSTGRES_DB= # postgreSQLのデータベース名を代入します

DJANGO_SECRET_KEY= #Djangoのプロジェクトで使用されるSecretKeyを代入します
```

デプロイの自動化を進める場合には, これが変更される可能性が多分にあります. 