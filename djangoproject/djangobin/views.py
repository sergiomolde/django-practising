from django.http.response import HttpResponseNotFound
from django.shortcuts import (HttpResponse, render, redirect,
                              get_object_or_404, reverse, get_list_or_404)
from .utils import paginate_result
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from .models import Snippet
from djangobin.forms import SnippetForm
from django.conf import settings
from django.contrib import messages
from .models import Language, Snippet
import datetime
import json
import time

# Create your views here.
def index(request):
    return render(request, 'index.html')

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

def snippet_details(request, snippet_id):
    recent_snippet = Snippet.objects.filter(exposure='public').order_by("-created_on")[:8]
    snippet = get_object_or_404(Snippet, id=snippet_id)
    snippet.hits += 1
    snippet.save()
    return render(request, 'snippet_detail.html', {'snippet': snippet, 
                                                             'recent_snippet': recent_snippet})


def tag_list(request, tag):
    return HttpResponse('viewing tag #{0}', tag)

def add_snippet(request):        
    if request.method ==  'POST':
        f = SnippetForm(request.POST)
        if f.is_valid():
            snippet = f.save(request)
            return redirect(reverse('snippet_details', args=[snippet.id]))
    else:
        f = SnippetForm()

    return render(request, 'add_snippet.html', {'form': f})

def download_snippet(request, snippet_id):
    snippet = get_object_or_404(Snippet, id=snippet_id)
    file_extension = snippet.language.file_extension
    filename = snippet.slug + file_extension
    res = HttpResponse(snippet.original_code)
    res['content-disposition'] = 'attachment; filename'  + filename + ';'
    return res

def trending_snippets(request, language_slug=''):
    lang = None
    snippets = Snippet.objects
    if language_slug:
        snippets = snippets.filter(language__slug=language_slug)
        lang = get_object_or_404(Language, slug=language_slug)
    snippet_list = get_list_or_404(snippets.filter(exposure='public').order_by('-hits'))
    snippets = paginate_result(request, snippet_list, 5)
    paginator = Paginator(snippets, 5)

    # get the page parameter from the query string
    # if page parameter is available get() method will return empty string ''
    page = request.GET.get('page')

    try:
        # create Page object for the given page
        posts = paginator.page(page)
    except PageNotAnInteger:
        # if page parameter in the query string is not available, return the first page
        snippets = paginator.page(1)
    except EmptyPage:
        # if the value of the page parameter exceeds num_pages then return the last page
        snippets = paginator.page(paginator.num_pages)
    return render(request, 'trending.html', {'snippets': snippets, 'lang': lang})


def tag_list(request, tag):
    t = get_object_or_404(Tag, name=tag)
    snippet_list = get_list_or_404(t.snippet_set)
    snippets = paginate_result(request, snippet_list, 5)
    return render(request, 'djangobin/tag_list.html', {'snippets': snuppets, 'tag': t})

def raw_snippet(request, snippet_id):
    snippet = get_object_or_404(Snippet, id=snippet_id)
    return HttpResponse(snippet.original_code, content_type=snippet.language.mime)

def language_list(request):
    return render(request, 'language_list.html', {'language_list': Language.objects.all()})

def handler404(request, exception, template_name="index.html"):
    return render(request, template_name)