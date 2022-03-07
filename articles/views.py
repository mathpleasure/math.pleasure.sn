from django.shortcuts import render , redirect
from .models import Article , CommentArticle
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.db.models import Q

@login_required(login_url = "/accounts/login")
def create(request):
    if request.method == 'POST':
        if ((request.POST['input-name-blog']) and
            (request.FILES['input-image-header']) and
            (request.POST['input-slug']) and
            (request.POST['input-blog'])):
            try:
                article = Article.objects.get(title=request.POST['input-name-blog'])
                return render(request ,'articles/create.html', {'error':'لطفا عنوان مقاله را تکراری وارد نکنید.'})
            except Article.DoesNotExist:
                article = Article()
                article.title = request.POST['input-name-blog']
                article.slug = request.POST['input-slug']
                article.image = request.FILES['input-image-header']
                article.date = timezone.datetime.now()
                article.user = request.user
                article.content = request.POST['input-blog']
                article.save()
                return redirect('/articles/' + str(article.slug))
        else:
            return render(request ,'articles/create.html', {'error':'لطفا مقادیر فیلد ها را با دقت وارد کنید.'})
    else:
        return render(request, 'articles/create.html')

def article(request, slug):
    try:
        article = Article.objects.get(slug=slug)
        article.view_count += 1
        article.save()
        comments = CommentArticle.objects.all().filter(Q(comment_for=slug)).order_by('-date')
        return render(request, 'articles/article.html',{'article':article,'comments':comments})
    except CommentArticle.DoesNotExist:
        return render(request, 'articles/article.html',{'article':article})        
    except Article.DoesNotExist:
        return HttpResponseNotFound("صفحه مورد نظر پیدا نشد!")

def articles(request):
    articles = Article.objects.all().order_by('-date')
    args = {'articles':articles}
    return render(request, 'articles/items.html', args)

@login_required
def create_comment_article(request):
    if request.method == 'POST':
        if ((request.POST['input-blog']) and (request.POST['input-comment-slug'])):
            comment = CommentArticle()
            comment.comment_for = request.POST['input-comment-slug']
            comment.date = timezone.datetime.now()
            comment.user = request.user
            comment.comment = request.POST['input-blog']
            comment.save()  
    return redirect('/articles/' + str(request.POST['input-comment-slug']))

@login_required
def edit_article(request):
    if request.method == 'POST':
        if request.POST['get-article']:
            article = Article.objects.get(title=request.POST['get-article'])
            return render(request, 'articles/edit.html', {'article':article})

@login_required
def editor_article(request):
    if request.method == 'POST':
        if ((request.POST['input-name-blog']) and
            (request.POST['input-slug']) and
            (request.POST['input-blog'])):
            article = Article.objects.get(title=request.POST['input-name-blog'])
            article.content = request.POST['input-blog']
            article.date = timezone.datetime.now()
            article.save()
            return redirect('/articles/' + str(article.slug))
        else:
            return render(request ,'articles/edit.html', {'error':'لطفا مقادیر فیلد ها را با دقت وارد کنید.'})
    else:
        return render(request, 'articles/edit.html')

def search_article(request):
    search = request.GET['search-input']
    articles = Article.objects.all().filter(Q(title__icontains=search)|Q(content__contains=search)).order_by('-date')
    args = {'articles':articles}
    return render(request, 'articles/items.html', args)

def my_articles(request):
    my_user = request.user.username
    articles = Article.objects.all().filter(user__username=my_user).order_by('-date')
    args = {'articles':articles}
    return render(request, 'articles/items.html', args)