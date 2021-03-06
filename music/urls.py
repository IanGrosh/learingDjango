from django.conf.urls import url
from . import views

app_name = "music"

urlpatterns = [
    # /music/
    url(r'^$', views.IndexView.as_view(),name="index"),
    # /music/<albumID>/
    url(r'^(?P<pk>[0-9]+)/$',views.DetailView.as_view(),name="detail"),
    # /music/album/add
    url(r'album/add/$',views.AlbumCreate.as_view(),name="album-add")
    # /music/album/<albumID>/update
    #url(r'^(?P<pk>[0-9]+)/$',views.DetailView.as_view(),name="detail"),

]
