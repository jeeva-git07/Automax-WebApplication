
from django import forms
from django.contrib.auth.models import User
from .models import Location,Profile
from .widgets import CustomPhoto

class UserForm(forms.ModelForm):
    username=forms.CharField(disabled=True)
    class Meta:
        model=User
        fields={"username"}

class ProfileForm(forms.ModelForm):
    photo=forms.ImageField(widget=CustomPhoto)
    class Meta:
        model=Profile
        fields=("photo","bio","phone_number")


class LocationForm(forms.ModelForm):
    pincode=forms.CharField(required=True)
    State=forms.CharField(required=True)
    class Meta:
        model=Location
        fields={"adress1","adress2","city","State","pincode"}