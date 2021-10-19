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
    # Paths for new models
    path('trending/', views.trending_snippets, name="trending_snippets"),
    path('trending/<language_slug>', views.trending_snippets, name="trending_snippets"),
    path('tag/<tag>/', views.tag_list, name="tag_list"),
    path('add-snippet/', views.add_snippet, name="add-snippet"),
    path('<snippet_id>/', views.snippet_details, name="snippet_details"),
    path('download/<snippet_id>/', views.download_snippet, name='download_snippet'),
    path('raw/<snippet_id>/', views.raw_snippet, name='raw_snippet'),
    path('trending/<language_slug>/?page=<page_number>', views.trending_snippets, name="trending_snippets"),
    path('language-list/', views.language_list, name="language_list"),
    path('', views.index, name="index"),
]