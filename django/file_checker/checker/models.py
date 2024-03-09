from django.db import models
from django.utils import timezone

class Document(models.Model):

    created_at  = models.DateTimeField(verbose_name="投稿日時",default=timezone.now)
    
    pdf         = models.FileField(verbose_name="PDFファイル", upload_to="checker/document/pdf/")
    excel       = models.FileField(verbose_name="excelファイル", upload_to="checker/document/excel/")
