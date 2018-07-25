from django import forms

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from . models import Profile



class signupForm(UserCreationForm):

    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')


    class Meta:
        model = User
        fields = ('username','password1','password2', 'email')



class loginForm(AuthenticationForm):

    class Meta:
        model = User


class userForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('bio', 'degree')