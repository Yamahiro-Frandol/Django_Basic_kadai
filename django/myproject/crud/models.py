from django.db import models

# Create your models here.

class Topic(models.Model):
    # テーブルの列（カラム）に相当する
    # 左辺： カラム名
    # 右辺： データ型( modeld.CharField() なので、文字列型 )
    comment = models.CharField(verbose_name="コメント", max_length=100)

class Album(models.Model):

    photo       = models.ImageField(verbose_name="フォト",upload_to="upload/album/photo/")

class Document(models.Model):

    file        = models.FileField(verbose_name="ファイル",upload_to="upload/document/file/")
