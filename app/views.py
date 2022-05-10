import email
import re
from tkinter import S, Y
from wsgiref.validate import validator
from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseRedirect
from . models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib import messages
from .forms import *
from django.core.exceptions import ValidationError
from django.contrib.auth import authenticate, login ,logout
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from firstjob import settings
from django.contrib.auth.forms import UserCreationForm  ,AuthenticationForm



def home(request):
   form = FileForm()
   if request.method == 'POST':
      first_name = request.POST.get('first_name')
      last_name = request.POST.get('last_name')
      country = request.POST.get('country')
      subject = request.POST.get('subject')
      contactus = ContactUs(first_name=first_name,last_name=last_name,country=country,subject=subject)
      contactus.save()
      return redirect("/")
                    #print(first_name,last_name,country,subject)
   else:
      pass

   return render(request, 'app/index.html',{'form':form})

# Create your views here.

def about(request):
                    return render(request, 'app/aboutus.html')


@login_required(login_url='login')
def feedback(request):
      if request.method == 'POST':
         fname = request.POST.get('fname')
         
         hear = request.POST.get('hear')
         rate = request.POST.get('rate')
         comments = request.POST.get('comments')
         feedback = F(name=fname,hear=hear,rate=rate,comments=comments)
         feedback.save()
         return render(request, 'app/thanks.html')
      else:
         pass
      return render(request, 'app/feedback.html')


@login_required(login_url='login')
def upload(request):

   form = FileForm(request.POST)

   if request.method == 'POST':
      form = FileForm(request.POST, request.FILES)

      if form.is_valid():
         form.save()
         return redirect('/')
      
      else:
         return HttpResponse('Something went wrong!')

   return render(request, 'app/index.html')

# def register(request):
#      if request.method == "POST":  
#         form = Registration(request.POST)  
#         if form.is_valid():
#             password=request.POST.get('password')
#             repassword=request.POST.get('repassword')

#             if Signup.objects.filter(username=request.POST.get('username')).exists():
#                messages.error(request, " User is already exist")
#                return render(request,'app/signup.html')
#             if Signup.objects.filter(email=request.POST.get('email')).exists():
#                messages.error(request, " User is already exist")
#                return render(request,'app/signup.html')
#             if (password!= repassword):
#                messages.error(request,"Password not matching!!")
#                return render(request,'app/signup.html')
#             else:
#                     form.save()
#                     subject = "Greetings"  
#                     msg     = "You are Successfully Registered in FirstJob...."  
#                     to      = request.POST.get('email')
#                     res     = send_mail(subject, msg, settings.EMAIL_HOST_USER, [to])  
#                     if(res == 1): 
#                      form = Registration()
#                      return render(request,'app/index.html') 
#                     else:  
#                      pass
                    
#             #     error('Password not matched!!!!!')
#      else:  
#         form = Registration()  
#      return render(request,'app/signup.html',{'form':form})

def register(request):
   #  if request.user.is_authenticated:
   #      return redirect('/')
    if request.method == 'POST':
        form = Registration(request.POST)
        if form.is_valid():
            username=request.POST.get('username')
            email=request.POST.get('email')
            password1 = request.POST.get('password1')
            user = User.objects.create_user(username=username,email=email,password=password1)
            user.save()
            # email = request.POST.get('email')
            # password1 = request.POST.get('password1')
            # user = authenticate(email=email, password1=password1)
            # login(request, user)
            subject = "Greetings"  
            msg     = "You are Successfully Registered in FirstJob...."  
            to      = request.POST.get('email')
            res     = send_mail(subject, msg, settings.EMAIL_HOST_USER, [to])  
            if(res == 1): 
             form = Registration()
             redirect('index/') 
            else:  
               pass 
            return render(request,'app/index.html')
        else:
            return render(request, 'app/signup.html', {'form': form})
    else:
        form = Registration()
        return render(request, 'app/signup.html', {'form': form})

# def loginnew(request):
#    if not request.user.is_authenticated:
#       if request.method == 'POST':
#          form=AuthenticationForm(request=request,data=request.POST) 
#          if form.is_valid():
#             username = form.cleaned_data('username')
#             password1 = form.cleaned_data('password1')
#             user = authenticate(username=username,password=password1)
#             if user is not None:
#                login(request,user)
#                return redirect('index/')
#             else:
#                return render(request, 'app/signup.html', {'form': form})
#          else:
#             form=AuthenticationForm()
#          return render(request, 'app/signup.html', {'form': form})     
#       else:
#          form=AuthenticationForm()
#       return render(request, 'app/signup.html', {'form': form})
#    else:
#       return render(request,'app/signup.html')

def loginnew(request):
   if not request.user.is_authenticated:
    if request.method == 'POST':
        form=Login(request.POST)
        username = request.POST.get('username')
        password1 = request.POST.get('password1')
        user = authenticate(request, username=username, password=password1)

        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.info(request, 'Try again! username or password is incorrect')
            form = Registration()
            return render(request, 'app/signup.html', {'form': form})
    context = {}
    return render(request, 'app/signup.html', context)
   return render(request, 'app/signup.html', context)
# def loginnew(request):
#    if request.method == 'POST':
      
#       user = authenticate(request,email=request.POST.get('email'), password=request.POST.get('password'))
#       if user is not None:
#          login(request,user)
#          return redirect("home")
#       else:
#          return render(request, 'app/signup.html')
   
#    return render(request, 'app/signup.html')

@login_required(login_url='login')
def userlogout(request):
   logout(request,)
   return render(request, 'app/index.html')


