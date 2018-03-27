from django.db import models
from django.utils import timezone


class Content(models.Model):
    #author = models.ForeignKey('auth.User',on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField(max_length = 20000)
    created_date = models.DateTimeField(
            default=timezone.now)
    
    def __str__(self):
        return self.title