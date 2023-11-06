from fileinput import FileInput
from tokenize import maybe
from typing import Counter
from urllib import request
from venv import create
from django.http import HttpResponseRedirect
from django.urls import reverse
from storeApp.models import db_Profile, db_AppStore, Like ,db_Amount_With
from django.shortcuts import redirect, render, get_object_or_404
from django.template import loader
from django.contrib.auth.models import User
from django.contrib import messages
from .models import *
import uuid
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth import authenticate,login
from django.contrib.auth.decorators import login_required
from LofinApp_Project import settings

import stripe
from django.http import JsonResponse,HttpResponse
from django.views.decorators.csrf import csrf_exempt

from django.http import HttpResponse
from django.core.mail import EmailMessage, send_mail
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes, force_str
from django.contrib.auth import authenticate, login, logout
from . tokens import generate_token


import sys , os
from .views import *
from . import views

from .login import *
from . import login

from .publish import *
from . import publish

from .signUp import *
from . import signUp

from .urls import *
from . import urls

from .monitor import *
from . import monitor
from django.views import View
from django.urls import reverse_lazy
# from django.views.decorators.csrf import csrf_exempt
# @csrf_exempt

@login_required
def home(request):
    model = db_AppStore
    login.initialize()
    
    myProfile = db_Profile.objects.filter(db_username = login.gb_username).values()
    myAppStore_All = model.objects.all()
    count = (model.objects.filter(db_username = login.gb_username)) and Wishlist.objects.filter(username = login.gb_username).all()
    myProfile_All = db_Profile.objects.all()
    wish_cart = Wishlist.objects.values_list('db_id_wishlist','username').filter(username = login.gb_username).values()
    
    

    template = loader.get_template('home.html')
    
    context = {
        'myAppStore_All': myAppStore_All,
        'myProfile': myProfile,

        'myProfile_All': myProfile_All,
        'count' : count,
        'wish_cart' : wish_cart,
    }
    return HttpResponse(template.render(context, request))


@login_required
def like(request):
    if request.method == 'POST':
        post_id = request.POST.get('post_id')
        post_obj = db_AppStore.objects.get(db_id_App = post_id)
        post_id = request.POST['post_id']
        post_username = request.POST['post_username']
        post_AppName = request.POST['post_AppName']
        user = get_object_or_404(User, username = post_username)

        db_Like = Like(username = post_username, AppStore = post_AppName, db_id_Like = post_id)
        
        
        if Like.objects.filter(db_id_Like = request.POST['post_id'], username = request.POST['post_username']).exists() == True:
            db_Like_Del = Like.objects.get(db_id_Like = post_id, username = post_username)
            db_Like_Del.delete()
            post_obj.db_like.remove(user)
        else:
            db_Like.value = 'Like'
            post_obj.db_like.add(user)
            db_Like.save()
        id= post_id
        local = settings.LOCAL_HOST_STRIPE

    return redirect(local + '/fullView/' + str(id))



def wishlist(request):
    if request.method == 'POST':
        post_id = request.POST.get('post_id')
        post_obj = db_AppStore.objects.get(db_id_App = post_id)
        post_id = request.POST['post_id']
        post_username = request.POST['post_username']
        post_AppName = request.POST['post_AppName']
        post_type = request.POST['post_type']
        post_Category = request.POST['post_Category']
        user = get_object_or_404(User, username = post_username)

        db_Wish = Wishlist(username = post_username, AppStore = post_AppName, db_id_wishlist = post_id, type_wish = post_type , Category_wish = post_Category)
        
        
        if Wishlist.objects.filter(db_id_wishlist = request.POST['post_id'], username = request.POST['post_username']).exists() == True:
            db_Wish_Del = Wishlist.objects.get(db_id_wishlist = post_id, username = post_username)
            db_Wish_Del.delete()
            post_obj.db_wishlist.remove(user)
        else:
            db_Wish.value_wish = 'Wish'
            db_Wish.type_wish = post_type
            db_Wish.Category_wish = post_Category
            post_obj.db_wishlist.add(user)
            db_Wish.save()

    return redirect('home')




@login_required
def gamePage(request):
    model = db_AppStore
    login.initialize()
    myProfile = db_Profile.objects.filter(db_username = login.gb_username).values()
    myAppStore_Car = db_AppStore.objects.filter(db_Category ='Game')
    myAppStore_Race = db_AppStore.objects.filter(db_type ='Race')
    
    myAppStore_All = model.objects.all()
    count = (model.objects.filter(db_username = login.gb_username)) and Wishlist.objects.filter(username = login.gb_username)
    myProfile_All = db_Profile.objects.all()
    wish_cart = Wishlist.objects.values_list('db_id_wishlist','username').filter(username = login.gb_username).values()
    
   
    template = loader.get_template('main/game.html')
    context = {
        'myAppStore_All' : myAppStore_All,
        'count' : count,
        'myProfile_All' : myProfile_All,
        'wish_cart' : wish_cart,
        'myProfile' : myProfile,
        'myAppStore_Car': myAppStore_Car,
        'myAppStore_Race': myAppStore_Race,
    }
    return HttpResponse(template.render(context, request))

@login_required
def socialPage(request):
    model = db_AppStore
    login.initialize()
    myProfile = db_Profile.objects.filter(db_username = login.gb_username).values()
    myAppStore_Social = db_AppStore.objects.filter(db_Category ='Social')
    myAppStore_Chat = db_AppStore.objects.filter(db_type ='Chat')
    
    myAppStore_All = model.objects.all()
    count = (model.objects.filter(db_username = login.gb_username)) and Wishlist.objects.filter(username = login.gb_username)
    myProfile_All = db_Profile.objects.all()
    wish_cart = Wishlist.objects.values_list('db_id_wishlist','username').filter(username = login.gb_username).values()
    
   
    template = loader.get_template('main/social.html')
    context = {
        'myAppStore_All' : myAppStore_All,
        'count' : count,
        'myProfile_All' : myProfile_All,
        'wish_cart' : wish_cart,
        'myProfile' : myProfile,
        'myAppStore_Social': myAppStore_Social,
        'myAppStore_Chat': myAppStore_Chat,
    }
    return HttpResponse(template.render(context, request))

@login_required
def sportPage(request):
    model = db_AppStore
    login.initialize()
    myProfile = db_Profile.objects.filter(db_username = login.gb_username).values()
    myAppStore_sport = db_AppStore.objects.filter(db_Category ='Sport')
    myAppStore_match = db_AppStore.objects.filter(db_type ='Match')
    
    myAppStore_All = model.objects.all()
    count = (model.objects.filter(db_username = login.gb_username)) and Wishlist.objects.filter(username = login.gb_username)
    myProfile_All = db_Profile.objects.all()
    wish_cart = Wishlist.objects.values_list('db_id_wishlist','username').filter(username = login.gb_username).values()
    
   
    template = loader.get_template('main/sport.html')
    context = {
        'myAppStore_All' : myAppStore_All,
        'count' : count,
        'myProfile_All' : myProfile_All,
        'wish_cart' : wish_cart,
        'myProfile' : myProfile,
        'myAppStore_sport': myAppStore_sport,
        'myAppStore_match': myAppStore_match,
    }
    return HttpResponse(template.render(context, request))

@login_required
def topPage(request):
    model = db_AppStore
    
    login.initialize()
    myProfile = db_Profile.objects.filter(db_username = login.gb_username).values()
    
    # myAppStore_top_like = db_AppStore.objects.filter(db_like = 3)
    myAppStore_top_like = db_AppStore.objects.filter(db_like = 3).order_by('-db_like','db_AppName','db_id_App','db_username').reverse()[:10]
    myAppStore_top = db_AppStore.objects.filter(db_type ='Top')
    
    myAppStore_All = model.objects.all()
    count = (model.objects.filter(db_username = login.gb_username)) and Wishlist.objects.filter(username = login.gb_username)
    myProfile_All = db_Profile.objects.all()
    wish_cart = Wishlist.objects.values_list('db_id_wishlist','username').filter(username = login.gb_username).values()
    
   

    template = loader.get_template('main/top.html')
    context = {
        'myAppStore_All' : myAppStore_All,
        'count' : count,
        'myProfile_All' : myProfile_All,
        'wish_cart' : wish_cart,
        'myProfile' : myProfile,
        'myAppStore_top_like': myAppStore_top_like,
        'myAppStore_top': myAppStore_top,
    }
    return HttpResponse(template.render(context, request))


@login_required
def logout(request):
    request.session.clear()
    return redirect('login_tab') 

#_________________________________________________________________________________________-_--

def layout_account_header(request):
    return render(request=request, template_name="layout-account/header.html")


def layout_account_footer(request):
    return render(request=request, template_name="layout-account/footer.html")



def layout_main_header(request):
    login.initialize()
    model = db_AppStore
    myUserShow = db_Profile.objects.filter(db_username = login.gb_username)
    myAppWish = model.objects.all()

    template = loader.get_template('layout-main/header.html')
    context={ 
        'myUserShow': myUserShow,
        'myAppWish' : myAppWish,
    }
    return HttpResponse(template.render(context, request))

def layout_main_footer(request):
    
    template = loader.get_template('layout-main/footer.html')
    
    
    return HttpResponse(template.render({}, request))



#__________________________________________________________________________________________--

@login_required
def search(request):
    
    search = request.GET['search']
    myAppStore_search = db_AppStore.objects.filter(db_AppName__contains = search.capitalize()) | db_AppStore.objects.filter(db_Category__contains = search.capitalize() ).values() | db_AppStore.objects.filter(db_type__contains = search.capitalize() ).values() | db_AppStore.objects.filter(db_country__contains = search.capitalize() ).values()  | db_AppStore.objects.filter(db_Describe__contains = search.capitalize() ).values() 

    template = loader.get_template('main/search.html')
    context = {
    'myAppStore_search': myAppStore_search,
    }
    # global gb_title
    # gb_title = 'search'
    return HttpResponse(template.render(context, request))




# ------------------------------------------------------------------------------------------------------


def comment(request):
    if request.method == 'POST':
        post_id = request.POST.get('post_id')
        post_obj = db_AppStore.objects.get(db_id_App = post_id)
        post_id = request.POST['post_id']
        post_username = request.POST['post_username']
        post_AppName = request.POST['post_AppName']
        post_type = request.POST['post_type']
        post_Category = request.POST['post_Category']
        post_Subject =  request.POST['post_Subject']
        post_Text_comment =  request.POST['post_Text_comment']
        user = get_object_or_404(User, username = post_username)

        db_Comm = Comment(username = post_username, AppStore = post_AppName, db_id_comment = post_id, type_comment = post_type , Category_comment = post_Category, subject_comment = post_Subject, text_comment = post_Text_comment)
        
        
        if Comment.objects.filter(db_id_comment = request.POST['post_id'], username = request.POST['post_username']).exists() == True:
        
            db_Comm.value_comment = 'Comment'
            db_Comm.type_comment = post_type
            db_Comm.Category_comment = post_Category
            db_Comm.subject_comment = post_Subject
            db_Comm.text_comment = post_Text_comment

            post_obj.db_comment.add(user)
            db_Comm.save()
        else:
            db_Comm.value_comment = 'Comment'
            db_Comm.type_comment = post_type
            db_Comm.Category_comment = post_Category
            db_Comm.subject_comment = post_Subject
            db_Comm.text_comment = post_Text_comment

            post_obj.db_comment.add(user)
            db_Comm.save()

    return redirect('fullView', id = post_id)



def fullView(request, id):
    model = db_AppStore
    
    login.initialize()
    
    myAppStore = model.objects.all()
    myProfile = db_Profile.objects.filter(db_username = login.gb_username).values()
    myAppStore_All = model.objects.filter(db_id_App = id).values()
    count = (model.objects.filter(db_username = login.gb_username)) and Wishlist.objects.filter(username = login.gb_username)
    myProfile_All = db_Profile.objects.all()
    count_comment = (model.objects.filter(db_id_App = id) and Comment.objects.filter(db_id_comment = id))
    # myAppStore_All = model.objects.all()
    myComment_All = Comment.objects.all()
    wish_cart = Wishlist.objects.values_list('db_id_wishlist','username').filter(username = login.gb_username).values()
    comment_send = Comment.objects.values_list('db_id_comment','username').filter(db_id_comment = id).values()
    
    if not db_Amount_With.objects.values_list('db_id_App','db_username_PaidBy').filter(db_username_PaidBy = login.gb_username, db_id_App = id):
        check = False
        print(check)
    else :
        check = True
        print(check)

    # template = loader.get_template('main/fullView.html')
    template = loader.get_template('main/fullView.html')
    context = {
                'myAppStore_All': myAppStore_All,
                'myProfile': myProfile,

                'myProfile_All': myProfile_All,
                'myComment_All': myComment_All,
                'myAppStore': myAppStore,
                'comment_send': comment_send,
                'count' : count,
                'count_comment': count_comment,
                'wish_cart' : wish_cart,
                'check' : check,
                # 'myAmount' : myAmount,
    }

    return HttpResponse(template.render(context, request))
    # return render(request=request, template_name="home.html", context={' myprofile' : myprofile,' mypersonal' : mypersonal,'myimage': myimage,})




#-----------------------Create Check Out------------------------------------------------------------------------------------------


stripe.api_key = settings.STRIPE_PRIVATE_KEY
YOUR_DOMAIN = settings.LOCAL_HOST_STRIPE

@csrf_exempt
def create_session_checkout(request,id,name,price):

    price=price*100
    session = stripe.checkout.Session.create(
    payment_method_types=['card'],
    line_items=[{
            'price_data': {
            'currency': 'usd',
            'product_data': {
            'name': name,
            },
            'unit_amount': price,
            },
            'quantity': 1,
    }],
    mode='payment',
    #success_url=YOUR_DOMAIN + '/fullView/' + str(id),
    success_url = YOUR_DOMAIN + '/success.html/' + str(id),
    cancel_url=YOUR_DOMAIN + '/cancel.html',
    )
    return JsonResponse({'id': session.id})

'''#home view
def homeOut(request):
    return render(request,'checkout.html')
'''
#success view
def success(request,id):
    login.initialize()
    myAmount = db_Amount_With()
    
    myAppStore = db_AppStore.objects.get(db_id_App = id)

    db_id_Ap = myAppStore.db_id_App
    username_PaidBy = login.gb_username
    username_Publisher =  myAppStore.db_username
    input_AppName = myAppStore.db_AppName
    input_price = myAppStore.db_price
    input_type = myAppStore.db_type
    input_is_paid = True
    print(input_price)
    user = get_object_or_404(User, username = username_PaidBy)
    # myAmount.save()
    # Withdrawal.objects.get(db_username_Publisher = login.gb_username)
    myWithdrawal = Withdrawal()
    
    if Withdrawal.objects.filter(db_username_Pub = username_Publisher).exists() == True:
        id_get = Withdrawal.objects.get(db_username_Pub = username_Publisher)
        # var_id = id_get.id
        var_price = id_get.db_price
        update_Withd = Withdrawal.objects.get(db_username_Pub = username_Publisher)
        update_Withd.db_username_Publisher = username_Publisher
        update_Withd.db_username_Pub = username_Publisher
        per_price = (input_price * (0.8))
        update_Withd.db_price = int(per_price) + int(var_price)
        update_Withd.save()
    else:
        myWithdrawal.db_username_Publisher = username_Publisher
        myWithdrawal.db_username_Pub = username_Publisher
        per_price = (input_price * (0.8))
        myWithdrawal.db_price = per_price
        myWithdrawal.save()   
        
    if db_Amount_With.objects.filter(db_username_PaidBy = login.gb_username).exists() == True:
        
        myAmount.db_id_App = db_id_Ap
        myAmount.db_username_PaidBy = username_PaidBy
        myAmount.db_username_Publisher =  username_Publisher
        myAmount.db_AppName = input_AppName
        myAmount.db_price = input_price
        myAmount.db_type = input_type 
        myAmount.is_paid = True

        myAppStore.db_paid.add(user)
        myAmount.save()
    else:
        
        myAmount.db_id_App = db_id_Ap
        myAmount.db_username_PaidBy = username_PaidBy
        myAmount.db_username_Publisher =  username_Publisher
        myAmount.db_AppName = input_AppName
        myAmount.db_price = input_price
        myAmount.db_type = input_type 
        myAmount.is_paid = True

        myAppStore.db_paid.add(user)
        myAmount.save()
    

    
    return redirect('/fullView/'+ str(id))



 #cancel view
def cancel(request):
    return render(request,'cancel.html')


endpoint_secret = settings.STRIPE_PRIVATE_KEY
@csrf_exempt
def webhook(request):
    
    endpoint_secret = ''
    payload = request.body
    sig_header = request.META['HTTP_STRIPE_SIGNATURE']
    event = None

    try:
        event = stripe.Webhook.construct_event(
    payload, sig_header, endpoint_secret
    )
    except ValueError as e:
 # Invalid payload
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError as e:
 # Invalid signature
        return HttpResponse(status=400)

 # Handle the checkout.session.completed event
    if event['type'] == 'checkout.session.completed':
        print("Payment was successful.")
 # TODO: run some custom code here

    return HttpResponse(status=200)
#-----------------------------------------------------------------------------------------------------------------





def wishlistView(request):
    model = db_AppStore
    login.initialize()
    
    myProfile = db_Profile.objects.filter(db_username = login.gb_username).values()
    myAppStore_All = model.objects.all()
    count = (model.objects.filter(db_username = login.gb_username)) and Wishlist.objects.filter(username = login.gb_username)
    myProfile_All = db_Profile.objects.all()
    wish_cart = Wishlist.objects.values_list('db_id_wishlist','username').filter(username = login.gb_username).values()
    
    

    template = loader.get_template('layout-main/wishlistView.html')
    
    context = {
        'myAppStore_All': myAppStore_All,
        'myProfile': myProfile,

        'myProfile_All': myProfile_All,
        'count' : count,
        'wish_cart' : wish_cart,
    }
    return HttpResponse(template.render(context, request))