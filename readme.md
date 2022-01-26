## 指定ディレクトリの更新を検知して webhook を叩くツール

config.py に更新検知をするディレクトリのパス、webhook の url、webhook のユーザー名などの設定すると通知を送信するよ


## usage

pipenv がインストールされてる環境の場合

```
pipenv install
pipenv run start
```

pipenv なしの場合

```
pip install requests watchdog
python __init__.py
```
