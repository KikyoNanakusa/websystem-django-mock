# Setup
本ドキュメントには, どうしても期間中に自動化できなかったインフラのセットアップ手順を示しておく
今後, Terraform, Ansibleの組み合わせによって, これらの作業を自動化することが計画されている. 

## 環境変数
EC2上で環境変数を設定する必要がある. 
`.env` の内容をそのまま設定すればよい

## nginxの設定
`/etc/nginx/conf.d/websystem-django.conf` に以下の内容を設定する必要がある. 
```nginx
server {
    listen 80;

	# ここにはEC2のipグローバルIPと, ALBのローカルIPを指定
    server_name 111.111.111.111 10.0.1.129;

    location /static/ {
        alias /home/ec2-user/websystem-django-mock/app/static/;
    }

    location / {
        proxy_pass http://127.0.0.1:8000;  # Gunicorn>が動作しているアドレスとポート
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}
```

## nginxの起動
以下のコマンドで起動できる
```bash
sudo nginx -t
sudo systemctl restart nginx
```

## djangoのセットアップ
`websystem-django/app/BookReview/setting.py` の `ALLOW_HOSTS` にEC2のグローバルIP, ALBのローカルIPを追加する必要がある. 

## 静的ファイルの用意
`websystem-django/app` にて以下のコマンドを実行する必要がある. 
```bash
python3 manage.py collectstatic
```

## gunicornの起動
`websystem-django/app` にて以下のコマンドを実行し, サーバーを起動する必要がある. 
```bash
gunicorn BookReview.wsgi:application --bind 0.0.0.0:8000 --workers 3 --daemon
```