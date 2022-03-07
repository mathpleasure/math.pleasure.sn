from django.shortcuts import render , redirect
from .models import Topic , CommentTopic
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseNotFound
from django.utils import timezone
from django.db.models import Q

@login_required(login_url = "/accounts/login")
def create(request):
    if request.method == 'POST':
        if ((request.POST['input-name-blog']) and
            (request.POST['input-slug']) and
            (request.POST['input-blog'])):
            try:
                topic = Topic.objects.get(title=request.POST['input-name-blog'])
                return render(request ,'topics/create.html', {'error':'لطفا عنوان پرسش را تکراری وارد نکنید.'})
            except Topic.DoesNotExist:
                topic = Topic()
                topic.title = request.POST['input-name-blog']
                topic.slug = request.POST['input-slug']
                topic.date = timezone.datetime.now()
                topic.user = request.user
                topic.content = request.POST['input-blog']
                topic.save()
                return redirect('/topics/' + str(topic.slug))
        else:
            return render(request ,'topics/create.html', {'error':'لطفا مقادیر فیلد ها را با دقت وارد کنید.'})
    else:
    	return render(request, 'topics/create.html')

def topic(request, slug):
    try:
        topic = Topic.objects.get(slug=slug)
        topic.view_count += 1
        topic.save()
        comments = CommentTopic.objects.all().filter(Q(comment_for=slug)).order_by('-date')
        return render(request, 'topics/topic.html',{'topic':topic,'comments':comments})
    except CommentTopic.DoesNotExist:
        return render(request, 'topics/topic.html',{'topic':topic})
    except Topic.DoesNotExist:
        return HttpResponseNotFound("صفحه مورد نظر پیدا نشد!")

def topics(request):
    topics = Topic.objects.all().order_by('-date')
    args = {'topics':topics}
    return render(request, 'topics/items.html', args)

@login_required
def create_comment_topic(request):
    topics = Topic.objects.all().order_by('-date')
    if request.method == 'POST':
        if ((request.POST['input-blog']) and (request.POST['input-comment-slug'])):
            comment = CommentTopic()
            comment.comment_for = request.POST['input-comment-slug']
            comment.date = timezone.datetime.now()
            comment.user = request.user
            comment.comment = request.POST['input-blog']
            comment.save()    
    return redirect('/topics/' + str(request.POST['input-comment-slug']))

@login_required
def edit_topic(request):
    if request.method == 'POST':
        if request.POST['get-topic']:
            topic = Topic.objects.get(title=request.POST['get-topic'])
            return render(request, 'topics/edit.html', {'topic':topic})

@login_required
def editor_topic(request):
    if request.method == 'POST':
        if ((request.POST['input-name-blog']) and
            (request.POST['input-slug']) and
            (request.POST['input-blog'])):
            topic = Topic.objects.get(title=request.POST['input-name-blog'])
            topic.content = request.POST['input-blog']
            topic.date = timezone.datetime.now()
            topic.save()
            return redirect('/topics/' + str(topic.slug))
        else:
            return render(request ,'topics/edit.html', {'error':'لطفا مقادیر فیلد ها را با دقت وارد کنید.'})
    else:
        return render(request, 'topics/edit.html')

def search_topics(request):
    search = request.GET['search-input']
    topics = Topic.objects.all().filter(Q(title__icontains=search)|Q(content__contains=search)).order_by('-date')
    args = {'topics':topics}
    return render(request, 'topics/items.html', args)

def my_topics(request):
    my_user = request.user.username
    topics = Topic.objects.all().filter(user__username=my_user).order_by('-date')
    args = {'topics':topics}
    return render(request, 'topics/items.html', args)