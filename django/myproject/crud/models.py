from django.db import models

# settings.pyのTIME_ZONEで設定したタイムゾーンを使う。
from django.utils import timezone


# Create your models here.

# このモデルクラス1個分がDBのテーブル1個分に相当する。
class Topic(models.Model):

    # テーブルの列(カラム)に相当する
    # 左辺: カラム名
    # 右辺: データ型( models.CharField() なので、文字列型 ) 制約: 文字列型であり100文字まで、入力必須
    comment = models.CharField(verbose_name="コメント", max_length=100)

    # カラム名: dt
    # 制約: データ型( models.DateTimeField() なので、日時型(datetime型) )、入力必須
    # default=timezone.now : DBにレコード(データ)が与えられる時、自動的に与えられる値(timezone.now) 現在時刻が入る。
    dt      = models.DateTimeField(verbose_name="投稿日時",default=timezone.now)

    # 一旦サーバーを落として(Ctrl + C)、マイグレーションをする。
    # マイグレーションは2つのコマンドで行う。
    # python manage.py makemigrations (モデルを元にマイグレーションファイル(作業手順書)を作る) 
    # python manage.py migrate (マイグレーションファイルを元にDBに反映させるコマンド) 

    # 名前を記録するフィールド
    # カラム名 : name
    # 制約 : 10文字までの文字列型、入力必須。defaultはなし。
    name    = models.CharField(verbose_name="投稿者の名前",max_length=10)
    # It is impossible to add a non-nullable field 'name' to topic without specifying a default.
    # defaultなしで、入力必須のフィールドnameをtopicに追加することはできない。

    # 1) Provide a one-off default now (will be set on all existing rows with a null value for this column)
    # 2) Quit and manually define a default value in models.py.

    # 1) 1度限りのデフォルト値を入れる。
    # 2) モデルを編集してdefaultを与えるか。


    file    = models.FileField(verbose_name="ファイル",upload_to="crud/topic/file/")

