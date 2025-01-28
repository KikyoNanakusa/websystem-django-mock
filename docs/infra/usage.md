# Usage of terraform

本ドキュメントは, Terraformの使い方について記述します.

## 前提

Terraformは, Infrastructure as Code(IaC)のツールの1つです.
システムに関わるリソースをソースコードで宣言的に管理することができます.  
本リポジトリでは, Terraformを用いてAWSのリソースを管理しています.  

## セットアップ

Terraformで宣言したリソースをAWSにデプロイするためには, 事前にAWSの認証情報を設定する必要があります.
管理者に要請して, 必要な権限を持つIAMユーザを作成し, アクセスキーとシークレットキーを取得してください.

取得したアクセスキーとシークレットキーをデフォルトのプロファイルに設定します.
設定には以下のコマンドを実行します.

```bash
aws configure
```

## デプロイ

適切な権限が設定されていれば, デプロイは非常に簡単です.
以下のコマンドを順番に実行することでデプロイが可能です.

```bash
cd infra
terraform init
terraform plan
terraform apply
```
