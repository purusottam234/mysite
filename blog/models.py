from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class Post(models.Model):
    STATUS_CHOICES = (
        ('draft','Draft'),
        ('published','Published')
    )
    title = models.CharField(max_length=50)
    slug = models.SlugField( max_length=50, unique_for_date='publish')
    author = models.ForeignKey(User, on_delete=models.CASCADE,related_name='blog_posts')
    body = models.TextField()
    publish = models.DateTimeField( auto_now=False, auto_now_add=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    status = models.CharField( max_length=50,choices = STATUS_CHOICES,default= 'draft')
    class Meta:
        ordering = ('-publish',)
    def __str__(self):
        return self.title
    
