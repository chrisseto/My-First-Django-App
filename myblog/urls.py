from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^api/get posts/?', views.getPosts),
    url(r'^api/get post/(?P<yo_numbah>.+)?', views.getAPost),
]
