from fileinput import FileInput
from urllib import request
from django.http import HttpResponseRedirect
from django.urls import reverse
from storeApp.models import db_Profile
from django.shortcuts import redirect, render
from django.template import loader
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from .models import *
import uuid, re
from django.conf import settings
from django.contrib.auth.decorators import login_required
from LofinApp_Project import settings
from django.http import HttpResponse
from django.core.mail import EmailMessage, send_mail
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.utils.encoding import force_bytes, force_str
from django.contrib.auth import authenticate, login, logout
from . tokens import generate_token

from .login import *
from . import login



# Create your views here.




def register(request):
    mypersonal = db_Profile.objects.all().values()
    return render(request=request, template_name="account/register.html", context={ 'myregister': mypersonal, })


def addrecord(request):
    
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        fname =  request.POST.get('input_firstName')
        lname =  request.POST.get('input_lastName')
        #print(password)
# _________________________________________________________________________________________--
        db_username=request.POST['username']
        db_email=request.POST['email']
        db_photo = request.POST['input_imageP']
        db_firstName=request.POST['input_firstName']
        db_lastName=request.POST['input_lastName']
        db_password=request.POST['password']
        db_Confirm_password=request.POST['input_Confirm_password']
        db_phoneNumber=request.POST['input_phoneNumber']
        db_address=request.POST['input_address']
        db_date_DoB=request.POST['input_date_DoB']
        db_exper=request.POST['input_exper']
        db_hourly=request.POST['input_hourly']
        db_speak=request.POST['input_speak']
        db_available=request.POST['input_available']
        db_bio=request.POST['input_bio']

        if len(db_phoneNumber) >= 13:
            messages.error(request,"Phone number Must be under 13 Digits.")
            return redirect('register')
        elif not len(db_password) >= 6:
            messages.error(request,"Password Must be six charatcer Long")
            return redirect('register')
        else:
            if db_password != db_Confirm_password:
                messages.error(request,"Password Didn't Match")
                return redirect('register')
#__________________________________________________________________________________________--
    try:
        
        if re.findall("@", username):
            messages.error(request, 'username cann\'t hold  " @ " .')
            return redirect('register')
        if re.findall("[.]", username):
            messages.error(request, 'username cann\'t hold  " . " .')
            return redirect('register')
        if re.findall("@gmail.com\Z", username):
            messages.error(request, 'username cann\'t hold  " @gmail.com " .')
            return redirect('register')

        if User.objects.filter(username = username).first():
            messages.error(request, 'Username is already Taken.')
            return redirect('register')

        if User.objects.filter(email = email).first():
            messages.error(request, 'Email is already Taken.')
            return redirect('register')
            
        user_obj = User(username = username , email = email)
        user_obj.first_name = fname
        user_obj.last_name = lname
        user_obj.set_password(password)
        user_obj.save()
        auth_token = str(uuid.uuid4())
        profile_obj = db_Profile.objects.create(user = user_obj ,
        auth_token = auth_token,
        db_username=db_username,
        db_email=db_email,
        db_photo=db_photo,
        db_firstName=db_firstName,
        db_lastName=db_lastName,
        db_phoneNumber=db_phoneNumber,
        db_address=db_address,
        db_date_DoB=db_date_DoB,
        db_exper=db_exper,
        db_hourly=db_hourly,
        db_speak=db_speak,
        db_available=db_available,
        db_bio=db_bio,
        db_price= 10,
        )

        profile_obj.save()
        #SuperUser_obj = User(db_SuperUse = username , db_email = email)
        
        # myimage = db_Image.objects.all().values()
    
        messages.success(request, 'Email Successfully Register. \n We have sent an email to you , \"Please check your mail to Verify\"')
        send_mail_after_registration(email , auth_token)
        return redirect('login_tab')

    except Exception as e:
        print(e)
 
    return HttpResponseRedirect(reverse('register'))


def verify(request , auth_token):
    try:
        profile_obj = db_Profile.objects.filter(auth_token = auth_token).first()
    

        if profile_obj:
            if profile_obj.is_verified:
                messages.success(request, 'Your account is already verified.')
                return redirect('login_tab')
            profile_obj.is_verified = True
            profile_obj.save()
            messages.success(request, 'Your account has been verified.')
            return redirect('login_tab')
        else:
            return redirect('error')
    except Exception as e:
        print(e)
        return redirect('/')

def error_page(request):
    return  render(request , 'error.html')

def send_mail_after_registration(email , token):
    subject = 'Lofin App Store : Activation Code'
    domain = settings.LOCAL_HOST_STRIPE
    message = f'Welcome to LofinApp !! \n Hi {email} \n Please confirm your email by clicking on the following link.\n \n Confirmation Link: {domain}/verify/{token}'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email]
    send_mail(subject, message , email_from , recipient_list, fail_silently = True )


def activate(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        myuser = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        myuser = None

    if myuser is not None and generate_token.check_token(myuser,token):
        myuser.is_active = True
        myuser.profile.signup_confirmation = True
        myuser.save()
        login(request, myuser)
        messages.success(request, "Your Account has been activated!!")
        return redirect('register')
    else:
        return render(request,'activation_failed.html')

