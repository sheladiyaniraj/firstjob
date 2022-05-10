
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from .models import *
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class Registration(UserCreationForm):  
    username = forms.CharField(label='username', min_length=5, max_length=150)  
    email = forms.EmailField(label='email')  
    password1 = forms.CharField(label='password', widget=forms.PasswordInput)  
    password2 = forms.CharField(label='Confirm password', widget=forms.PasswordInput)  
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'type': 'text','placeholder':'Name'})
        self.fields['email'].widget.attrs.update({'type': 'email','placeholder':'Email'})
        self.fields['password1'].widget.attrs.update({'type': 'Password','placeholder':'Password'})
        self.fields['password2'].widget.attrs.update({'type': 'Password','placeholder':'Confirm Password'}) 
    def username_clean(self):  
        username = self.cleaned_data['username']  
        new = User.objects.filter(username = username)  
        if new.count():  
            raise ValidationError("User Already Exist")  
        return username  
  
    def email_clean(self):  
        email = self.cleaned_data['email'].lower()  
        new = User.objects.filter(email=email)  
        if new.count():  
            raise forms.ValidationError(" Email Already Exist")  
        return email  
  
    def clean_password2(self):  
        password1 = self.cleaned_data['password1']  
        password2 = self.cleaned_data['password2']  
  
        if password1 and password2 and password1 != password2:  
            raise forms.ValidationError("Password don't match")  
        return password2  
    # def save(request,self):
    #     username=request.POST.get('username')
    #     email=request.POST.get('email')
    #     password1 = request.POST.get('password1')
    #     user = User.objects.create_user(username=username,email=email,password1=password1)
    #     return user
    # def save(self, commit = True):  
    #     user = User.objects.create_user(  
    #         self.cleaned_data['username'],  
    #         self.cleaned_data['email'],  
    #         self.cleaned_data['password1']  
    #     )  
    #     return user
       

class FileForm(ModelForm):
    class Meta:
       model = File
       fields = ['resume']


# class Registration(ModelForm):
#     class Meta:
#         model = Signup
#         fields= "__all__"
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.fields['username'].widget.attrs.update({'type': 'text','placeholder':'Name'})
#         self.fields['email'].widget.attrs.update({'type': 'email','placeholder':'Email'})
#         self.fields['password'].widget.attrs.update({'type': 'Password','placeholder':'Password'})
#         self.fields['repassword'].widget.attrs.update({'type': 'Password','placeholder':'Confirm Password'})

class Login(User):
    username = forms.CharField(label='username', min_length=5, max_length=150)
    password1 = forms.CharField(label='password', widget=forms.PasswordInput)

def __init__(self, *args, **kwargs):
    self.fields['username'].widget.attrs.update({'type': 'text','placeholder':'Name'})
    self.fields['password1'].widget.attrs.update({'type': 'Password','placeholder':'Password'})