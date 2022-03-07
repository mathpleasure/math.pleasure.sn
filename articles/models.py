from django.db import models
from django.contrib.auth.models import User

class Article(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)
    image = models.ImageField(upload_to="uploads/",blank=False)
    date = models.DateTimeField()
    content = models.TextField()
    view_count = models.IntegerField(default=0)
    user = models.ForeignKey(User,default=None,on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
class CommentArticle(models.Model):
    comment_for = models.SlugField(max_length=200)
    date = models.DateTimeField()
    comment = models.TextField()
    user = models.ForeignKey(User,default=None,on_delete=models.CASCADE)
	
    def __str__(self):
        comment_show = self.comment[:10]
        return (f'{self.user} نظر داده است.')