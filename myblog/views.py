from django.http import HttpResponse, JsonResponse

from myblog.models import Post, PostView


def getPosts(request):
    posts_to_return = list();  # Make an empty list

    m = 0
    while True:
        m = m + 1
        if m >= Post.objects.count():
            break;

        l = Post.objects.all()[m];

        posts_to_return.append({
            'id': l.id,
            'author': l.author,
            'title': l.title,
            'content': l.content,
            'count': len(PostView.objects.filter(forWhatPost=l.id))
        });

    # This does work???
    # return JsonResponse(posts_to_return);
    return HttpResponse(posts_to_return, content_type='application/json');



def getAPost(request, yo_numbah):
    if not isinstance(eval(yo_numbah), int):
        return HttpResponse("No a number!", status_code=400)

    u = Post.objects.raw('SELECT * FROM myblog_post WHERE id = ' + yo_numbah)[0];

    h = PostView();
    h.forWhatPost = eval(yo_numbah);#Needs to be an number
    h.save();

    i = {o: getattr(u, o) for o in ('id', 'author', 'title', 'content')};
    return JsonResponse(i)
