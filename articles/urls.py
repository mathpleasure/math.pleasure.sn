from django.urls import path 
from . import views

urlpatterns = [
    path('articles/', views.articles , name='articles'),
    path('create-article/', views.create , name='create-article'),
    path('edit-article/', views.edit_article , name='edit-article'),
    path('my-articles/', views.my_articles , name='my-articles'),
    path('editor-article/', views.editor_article , name='editor-article'),
    path('search-article/', views.search_article , name='search-article'),
    path('create-comment-article/', views.create_comment_article , name='create-comment-article'),
    path('<slug>' , views.article , name='article'),
]