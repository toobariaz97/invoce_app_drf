from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
 
class UserModel(models.Model):
     email=models.EmailField(max_length=128,verbose_name='Email')
     password=models.CharField(max_length=128,verbose_name="Password")
     
     
     class Meta:
         db_table='user_model'
         verbose_name='UserModel'
         verbose_name_plural="UserModels"
         
class User(AbstractUser):
    pass