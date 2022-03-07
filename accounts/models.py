from django.db import models
from django.contrib.auth.models import User

class Contact(models.Model):
    email = models.EmailField()
    message = models.TextField()
    file = models.FileField(blank=True)

    def __str__(self):
        message_show = self.message[:10]
        return (f'{self.email} گفته است : {message_show}.')
    

		
