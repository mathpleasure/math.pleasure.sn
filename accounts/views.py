from django.shortcuts import render , redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from .models import Contact

def sign_up(request):
    if request.method == 'POST':
        if ((request.POST['input-username']) and 
            (request.POST['input-email']) and
            (request.POST['input-pass']) and
            (request.POST['input-firstname']) and
            (request.POST['input-lastname'])):
            try:
                user = User.objects.get(username=request.POST['input-username'])
                return render(request, 'accounts/sign-up.html', {'error':'متاسفانه این این نام کاربری قبلا انتخاب شده است !'})
            except User.DoesNotExist:
                user = User()
                user.username = request.POST['input-username']
                user.email = request.POST['input-email']
                user.password = request.POST['input-pass']
                user.first_name = request.POST['input-firstname']
                user.last_name = request.POST['input-lastname']
                user.save()
                auth.login(request, user)
                return redirect('home')
        else:
            return render(request ,'accounts/sign-up.html', {'error':'لطفا اطلاعات کاربری خود را با دقت وارد کنید.'})
    else:
        return render(request , 'accounts/sign-up.html')


def login(request):
    if request.method == 'POST':
        user = auth.authenticate(username=request.POST['input-username'], password=request.POST['input-pass'])
        if ((user is not None) and (request.POST['input-username']) and (request.POST['input-pass'])):
            auth.login(request, user)
            return redirect('home')
        else:
            return render(request, 'accounts/login.html', {'error': 'لطفا اطلاعات کاربری خود را درست وارد کنید.'})
    else:
        return render(request, 'accounts/login.html')

def contact(request):
    if request.method == 'POST':
        if ((request.POST['input-email']) and (request.POST['input-comment'])):
            ticket = Contact()
            ticket.email = request.POST['input-email']
            ticket.message = request.POST['input-comment']
            try:
                ticket.file = request.FILES['input-file']
            except:
                ticket.file = None
            ticket.save()
            return redirect('home')
        else:
            return render(request ,'accounts/contact.html', {'error':'لطفا مقادیر فیلد ها را با دقت وارد کنید.'})
    else:
        return render(request, 'accounts/contact.html')
        
@login_required
def edit(request):
    if request.method == 'POST':
        if ((request.POST['input-username']) and 
            (request.POST['input-email']) and
            (request.POST['input-pass']) and
            (request.POST['input-firstname']) and
            (request.POST['input-lastname'])):
            try:
                user = User.objects.get(username=request.POST['input-username'])
            except User.DoesNotExist:
                return render(request ,'accounts/edit.html', {'error':'لطفا اطلاعات کاربری خود را با دقت وارد کنید.'})   
            else:
                user.email = request.POST['input-email']
                user.set_password(request.POST['input-pass'])
                user.first_name = request.POST['input-firstname']
                user.last_name = request.POST['input-lastname']
                user.save()
                auth.login(request, user)
                return redirect('home')
        else:
            return render(request ,'accounts/edit.html', {'error':'لطفا اطلاعات کاربری خود را با دقت وارد کنید.'})
    else:
        return render(request , 'accounts/edit.html')

