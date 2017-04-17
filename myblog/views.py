from django.http import HttpResponse
from django.core import serializers
from django.db.models import F  # http://stackoverflow.com/questions/447117/django-increment-blog-entry-view-count-by-one-is-this-efficient

from myblog.models import Post


def getPosts(request):
    return HttpResponse(serializers.serialize('json', Post.objects.all()))


def getAPost(request, post_number):
    try:
        int(post_number)
    except ValueError:
        raise ValueError('Number required.')

    Post.objects.filter(id=post_number).update(views=F('views')+1)

    return HttpResponse(
        serializers.serialize('json', Post.objects.filter(id=post_number)),
        content_type='application/json'
    )
