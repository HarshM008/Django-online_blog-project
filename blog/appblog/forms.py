from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,UsernameField
from django.contrib.auth.models import User
from django.utils.translation import gettext, gettext_lazy as _
from .models import Blogpost


# Creating signupform from using prebuilt 'usercreationform', changing labels in passwords,  

class SignupForm(UserCreationForm):
    password1 = forms.CharField(label= 'Password', widget= forms.PasswordInput(attrs= {'class' : 'form-control'}))
    password2 = forms.CharField(label = 'Confirm Password (again)', widget= forms.PasswordInput(attrs= {'class' : 'form-control'}))
    class Meta:
        # using required field from prebuilt 'User' model, changing lables and adding styling class.
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
        labels = {'first_name': 'First Name', 'last_name': 'Last Name', 'email': 'Email'}
        widgets = {'username': forms.TextInput(attrs = {'class' : 'form-control'}),
        'first_name': forms.TextInput(attrs = {'class' : 'form-control'}), 
        'last_name': forms.TextInput(attrs = {'class' : 'form-control'}),
        'email': forms.EmailInput(attrs = {'class' : 'form-control'})}


# creating loginform from using prebuilt 'authenticationform' , changing styling class in username and label in password. 
class LoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={'autofocus': True, 'class': 'form-control'}))
    password = forms.CharField(label =_("Password"),strip = False, widget=forms.PasswordInput(attrs={'autocomplete': 'current-password', 'class': 'form-control'}))

# creating modelform with model 'Blogpost', changing labels and adding styling class
class Postform(forms.ModelForm):
    class Meta:
        model = Blogpost
        fields = ['title', 'desc']
        labels = {'title': 'Title', 'desc':'Description'}
        widgets = {'title': forms.TextInput(attrs = {'class' : 'form-control'}),
        'desc': forms.Textarea(attrs = {'class' : 'form-control'}), }
