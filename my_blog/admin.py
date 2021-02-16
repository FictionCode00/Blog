from django.contrib import admin
from .models import Category
from.models import blog
# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display=('ID','Name')

class blogAdmin(admin.ModelAdmin):
    list_display=('ID','category','Title','blog','author')    

admin.site.register(Category,CategoryAdmin) 
admin.site.register(blog,blogAdmin)