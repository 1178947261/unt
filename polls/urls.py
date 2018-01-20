from django.urls import path,re_path
from . import views
'''
例子中，只有一个app也就是polls，但是在现实中很显然会有5个、10个、更多的app同时存在一个项目中。Django是如何区分这些app之间的URL name呢？

答案是使用URLconf的命名空间。在polls/urls.py文件的开头部分，添加一个app_name的变量来指定该应用的命名空间：
app_naem= URL names的命名空间
'''
app_name = 'polls'
urlpatterns = [
    path('', views.index, name='index'),
    # ex: /polls/5/
    path('<int:question_id>/', views.detail, name='detail'),
    # ex: /polls/5/results/
    path('<int:question_id>/results/', views.results, name='results'),
    # ex: /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
]