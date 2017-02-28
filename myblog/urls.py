from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^api/posts/?', views.getPosts),
    url(r'^api/post/(?P<post_number>.+)?', views.getAPost),
]
