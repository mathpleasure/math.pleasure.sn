from django.contrib import admin
from django.urls import path , include
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home , name='home'),
    path('admin/', admin.site.urls),
    path('about/' , views.about , name='about'),
    path('logout/' , views.logout , name='logout'),
    path('accounts/', include('accounts.urls') , name='accounts'),
    path('articles/', include('articles.urls') , name='articles'),
    path('topics/', include('topics.urls') , name='topics'),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL , document_root=settings.MEDIA_ROOT)