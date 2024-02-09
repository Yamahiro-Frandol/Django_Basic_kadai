from django.shortcuts import render, redirect # ← リダイレクト(別のURLへ転送する処理)
from django.views.generic import TemplateView

# Viewを継承したビュークラスを作る
from django.views import View

import datetime

# models.pyからTopicモデルクラスをimportする。
from .models import Topic

# form ~ import でPythonライブラリを読み込みできる
# ↑ 他のPythonファイルを読み込みすることもできる。
# 今回、 crud/views.py が crud/models.py を読み込みする。
# 別のPythonファイルを読み込みするとき、 import models などと .pyを略して書く。
# Djangoを動かしているmanage.pyからみて、crudディレクトリを挟んでmodels.pyがある。そのため、 from . import models 
# ↑だとmodels.py全てを読み込みしてしまう。 Topicだけ読み込みするには、 form .models import Topic



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
    # この引数のrequestはリクエストを送ったクライアントの情報(使用しているブラウザ、IPアドレスの他に、フォームに入力された内容などが含まれている。)
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

        context["dt"]       = datetime.datetime.now()
        
        # ブーリアン型
        context["flag"]     = True


        # TODO:Topicを使って読み込みする。 Topic.objects.all() でTopicテーブルの全データの読み込み
        # データ型は辞書型のリストとほぼ同じなので、同じようにfor文で表示できる。
        topics              = Topic.objects.all()
        context["topics"]   = topics

        # 特定の条件に一致するデータだけ取り出したい。.filter() を使う。
        # Topic.objects.filter(検索条件を書く)
        # 参考: https://noauto-nolife.com/post/django-filter-method/


        # TODO:ここで検索の入力欄に書かれた内容を受け取る。

        # クエリストリングの中に ?search=... が含まれているかチェックする。
        if "search" in request.GET:
            print( request.GET["search"] )
            # 受け取った内容を元に検索処理を実行していく。


        # 指定したテンプレートをレンダリングする(図の6と7) 
        return render(request, "top.html", context)

        # getメソッドでリダイレクトは基本やらない。
        #もしする場合、このビュー自身をリダイレクト先に指定しないように(ループになってしまう。) 
        #return redirect("top")

    # postメソッドを受け取る。
    def post(self, request, *args, **kwargs):
        print("POSTメソッド")

        # フォームに書かれてある内容を受け取る。

        # postメソッドでフォームに書かれてある内容を取り出すには、request.POST["comment"]
        print( request.POST["comment"] )
        # TODO: DBに書き込みをする。

        # クラスからオブジェクト(インスタンス)
        topic = Topic()
        # comment属性(フィールド)に受け取ったコメントを与える。
        topic.comment = request.POST["comment"]
        # TODO:受け取ったコメントはチェックされていない。制約に則っていないデータもDBに保存されてしまう。

        # .save() DBに書き込みをする。
        topic.save()

        # このようにオブジェクトを作る際に引数を与える方法でもOK
        # オブジェクトの名前はなんでも良い。
        """
        posted  = Topic( comment = request.POST["comment"] )
        posted.save()
        """


        # name="document"のファイルを参照する。request.FILES を参照する。
        if "document" in request.FILES:
            print( request.FILES["document"] )
            # TODO: このアップロードされたファイルを読み取って、PDFとエクセルファイルのチェックをする。
            # ↑このアップロードされたファイルは本当にPDFファイルか？チェックをする必要がある。
        else:
            print("documentがありません")

        """
        if "document" in request.POST:
            print(request.POST["document"])
        else:
            print("documentがありません")
        """




        #return render(request, "top.html")
        # redirect(転送先のURL,もしくはURL名)
        return redirect("top")
        # POSTメソッドではリダイレクトを返すようにする。