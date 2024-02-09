from django.db import models

# Create your models here.

# このモデルクラス1個分がDBのテーブル1個分に相当する。
class Topic(models.Model):

    # テーブルの列(カラム)に相当する
    # 左辺: カラム名
    # 右辺: データ型( models.CharField() なので、文字列型 ) 制約: 文字列型であり100文字まで、入力必須
    comment = models.CharField(verbose_name="コメント", max_length=100)