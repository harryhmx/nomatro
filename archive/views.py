from django.http import HttpResponse
from django.template import loader
from nomatro.config import APP_NAMES
from .models import Post

def index(request):
    template = loader.get_template('index.html')
    context = {
        'APP_NAMES':  APP_NAMES,
        'head_title': APP_NAMES['MAIN'],
    }
    return HttpResponse(template.render(context, request))

def posts(request):
    template = loader.get_template('posts.html')
    context = {
        'APP_NAMES':  APP_NAMES,
        'head_title': APP_NAMES['POSTS'],
        'posts':      Post.objects.order_by('-created_at'),
    }
    return HttpResponse(template.render(context, request))
