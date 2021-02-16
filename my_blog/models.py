from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Category(models.Model):
    ID=models.AutoField(primary_key=True)
    Name=models.CharField(max_length=30)

    def __str__(self):
        return self.Name
    

class blog(models.Model):
    ID=models.AutoField(primary_key=True) 
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    Title=models.CharField(max_length=100)
    blog=models.CharField(max_length=100)
    author=models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.Title

    
