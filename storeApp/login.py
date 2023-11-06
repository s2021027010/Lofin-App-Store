from fileinput import FileInput
from urllib import request
from django.http import HttpResponseRedirect
from django.urls import reverse
from storeApp.models import db_Profile, db_AppStore
from django.shortcuts import redirect, render
from django.template import loader
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from .models import *
import uuid , re
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth import authenticate,login
from django.contrib.auth.decorators import login_required
from . tokens import generate_token
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode

from LofinApp_Project import settings
from django.http import HttpResponse
from django.core.mail import EmailMessage, send_mail
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes, force_str
from django.contrib.auth import authenticate, login, logout
from . tokens import generate_token


from .views import *
from . import views



# Create your views here.



def login_tab(request):
    # global gb_userIn

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user_obj = User.objects.filter(username = username).first()
        if (len(password) >= 6):
            if user_obj is None:
                messages.error(request, 'User not found.')
                return redirect('login_tab')
            
            
            profile_obj = db_Profile.objects.filter(user = user_obj ).first()

            if not profile_obj.is_verified:
                messages.error(request, 'Profile is not verified check your mail.')
                return redirect('login_tab')

            user = authenticate(username = username , password = password)
            if user is None:
                messages.error(request, 'Wrong password.')
                return redirect('login_tab')
            
            login(request , user)
            global gb_userIn
            gb_userIn = request.POST.get('username')
            return redirect('home')
        else:
            messages.error(request, 'Password Must be six charatcer Long')

    # gb_userIn = request.POST.get('username')
    return render(request , 'account/login.html')


def reset_Password(request):

    if request.method == 'POST':
        input_username = request.POST['input_username']
        input_email = request.POST['input_email']
        input_password = request.POST['resetPassword']
        input_confirmPassword = request.POST['confirmPassword']

        user = User.objects.filter(username = input_username , email = input_email).first()

        if input_password != input_confirmPassword:
            messages.error(request,"Password Didn't Match")
        if user is None:
            messages.error(request, "Email Didn't Match")
        
    try:
        user_obj = User.objects.get(username = input_username, email = input_email)
        profile_obj = db_Profile.objects.filter(db_username = input_username , db_email = input_email).first()
        
        myuser = db_Profile.objects.get(db_username = input_username, db_email = input_email)
        
        if user_obj is None:
            messages.error(request, 'User not found.')
        else:
            profile_obj.is_verified = False
            auth_token = profile_obj.auth_token
            user_obj.set_password(input_password)
            myuser.is_verified = False

            profile_obj.save()
            user_obj.save()
            myuser.save()
            messages.success(request, 'Email Successfully Register. \n We have sent an email to you , \"Please check your mail to Verify\"')
            send_mail_after_registration(input_email , auth_token)
                  
    except Exception as e:
        print(e)
    return render(request , 'account/reset_Password.html')


def send_mail_after_registration(email , token):
    subject = 'Lofin App Store : Activation Code'
    message = f'Welcome to LofinApp !! \n Hi {email} \n Please confirm your email by clicking on the following link.\n \n Confirmation Link: http://127.0.0.1:8000/verify/{token}'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email]
    send_mail(subject, message , email_from , recipient_list, fail_silently = True )


def initialize(): 
    global gb_username
    gb_username = gb_userIn 
    # print(gb_userIn)