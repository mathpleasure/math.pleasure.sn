from django.urls import path 
from . import views

urlpatterns = [
    path('topics/', views.topics , name='topics'),
    path('create-topic/', views.create , name='create-topic'),
    path('edit-topic/', views.edit_topic , name='edit-topic'),
    path('my-topics/', views.my_topics , name='my-topics'),
    path('editor-topic/', views.editor_topic , name='editor-topic'),
    path('search-topics/', views.search_topics , name='search-topics'),
    path('create-comment-topic/', views.create_comment_topic , name='create-comment-topic'),
    path('<slug>' , views.topic , name='topic'),
]