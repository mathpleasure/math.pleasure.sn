from django.shortcuts import render , redirect
from django.contrib import auth
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request , 'mathematical/home.html')
           
def about(request):
    return render(request, 'mathematical/about.html')

@login_required
def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('home')