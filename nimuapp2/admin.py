
from django.contrib import admin

 #Register your models here.
from .models import contacts

# Register your models here.

class formAdmin(admin.ModelAdmin):
    
    list_display = ['email','password','password','name','name']


admin.site.register(contacts, formAdmin)
