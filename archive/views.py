from django.http import HttpResponse
from django.template import loader

def index(request):
    print('{}: Request Home Page!'.format(request.get_host()))
    template = loader.get_template('index.html')
    context = {
      'head_title': 'ReallyBraveHearts',
      'body_title': 'Hello World',
      'app_name':   'ReallyBraveHearts',
    }
    return HttpResponse(template.render(context, request))
