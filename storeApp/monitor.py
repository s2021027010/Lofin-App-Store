from fileinput import FileInput
from pydoc import stripid
from urllib import request
from django.http import HttpResponseRedirect
from django.urls import reverse
from storeApp.models import db_Profile, db_AppStore,db_Amount_With,Like
from django.shortcuts import redirect, render
from django.template import loader
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
# from .models import *
import uuid
from django.conf import settings
from django.contrib.auth import authenticate,login
from django.contrib.auth.decorators import login_required

from .models import *

import sys , os
from .views import *
from . import views

from .login import *
from . import login

from .signUp import *
from . import signUp

from .urls import *
from . import urls




stripid.api_key = settings.STRIPE_PRIVATE_KEY
YOUR_DOMAIN = settings.LOCAL_HOST_STRIPE

def accountManage(request):
    login.initialize()
    mypersonal = db_Profile.objects.filter(db_username = login.gb_username).values()
    myProfile = db_Profile.objects.filter(db_username = login.gb_username)

    model = db_AppStore
    myAppStore_All = model.objects.all()
    count = (model.objects.filter(db_username = login.gb_username)) and Wishlist.objects.filter(username = login.gb_username)
    myProfile_All = db_Profile.objects.all()
    wish_cart = Wishlist.objects.values_list('db_id_wishlist','username').filter(username = login.gb_username).values()
    
    template = loader.get_template('monitor/manage.html')
    context = {
        'myAppStore_All' : myAppStore_All,
        'count' : count,
        'myProfile_All' : myProfile_All,
        'wish_cart' : wish_cart,
        'myProfile': myProfile,
        'mypersonal': mypersonal,
    }
    return HttpResponse(template.render(context, request))
    # return render(request=request, template_name="home.html", context={' myprofile' : myprofile,' mypersonal' : mypersonal,'myimage': myimage,})

def setting(request):
    login.initialize()
    mypersonal = db_Profile.objects.filter(db_username = login.gb_username).values()
    myProfile = db_Profile.objects.filter(db_username = login.gb_username)

    model = db_AppStore
    myAppStore_All = model.objects.all()
    count = (model.objects.filter(db_username = login.gb_username)) and Wishlist.objects.filter(username = login.gb_username)
    myProfile_All = db_Profile.objects.all()
    wish_cart = Wishlist.objects.values_list('db_id_wishlist','username').filter(username = login.gb_username).values()
    
    template = loader.get_template('monitor/setting.html')
    context = {
        'myAppStore_All' : myAppStore_All,
        'count' : count,
        'myProfile' : myProfile,
        'myProfile_All' : myProfile_All,
        'wish_cart' : wish_cart,
        'mypersonal': mypersonal,
    }
    return HttpResponse(template.render(context, request))


def change_Email(request, id):  
    if request.method == "POST":  
        input_username = request.POST['input_username']
        input_email = request.POST['input_email']
        input_password = request.POST['input_password']

        profile_obj = db_Profile.objects.get(id = id)
        user_obj = User.objects.filter(username = input_username).first()
        user = authenticate(username = input_username , password = input_password)
        if user_obj is not None:
            myuser = db_Profile.objects.get(db_username = input_username)
        
        if user_obj is None:
            messages.error(request, 'User not found.')
            return redirect('setting')
        elif user is None:
            messages.error(request, 'Invalid password.')
            return redirect('setting')
        else:
            try:
                if User.objects.filter(email = input_email).first():
                    messages.error(request, 'Email is already Taken.') 
                    return redirect('setting')  
                else:
                    auth_token1 = str(uuid.uuid4())
                    auth_token = auth_token1
                    #auth_token = profile_obj.auth_token

                    profile_obj.db_email = input_email
                    profile_obj.auth_token = auth_token
                    profile_obj.is_verified = False
                    user_obj.email = input_email
                    myuser.auth_token = auth_token
                    myuser.is_verified = False
                    myuser.db_email = input_email

                    profile_obj.save()
                    myuser.save()
                    user_obj.save()

                    messages.success(request, 'Email Successfully Save Changed.')
                    send_mail_after_registration(input_email , auth_token)
                    return redirect('login_tab')


            except Exception as e:
                print(e)
 
    return redirect('setting')

from django.core.mail import EmailMessage, send_mail

def send_mail_after_registration(email , token):
    subject = 'Lofin App Store : Email Change Code'
    domain = settings.LOCAL_HOST_STRIPE
    message = f'Welcome to LofinApp !! \n Hi {email} \n Please confirm your email by clicking on the following link.\n \n Confirmation Link: {domain}/verify/{token}'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email]
    send_mail(subject, message , email_from , recipient_list, fail_silently = True )


def change_Password(request, id):  
    if request.method == "POST":  
        input_username = request.POST['input_username']
        input_Oldpassword = request.POST['input_password']
        input_NewPassword = request.POST['input_NewPassword']
        input_ConfirmPassword = request.POST['input_ConfirmPassword']

        profile_obj = db_Profile.objects.get(id = id)
        user_obj = User.objects.filter(username = input_username).first()
        user = authenticate(username = input_username , password = input_Oldpassword)
        if user_obj is not None:
            myuser = db_Profile.objects.get(db_username = input_username)
        
        if user_obj is None:
            messages.error(request, 'User not found.')
            return redirect('setting')
        elif user is None:
            messages.error(request, 'Invalid password.')
            return redirect('setting')
        elif input_NewPassword != input_ConfirmPassword:
            messages.error(request, "Password didn't Match.")
            return redirect('setting')
        else:
            try:
                user_obj.set_password(input_NewPassword)
                user_obj.save()

                messages.success(request, 'Password Successfully Save Changed.')
                return redirect('login_tab')


            except Exception as e:
                print(e)
 
    return redirect('setting')


    return redirect('status')
def status(request):
    login.initialize()
    myProfile = db_Profile.objects.filter(db_username = login.gb_username).values()
    myAppStore = db_AppStore.objects.filter(db_username = login.gb_username)
    myAmount_filter = db_Amount_With.objects.filter(db_username_PaidBy = login.gb_username).values()
    myAmount = db_Amount_With.objects.filter(db_username_Publisher = login.gb_username).values()
    myLike = db_AppStore.objects.values_list('db_like').filter(db_username = login.gb_username)
    myComment = db_AppStore.objects.values_list('db_comment').filter(db_username = login.gb_username)


    model = db_AppStore
    myAppStore_All = model.objects.all()
    count = (model.objects.filter(db_username = login.gb_username)) and Wishlist.objects.filter(username = login.gb_username)
    myProfile_All = db_Profile.objects.all()
    wish_cart = Wishlist.objects.values_list('db_id_wishlist','username').filter(username = login.gb_username).values()
    
    price = Withdrawal.objects.filter(db_username_Pub= login.gb_username).values()
    Transuct = Transuction.objects.filter(username_trans= login.gb_username).values()
    
    template = loader.get_template('monitor/status.html')
    context = {
        
            'myAppStore_All' : myAppStore_All,
            'count' : count,
            'myProfile_All' : myProfile_All,
            'wish_cart' : wish_cart,
            'myProfile': myProfile,
            'myAmount' : myAmount,
            'myAmount_filter': myAmount_filter,
            'myAppStore': myAppStore,
            'price' : price,
            'myLike' : myLike,
            'myComment' : myComment,
            'Transuct' : Transuct,
            }
    return HttpResponse(template.render(context, request))
    # return render(request=request, template_name="home.html", context={' myprofile' : myprofile,' mypersonal' : mypersonal,'myimage': myimage,})



def transfer(request):
    login.initialize()
    if request.method == "POST":  
        var_amount = request.POST['input_amount']
        var_currency = request.POST['input_currency']
        payout = Transuction()
        amount = Withdrawal.objects.get(db_username_Pub = login.gb_username)
        price = amount.db_price
        if int(var_amount) >= price:
            messages.error(request,'Please Enter only Earning Amount (limit exceeded)')
        elif price <1 :
            messages.error(request,'You have insufficient Balance')
        else:
            amount.db_price = int(price) - int(var_amount)
            payout.username_trans = login.gb_username
            payout.price = var_amount
            payout.type = var_currency
            payout.save()
            amount.save()
            return redirect('status')
        return redirect('status')
    return redirect('status')
    '''
    transfer = stripe.Transfer.create(
        amount= 1000,
        currency='usd',
        destination= "tgjhrwwk_23y4dns",
    )
    print(transfer)
    
    return JsonResponse({'transfer': transfer})
    '''

import stripe
from django.http import JsonResponse,HttpResponse
from django.views.decorators.csrf import csrf_exempt
stripe.api_key = settings.STRIPE_PRIVATE_KEY
YOUR_DOMAIN = settings.LOCAL_HOST_STRIPE
def create(request):
    if request.method == "POST":
        var_type = request.POST['input_type']
        var_country =  request.POST['input_country']
        var_email =  request.POST['input_email']

        account =  stripe.Account.create(
        type= var_type,
        country= var_country,
        email= var_email,
        capabilities={
            "card_payments": {"requested": True},
            "transfers": {"requested": True},
        },
        )
        login.initialize()
        profile_obj = db_Profile.objects.get(db_username = login.gb_username)
        profile_obj.is_account = True
        profile_obj.save()
        return redirect('publish')
    else:
        return redirect('accountManage')
    return redirect('/')
