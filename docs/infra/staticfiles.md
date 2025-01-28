# static files
本ドキュメントでは, gunicornによる静的ファイルの配信についての情報を記述します. 

## 前提
gunicornは静的ファイルを配信しません. そのため, `app/static` 以下のファイルはgunicorn単体では配信されません. 

## 静的ファイルの準備
本番環境では, 静的ファイルは `app/static` から参照されません. 
本番環境用に静的ファイルを用意するには以下のコマンドを実行する必要があります.
```bash
cd app
python manage.py collectstatic
```

## 静的ファイルの配信
静的ファイルの配信には, **nginx** を利用します. 

`/etc/nginx/conf.d/websystem-django.conf` に以下の内容を設定することで, 静的ファイルの配信をnginxに代替させることができます
```nginx
server {
    listen 80;

	# ここにはEC2のipグローバルIPと, ALBのローカルIPを指定
    server_name 111.111.111.111 10.0.1.129;

    location /static/ {
        alias /home/ec2-user/websystem-django-mock/app/static/;
    }

    location / {
        proxy_pass http://127.0.0.1:8000;  # Gunicornが動作しているアドレスとポート
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}
```