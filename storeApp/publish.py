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
# from .models import *
import datetime
import uuid
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required


import stripe
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from tokenize import maybe
from venv import create
from django.http import HttpResponseRedirect
from storeApp.models import db_Profile, db_AppStore, Like
from django.template import loader
from django.contrib.auth.models import User

from .models import *

from LofinApp_Project import settings

from django.http import HttpResponse
from django.core.mail import EmailMessage, send_mail
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes, force_str
from django.contrib.auth import authenticate, login, logout
from . tokens import generate_token


from .monitor import *
from . import monitor
from django.views import View
from django.urls import reverse_lazy

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



def publish(request):
    login.initialize()
    myAppStore = db_AppStore.objects.filter(db_username = login.gb_username)
    myProfile = db_Profile.objects.filter(db_username = login.gb_username)
    
    model = db_AppStore
    myAppStore_All = model.objects.all()
    count = (model.objects.filter(db_username = login.gb_username)) and Wishlist.objects.filter(username = login.gb_username)
    myProfile_All = db_Profile.objects.all()
    wish_cart = Wishlist.objects.values_list('db_id_wishlist','username').filter(username = login.gb_username).values()
    
    template = loader.get_template('monitor/publish.html')
    context = {
        'myAppStore_All' : myAppStore_All,
        'count' : count,
        'myProfile_All' : myProfile_All,
        'wish_cart' : wish_cart,
        'myAppStore': myAppStore,
        'myProfile' : myProfile,
    }
    
    return HttpResponse(template.render(context, request))
    # return render(request=request, template_name="home.html", context={' myprofile' : myprofile,' mypersonal' : mypersonal,'myimage': myimage,})

#-----------------------Create Check Out------------------------------------------------------------------------------------------


stripe.api_key = settings.STRIPE_PRIVATE_KEY
YOUR_DOMAIN = 'http://127.0.0.1:8000'

@csrf_exempt
def create_session_out(request,Username,price):
    price=price*100
    session = stripe.checkout.Session.create(
    payment_method_types=['card'],
    line_items=[{
            'price_data': {
            'currency': 'usd',
            'product_data': {
            'name': Username,
            },
            'unit_amount': price,
            },
            'quantity': 1,
    }],
    mode='payment',
    success_url=YOUR_DOMAIN + '/success.html',
    cancel_url=YOUR_DOMAIN + '/cancel.html',
    )
    return JsonResponse({'id': session.id})

'''#home view
def homeOut(request):
    return render(request,'checkout.html')
'''
#success view
def success(request):
    messages.success(request, 'Payment Successfully ')
    profile_obj = db_Profile.objects.filter(db_username = login.gb_username).first()
    login.initialize()
    if not profile_obj.SuperUser_is_verified:
        if profile_obj.SuperUser_is_verified:
                    messages.success(request, 'Your account is already verified.')
                    return redirect('publish')
        elif not profile_obj.SuperUser_is_verified:
                    profile_obj.SuperUser_is_verified = True
                    profile_obj.save()
                    messages.success(request, 'Your account has been verified.')
                    return redirect('publish')
        else:
            messages.success(request, 'Accure Error.')
            return redirect('publish')
    else:
        return redirect('publish')
    return render(request,'fullView.html')

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







def add_AppStore(request):
    if request.method == "POST":
        '''
        db_username = request.POST['username']
        db_photoApp = request.POST['input_imageApp']
        db_AppName = request.POST['input_AppName']
        db_price = request.POST['input_priceApp']
        db_type = request.POST['input_type']
        db_link_type  = request.POST['input_type_type']
        db_Category = request.POST['input_Category']
        db_describe = request.POST['input_describe']
        db_link = request.POST['input_link'],
        db_country = request.POST['input_country']
        db_create_Date = request.POST['input_date_Create']

        
        
 

        nowTime = datetime.datetime.now()
        year = nowTime.year
        month = nowTime.month
        day = nowTime.day

        '''
        db_username = request.POST['username']
        price = int(request.POST['input_price'])
        myAppStore = db_AppStore()

        myAppStore.db_username = request.POST.get('username')
        if len(request.FILES) !=0:
            myAppStore.db_photoApp = request.FILES['input_imageApp']

            myAppStore.db_images_list1 = request.FILES['input_images1']
            myAppStore.db_images_list2 = request.FILES['input_images2']
            myAppStore.db_images_list3 = request.FILES['input_images3']
            myAppStore.db_images_list4 = request.FILES['input_images4']
            # myAppStore.objects.create(db_images_list=db_images)
        
        myAppStore.db_AppName  = request.POST.get('input_AppName').capitalize()
        myAppStore.db_price = request.POST.get('input_price')

        myAppStore.db_type = request.POST.get('input_type')
        myAppStore.db_link_type = request.POST.get('input_link_type')
        myAppStore.db_Category = request.POST.get('input_Category')
        myAppStore.db_Describe = request.POST.get('input_describe')
        if len(request.FILES) !=0:
            myAppStore.db_link = request.FILES['input_link']
        
        # myAppStore.db_create_Date = ['%year %month %day']
        myAppStore.db_country = request.POST.get('input_country')
        
        myAppStore.save()
        messages.success(request, 'App Successfully Public')
    return HttpResponseRedirect(reverse('publish'))