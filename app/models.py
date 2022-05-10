from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
# Create your models here.
#
class ContactUs(models.Model):
                    first_name = models.CharField(max_length=200,blank=True,null=True)
                    last_name = models.CharField(max_length=200,blank=True,null=True)
                    country = models.CharField(max_length=200,blank=True,null=True)
                    subject = models.TextField(max_length=500,blank=True,null=True)

                    def __str__(self):
                        return self.first_name

class File(models.Model):
    resume = models.FileField(upload_to="first/",null=True,default=None)
    def __str__(self):
        return str(self.resume)
class F(models.Model):
    name = models.CharField(max_length=200,default=None)
    
    hear = models.CharField(max_length=200,default=None)
    rate = models.CharField(max_length=200,default=None)
    comments = models.TextField(max_length=500,default=None)

    def __str__(self):
        return self.name
    
# class Signup(models.Model):
#     username = models.CharField(max_length=50,blank=True,null=False,default=None)
#     email = models.EmailField(max_length=50,blank=True ,null=True,default=None)
#     password = models.CharField(max_length=50,blank=True,null=True,default=None)
#     repassword = models.CharField(max_length=50,blank=True,null=True,default=None)

#     def __str__(self):
#             return str(self.username)
    
