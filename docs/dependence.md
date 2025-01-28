# dependence
本ドキュメントでは, 依存関係に関する情報を記述します

## python
pythonのバージョンは**3.10**が想定されています. 

pythonのライブラリの依存関係は, `requirements.txt` にまとめられています. 
依存関係をまとめてインストールする際には以下のコマンドを実行してください. 

```bash
pip install -r requirements.txt
```

## PostgresSQL
PostgreSQLはメジャーバージョン15を利用することを想定しています. 
独自のimageを使用する際や, インフラを構築する際には気を付けてください. 

## Terraform
特に依存関係はありません. 
awsのリソースが使えればよいです. 