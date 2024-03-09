from django.db import models

from django.contrib.auth.models import BaseUserManager



# Create your models here.

from django.db import models

import datetime
import os



def getfilename(request,filename):
    now_time=datetime.datetime.now().strftime("%D%m%d%H:%M:%S")
    new_filename="%s%s"%(now_time,filename)
    return os.path.join('upload/',new_filename)


# Create your models here.
class Trendings(models.Model):
    name=models.CharField(max_length=150,null=False,blank=False)
    image=models.ImageField(upload_to=getfilename,null=True,blank=True)
    description=models.TextField(max_length=500,null=False,blank=False)
    status=models.BooleanField(default=False,help_text="0-default,1-Hidden")
    Trending=models.BooleanField(default=False,help_text="0-default,1-Trending")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class accessories(models.Model):
    
    Name=models.CharField(max_length=150,null=False,blank=False)
    Vendor = models.CharField(max_length=150, null=False, blank=False)
    product_image=models.ImageField(upload_to=getfilename,null=True,blank=True)
    quantity=models.IntegerField(null=False,blank=False)
    original_price = models.FloatField(null=False, blank=False)
    selling_price = models.FloatField(null=False, blank=False)
    description=models.TextField(max_length=500,null=False,blank=False)
    status=models.BooleanField(default=False,help_text="0-default,1-Hidden")
    trending = models.BooleanField(default=False, help_text="0-default,1-Trending")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.Name
    
class vegetables(models.Model):
    Name=models.CharField(max_length=150,null=False,blank=False)
    Vendor = models.CharField(max_length=150, null=False, blank=False)
    product_image=models.ImageField(upload_to=getfilename,null=True,blank=True)
    quantity=models.IntegerField(null=False,blank=False)
    original_price = models.FloatField(null=False, blank=False)
    selling_price = models.FloatField(null=False, blank=False)
    description=models.TextField(max_length=500,null=False,blank=False)
    status=models.BooleanField(default=False,help_text="0-default,1-Hidden")
    trending = models.BooleanField(default=False, help_text="0-default,1-Trending")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.Name
class sports(models.Model):
    Name=models.CharField(max_length=150,null=False,blank=False)
    Vendor = models.CharField(max_length=150, null=False, blank=False)
    product_image=models.ImageField(upload_to=getfilename,null=True,blank=True)
    quantity=models.IntegerField(null=False,blank=False)
    original_price = models.FloatField(null=False, blank=False)
    selling_price = models.FloatField(null=False, blank=False)
    description=models.TextField(max_length=500,null=False,blank=False)
    status=models.BooleanField(default=False,help_text="0-default,1-Hidden")
    trending = models.BooleanField(default=False, help_text="0-default,1-Trending")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.Name
class Fashions(models.Model):
    Name=models.CharField(max_length=150,null=False,blank=False)
    Vendor = models.CharField(max_length=150, null=False, blank=False)
    product_image=models.ImageField(upload_to=getfilename,null=True,blank=True)
    quantity=models.IntegerField(null=False,blank=False)
    original_price = models.FloatField(null=False, blank=False)
    selling_price = models.FloatField(null=False, blank=False)
    description=models.TextField(max_length=500,null=False,blank=False)
    status=models.BooleanField(default=False,help_text="0-default,1-Hidden")
    trending = models.BooleanField(default=False, help_text="0-default,1-Trending")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.Name
class HomeAppliences(models.Model):
    Name=models.CharField(max_length=150,null=False,blank=False)
    Vendor = models.CharField(max_length=150, null=False, blank=False)
    product_image=models.ImageField(upload_to=getfilename,null=True,blank=True)
    quantity=models.IntegerField(null=False,blank=False)
    original_price = models.FloatField(null=False, blank=False)
    selling_price = models.FloatField(null=False, blank=False)
    description=models.TextField(max_length=500,null=False,blank=False)
    status=models.BooleanField(default=False,help_text="0-default,1-Hidden")
    trending = models.BooleanField(default=False, help_text="0-default,1-Trending")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.Name
class Toys(models.Model):
    Name=models.CharField(max_length=150,null=False,blank=False)
    Vendor = models.CharField(max_length=150, null=False, blank=False)
    product_image=models.ImageField(upload_to=getfilename,null=True,blank=True)
    quantity=models.IntegerField(null=False,blank=False)
    original_price = models.FloatField(null=False, blank=False)
    selling_price = models.FloatField(null=False, blank=False)
    description=models.TextField(max_length=500,null=False,blank=False)
    status=models.BooleanField(default=False,help_text="0-default,1-Hidden")
    trending = models.BooleanField(default=False, help_text="0-default,1-Trending")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.Name
class NutritionsandMore(models.Model):
    Name=models.CharField(max_length=150,null=False,blank=False)
    Vendor = models.CharField(max_length=150, null=False, blank=False)
    product_image=models.ImageField(upload_to=getfilename,null=True,blank=True)
    quantity=models.IntegerField(null=False,blank=False)
    original_price = models.FloatField(null=False, blank=False)
    selling_price = models.FloatField(null=False, blank=False)
    description=models.TextField(max_length=500,null=False,blank=False)
    status=models.BooleanField(default=False,help_text="0-default,1-Hidden")
    trending = models.BooleanField(default=False, help_text="0-default,1-Trending")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.Name
class shoesandcheppals(models.Model):
    Name=models.CharField(max_length=150,null=False,blank=False)
    Vendor = models.CharField(max_length=150, null=False, blank=False)
    product_image=models.ImageField(upload_to=getfilename,null=True,blank=True)
    quantity=models.IntegerField(null=False,blank=False)
    original_price = models.FloatField(null=False, blank=False)
    selling_price = models.FloatField(null=False, blank=False)
    description=models.TextField(max_length=500,null=False,blank=False)
    status=models.BooleanField(default=False,help_text="0-default,1-Hidden")
    trending = models.BooleanField(default=False, help_text="0-default,1-Trending")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.Name       
class login(models.Model):
    Username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.Username

class userregister(models.Model):
    Username = models.CharField(max_length=100)
    Email = models.EmailField(unique=True,null=True)
    Password = models.CharField(max_length=100)
    confirm_password = models.CharField(max_length=100)
    

    def __str__(self):
        return self.Username
    def create_user(self,username, email, password, **extra_fields):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(username=username, **extra_fields)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self.mysql_db)
        return self.create_user(username,email,password)
class UserManager:
    def create_user(request):
        # Code to create a new user goes here
        print(" Account created successfully")




class UserManager:
    def create_user(request):
        # Code to create a new user goes hereextra_fields)
        print(" Account created successfully")

   