from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name= models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
class Product(models.Model):
    category= models.ForeignKey(Category,related_name='products',on_delete=models.CASCADE)
    name= models.CharField(max_length=255)
    price= models.DecimalField(max_digits=10, decimal_places=2)
    description= models.TextField()
    created_at= models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    
