from django.db import models
from django.urls import reverse

# Create your models here.
class contacts(models.Model):
    email = models.EmailField(max_length=50)
    password=models.CharField(max_length=20)
    password=models.CharField(max_length=20)
    name=models.CharField(max_length=20)
    name=models.CharField(max_length=20)
    
    def __str__(self):
        return self.name
    
    def get_update_url(self):
        return reverse('home1:update1', kwargs={'pk': self.id})
    
    