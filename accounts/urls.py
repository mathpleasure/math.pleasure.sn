from django.urls import path
from . import views

urlpatterns = [
    path('login/' , views.login , name='login'),
    path('sign-up/' , views.sign_up , name='sign-up'),
    path('edit-profile/' , views.edit , name='edit-profile'),
    path('contact/' , views.contact , name='contact'),
]