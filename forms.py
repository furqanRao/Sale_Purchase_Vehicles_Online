from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from vehicles_app.models import Posts, UserInfo
from enum import Enum
from django.conf import settings


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')



class AddFile(forms.ModelForm):
    details = forms.CharField(widget=forms.Textarea)
    class Meta:
        model = Posts
        fields = ('category','full_name','phone','title','city','price','brand','modelyear','condition','mileage',
                  'details','air_conditioner','power_windows','power_steering','automatic_break_system','air_bags',
                  'cd_player','image','image1','image2','image3','image4','image5','image6','image7','image8','image9')
