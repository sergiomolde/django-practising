from django.http.response import HttpResponseNotFound
from django.shortcuts import HttpResponse, render
from django.conf import settings
import datetime
import json

# Create your views here.
def index(request):
    return HttpResponse("<p>Hello Django developers</p>")

def today_is(request):
    return render(request, 'datetime.html', {'now': datetime.datetime.now(),
                                             'template_name': 'navbar.html',
                                             'BASE_DIR': settings.BASE_DIR})

# def profilename(request, username=-1):
#     return HttpResponse("<p>Welcome back, %s</p>" % username)

def complex_render(request):
    return render(request, 'markdown.md', content_type='text/markdown')

def profileid(request, user_id=None):
    if user_id == None:
        return HttpResponse("<p>No user_id provided.</p>")
    else:
        return HttpResponse("<p>Welcome back, user number %s</p>" % user_id)

def book_category(request, category):
    return HttpResponse("<p>Books in %s category" % category)

def dictionaryReturn(request, arg1=None, arg2=None):
    return HttpResponse("<p>arg1: {} <br> arg2: {}</p>".format(arg1, arg2))
    # Cambiar el tipo de contenido del retorno
    # return HttpResponse("<p>arg1: {} <br> arg2: {}</p>".format(arg1, arg2), content_type="text/plain")

def custom_response(request):
    data = {'name': "Sergio", 'age': 20}
    return HttpResponse(json.dumps(data), content_type="application/json")


def not_found_response(request):
    return HttpResponseNotFound("Not Found")

def redirect_to(request):

    # Te redirige a una página que le asignes en el res['location']
    # res = HttpResponse(status=302)
    # res['location'] = 'http://example.com/'
    # return res

    # Te descarga un archivo con la información que le devuelvas en el HttpResponse
    # Con res['content-disposition'] le defines el nombre del archivo a descargar y tal.
    res = HttpResponse('some data')
    res['content-disposition'] = 'attachment; filename=file.txt;'
    return res


# Trabajando con los nuevos modelos

def snippet_details(request, snippet_slug):
    return HttpResponse('viewing snippet #{0}', snippet_slug)

def trending_snippets(request, language_slug):
    return HttpResponse('trending {0} snippets'.format(language_slug if language_slug else ""))

def tag_list(request, tag):
    return HttpResponse('viewing tag #{0}', tag)