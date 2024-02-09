from django.shortcuts import render, redirect
from django.views.generic import TemplateView

# Viewを継承したビュークラスを作る
from django.views import View
from .models import Album,Document
from .forms import AlbumForm,DocumentForm

import datetime

from .models import Topic

import magic

ALLOWED_MIME    = [ "application/pdf" ]
# from .import 

# テンプレートをレンダリングする処理(ビュー) TemplateViewを継承して作る。
# class ビュー名(処理名)(TemplateView): 
"""
class TopView(TemplateView):
    # このビューでレンダリングしたいテンプレートを指定する。
    # template_name = "レンダリングしたいテンプレートのパス"
    template_name = "top.html"

    # templates/crud/index.html をレンダリングしたいとき。templatesまでは読んでくれるので、それ以降を書く。
    # template_name = "crud/index.html"
"""

# TODO: このtop.htmlをレンダリングするとき、データを与えたいとき。
"""
class TopView(TemplateView):
    template_name = "top.html"

    def get_context_data(self, **kwargs):
        # TemplateViewの中にある、contextを引き継ぐ。
        context             = super().get_context_data(**kwargs)
        # context は辞書型。
        # ここに レンダリング時のデータを追加する。
        context["message"]  = "Hello!!"

        return context
"""

# Viewを継承したビュークラス。
class TopView(View):

    # リクエストのメソッドで処理を分ける
    def get(self, request, *args, **kwargs):
        context             = {}
        context["message"]  = "Hello!!"

        # レンダリング時に与えるデータのことをコンテキストという。
        #context = {"message","Hello!!"}

        context["score"]    = 90
        # リスト型
        context["numbers"]  = [1,2,3,4,5,6,7,8]

        # 辞書型
        context["profile"]  = {"name":"Bob", "age":20 }


        # 辞書型のリスト (DBからデータを読み込んだとき)
        context["students"] = [ {"number":1 , "name": "Ash"},
                                {"number":2 , "name": "Bash"},
                                {"number":3 , "name": "Cash"},
                                {"number":4 , "name": "Dash"},
                            ]

        # TODO: datetime型、ブーリアン型
        context["dt"] = datetime.datetime.now()
        context["flag"] = True

        topics            = Topic.objects.all()
        context["topics"] = topics
    
        
        if "search" in request.GET:
            print( request.GET["search"] )
        if "view" in request.GET:
            print( request.GET["view"] )
        # 指定したテンプレートをレンダリングする(図の6と7) 
        return render(request, "top.html", context)
    
    #postを追加する
    def post(self, request, *args, **kwargs):
        print("POSTメソッド")
        print( request.POST["comment"] )
        
        topic = Topic()

        topic.comment = request.POST["comment"]

        topic.save()
        
        if "document" in request.FILES:
            print(request.FILES["document"])
        else:
            print("documentがありません")

        """
        if "document" in request.POST:
            print(request.POST["document"])
        else:
            print("documentがありません")
        """

        # return render(request, "top.html")
        return redirect("top")
    
class AlbumView(View):

    def get(self, request, *args, **kwargs):

        context             = {}
        context["albums"]   = Album.objects.all()

        return render(request,"upload/album.html",context)

    def post(self, request, *args, **kwargs):

        form    = AlbumForm(request.POST, request.FILES)
        
        if not form.is_valid():
            print("バリデーションNG")
            print(form.errors)
            return redirect("upload:album")

        print("バリデーションOK")
        form.save()

        return redirect("upload:album")

album   = AlbumView.as_view()

class DocumentView(View):

    def get(self, request, *args, **kwargs):

        context                 = {}
        context["documents"]    = Document.objects.all()

        return render(request,"upload/document.html",context)

    def post(self, request, *args, **kwargs):

        form        = DocumentForm(request.POST,request.FILES)

        if not form.is_valid():
            print("バリデーションNG")
            print(form.errors)
            return redirect("upload:document")

        mime_type   = magic.from_buffer(request.FILES["file"].read(1024) , mime=True)
        
        if not mime_type in ALLOWED_MIME:
            print("このファイルのMIMEは許可されていません。")
            print(mime_type)
            return redirect("upload:document")


        print("バリデーションOK")
        form.save()

        return redirect("upload:document")

document    = DocumentView.as_view()