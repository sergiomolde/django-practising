from django.conf.urls import url
from django.urls.conf import path
from . import views

urlpatterns = [
    path('time/', views.today_is, name='time'),
    # url(r'user/(?P<username>[A-Za-z0-9]+)/$', views.profilename, name="profilename"),
    path('user/<int:user_id>/', views.profileid, name="profileid"),
    path('category/<category>/', views.book_category, name="book_category"),
    path('dictionary/', views.dictionaryReturn, {'arg1': 1, 'arg2': (10, 20, 30)}, name="dictionary"),
    path('custom/', views.custom_response, name="custom_response"),
    path('not_found/', views.not_found_response, name="not_found_exception"),
    path('redirect_to/', views.redirect_to, name="redirect_to"),
    path('', views.index, name="index")
]