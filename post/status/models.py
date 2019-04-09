from django.db import models
from django.utils import timezone
from django.conf import settings

# Create your models here.
class post(models.Model):
    author = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    text = models.TextField(max_length=200)
    created_date = models.CharField(max_length=200)
    published_date = models.DateTimeField(blank=True, null=True)	
    
    def publish(self):
    	self.published_date=timezone.now()
    	

    def __str__(self):
    	return self.title	
