from django.http import HttpResponse
from django.template import loader

def index(request):
    template = loader.get_template('index.html')
    context = {
      'head_title': 'ReallyBraveHearts',
      'body_title': 'Hello World',
      'app_name':   'ReallyBraveHearts',
    }
    return HttpResponse(template.render(context, request))

def posts(request):
    template = loader.get_template('posts.html')
    context = {
      'head_title': 'ReallyBraveHearts',
      'body_title': 'Posts Page',
      'app_name':   'ReallyBraveHearts',
    }
    return HttpResponse(template.render(context, request))
