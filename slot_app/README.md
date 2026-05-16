# 🎰 スロット収支帳 - セットアップ手順

## ディレクトリ構成

```
django_k/
└── slot_app/          ← このフォルダをdjangoフォルダ内に置く
    ├── manage.py
    ├── config/
    │   ├── __init__.py
    │   ├── settings.py
    │   ├── urls.py
    │   └── wsgi.py
    └── slots/
        ├── __init__.py
        ├── admin.py
        ├── models.py
        ├── urls.py
        ├── views.py
        ├── migrations/
        │   └── __init__.py
        └── templates/
            └── slots/
                ├── base.html
                ├── index.html
                └── total.html
```

---

## セットアップ手順

### 1. slot_app フォルダを django_k 内に配置

```
django_k/
└── slot_app/   ← ここに置く
```

### 2. 仮想環境を有効化

```bash
cd django_k
# Windows の場合
.\venv\Scripts\activate

# Mac/Linux の場合
source venv/bin/activate
```

### 3. slot_app フォルダに移動

```bash
cd slot_app
```

### 4. マイグレーション実行（DB作成）

```bash
python manage.py migrate
```

### 5. サーバー起動

```bash
python manage.py runserver
```

### 6. ブラウザでアクセス

```
http://127.0.0.1:8000/
```

---

## スマホで確認する場合

PC と スマホ を同じWiFiに接続した状態で：

```bash
python manage.py runserver 0.0.0.0:8000
```

スマホのブラウザで：
```
http://PCのIPアドレス:8000/
```

（例: http://192.168.1.5:8000/）

---

## 機能説明

| ページ | URL | 内容 |
|--------|-----|------|
| 記録ページ | `/` | 日付・金額・メモを入力して保存 |
| 累計ページ | `/total/` | 累計収支・勝敗数・記録一覧 |

### 記録ページの使い方
1. 日付を確認（自動で今日の日付が入る）
2. ＋500 / ＋1,000 / ＋5,000 ボタンで勝ち金額を加算
3. －500 / －1,000 / －5,000 ボタンで負け金額を加算
4. メモ欄は任意入力
5. 「SAVE 記録する」で保存
