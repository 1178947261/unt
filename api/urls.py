from django.urls import path,re_path
from . import views
urlpatterns = [
    path('cur_time', views.cur_time),
    path('postindex', views.userInfo,name="postindex"),
    re_path("sp/([0-9]{4})/", views.sp_2003),
]