"""djangoproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls.conf import include

# Ahora si usamos el reverse() en el shell debemos indicar lo siguiente
# djangobin:profile \\ djangobin:example
# Esto sirve para distinguir entre aplicaciones de django que tengamos en la misma carpeta
app_name = 'djangobin'

urlpatterns = [
    path('', include('djangobin.urls')),
    path('exception/', include('exceptions.urls')),
    path('admin/', admin.site.urls),
]
