from django.db import models
from django.contrib.auth.models import User
from .utils import user_dir_path
from .consts import DISTRICTS_LIST

class Location(models.Model):
    adress1=models.CharField(max_length=140,blank=True)
    adress2=models.CharField(max_length=140,blank=True)
    city=models.CharField(max_length=50,blank=True)
    State=models.CharField(max_length=50,choices=DISTRICTS_LIST,blank=True)
    pincode=models.CharField(max_length=10,blank=True)

    def __str__(self):
        return f"Location {self.id}"

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    photo = models.ImageField(upload_to=user_dir_path,null=True)
    bio = models.CharField(max_length=150,blank=True)
    phone_number = models.CharField(max_length=10,blank=True)
    location=models.OneToOneField(Location,on_delete=models.SET_NULL,null=True)

    def __str__(self):
        return f"{self.user.username}'s profile"

