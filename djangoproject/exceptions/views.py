from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from django.http import Http404
from django.core.exceptions import SuspiciousOperation, PermissionDenied

# Create your views here.

def view_func(request):
    return redirect('https://www.ayesaworld.com', permanent=True)

    # La url puede aceptar argumentos como
    # return redirect('profile', 'foobar', permanent=True)
    # Redirige a /user/foobar, profile es solo el nombre que le hemos dado en urls.py a la ruta

def view_func1(request):
    return render(request, '404.html', content_type='application/json', status=404)

def view_func2(request):
    return render(request, '400.html', content_type='application/json', status=400)

def view_func3(request):
    return render(request, '403.html', content_type='application/json', status=403)

def view_func4(request):
    context_dict = Exception()
    return render(request, '500.html', status=500)