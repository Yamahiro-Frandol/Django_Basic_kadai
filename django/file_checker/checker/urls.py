from django.urls import path
# views.pyをimportする
from . import views

app_name    = "checker"
urlpatterns = [
    # views.pyのindex処理を呼び出す。
    path("", views.index)

]