from django.db import models
from django.urls import reverse

# Create your models here.
class contact(models.Model):
    name = models.CharField(max_length=50)
    email= models.EmailField(max_length=100)
    phone_number=models.CharField(max_length=20)
    message=models.CharField(max_length=200)
    
    def __str__(self):
        return self.name
    
    def get_update_url(self):
       
        return reverse('form:update', kwargs={'pk': self.id})
    
    def get_delete_url(self):
       
        return reverse('form:delete', kwargs={'pk': self.id})