from django.contrib import admin

# Register your models here.
from .models import contact

# Register your models here.

class formAdmin(admin.ModelAdmin):
    
    list_display = ['name', 'email','phone_number', 'message']


admin.site.register(contact, formAdmin)
