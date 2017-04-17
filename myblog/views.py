import json

from django.http import HttpResponse, HttpResponseBadRequest, JsonResponse
from django.shortcuts import get_object_or_404
from django.core import serializers
from django.db.models import F  # http://stackoverflow.com/questions/447117/django-increment-blog-entry-view-count-by-one-is-this-efficient
from django.forms.models import model_to_dict

from myblog.models import Post


def getPosts(request):
    return HttpResponse(serializers.serialize('json', Post.objects.all()))


def getAPost(request, post_number):
    try:
        int(post_number)
    except (ValueError, TypeError):
        return HttpResponseBadRequest('Bad post number. Number required.')

    Post.objects.filter(id=post_number).update(views=F('views')+1)

    post = get_object_or_404(Post, id=post_number)

    return HttpResponse(json.dumps(model_to_dict(post)))


def ElasticSearchView(request):
    return JsonResponse({'data': 'ElasticSearch placeholder.'})
