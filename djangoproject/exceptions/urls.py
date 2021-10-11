from django.conf.urls import url
from django.urls.conf import path
from . import views

urlpatterns = [
    path('1/', views.view_func1, name="error1"),
    path('2/', views.view_func2, name="error2"),
    path('3/', views.view_func3, name="error3"),
    path('4/', views.view_func4, name="error4"),
    path('redirect/', views.view_func, name="redirect")
]
