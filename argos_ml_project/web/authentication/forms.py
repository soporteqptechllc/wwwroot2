from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordResetForm, UserCreationForm,PasswordChangeForm,SetPasswordForm
from django.forms import widgets
from django.contrib.auth.models import(AbstractBaseUser)

# from . models import Register
#View1
class UserLoginForm(forms.Form):
    username=forms.CharField(initial="test",label='Username',widget=forms.TextInput(attrs={'placeholder': 'Enter username', 'id':'user'}),max_length=50,required=True)
    password =forms.CharField(label='Password',widget=forms.PasswordInput(attrs={'placeholder':'Enter password','id':'pwd'}),max_length=10,min_length=2,required=True)
    class Meta:
        model=User
        fields=['username','password']

class UserRegistrationForm(UserCreationForm):
    email=forms.EmailField(max_length=50,required=True,help_text='Required.add valid email address')
    class Meta:
        model=User
        fields=['username','email','password1','password2']



class UserrecoverpwForm(PasswordResetForm):
    email=forms.EmailField(label='Email',widget=forms.EmailInput(attrs={'placeholder': 'Enter email'}),max_length=50,required=True)
    class Meta:
        model=PasswordResetForm
        fields=['email']        

# #View2

class ChangePasswordForm(PasswordChangeForm):
    old_password = forms.CharField(label='Old password',widget=forms.PasswordInput(attrs={'placeholder':'Enter your old password'}),max_length=10,min_length=2,required=True)
    new_password1 = forms.CharField(label='New password',widget=forms.PasswordInput(attrs={'placeholder':'Enter your old password'}),max_length=10,min_length=2,required=True)
    new_password2 = forms.CharField(label='Confirm new password',widget=forms.PasswordInput(attrs={'placeholder':'Enter your old password'}),max_length=10,min_length=2,required=True)
    class Meta:
        model=PasswordChangeForm
        fields=['old_password','new_password1','new_password2']

class ResetPasswordForm(SetPasswordForm):
    new_password1 = forms.CharField(label='New password',widget=forms.PasswordInput(attrs={'placeholder':'Enter your old password'}),max_length=10,min_length=2,required=True)
    new_password2 = forms.CharField(label='Confirm new password',widget=forms.PasswordInput(attrs={'placeholder':'Enter your old password'}),max_length=10,min_length=2,required=True)
    class Meta:
        model=SetPasswordForm
        fields=['new_password1','new_password2']
