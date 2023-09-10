from django.http import HttpResponse
from django.template import loader
from nomatro.config import APP_NAMES, APP_INTRO_HTML
from .models import Post
import markdown

def index(request):
    template = loader.get_template('index.html')
    context = {
        'APP_NAMES':      APP_NAMES,
        'APP_INTRO_HTML': APP_INTRO_HTML,
    }
    return HttpResponse(template.render(context, request))

def posts(request):
    template = loader.get_template('posts.html')
    context = {
        'APP_NAMES': APP_NAMES,
        'posts':     Post.objects.order_by('-created_at'),
    }
    return HttpResponse(template.render(context, request))

def article(request, s):
    article = Post.objects.filter(slug=s)[0]
    article.body = markdown.markdown(article.body, extensions=[
    	           'markdown.extensions.extra',
    	           'markdown.extensions.codehilite',
    	           ])
    template = loader.get_template('article.html')
    context = {
        'APP_NAMES': APP_NAMES,
        'article':   article,
    }
    return HttpResponse(template.render(context, request))
