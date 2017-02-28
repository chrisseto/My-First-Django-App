from django.http import HttpResponse, JsonResponse

from myblog.models import Post
from django.core import serializers
from django.db.models import F #http://stackoverflow.com/questions/44711/django-increment-blog-entry-view-count-by-one-is-this-efficient


def getPosts(request):
    posts_to_return = Post.objects.all()  # Make an empty list

    return HttpResponse(posts_to_return, content_type='application/json')


def getAPost(request, post_number):
        try:
            int(post_number)
        except ValueError:
            raise ValueError('Number required.')

        # h = PostView()
        # h.forWhatPost = int(yo_numbah)  # Needs to be an number
        # h.save()
        Post.objects.filter(id=post_number).update(views=F('views')+1)

        return HttpResponse(
            serializers.serialize("json", Post.objects.filter(id=1)),content_type='application/json')
