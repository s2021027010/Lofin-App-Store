from fileinput import FileInput
from urllib import request
from django.http import HttpResponseRedirect
from django.urls import reverse
from storeApp.models import db_Profile, db_AppStore,db_Amount_With
from django.shortcuts import redirect, render
from django.template import loader
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from .models import *
import uuid
from django.conf import settings
from django.contrib.auth import authenticate,login
from django.contrib.auth.decorators import login_required

from .views import *
from . import views

from .login import *
from . import login



from .signUp import *
from . import signUp

from .urls import *
from . import urls

from .monitor import *
from . import monitor

# Create your views here.


def profile(request):
    login.initialize()
    myAppStore = db_AppStore.objects.filter(db_username = login.gb_username).values()
    myProfile = db_Profile.objects.filter(db_username =  login.gb_username).values()

    model = db_AppStore
    myAppStore_All = model.objects.all()
    count = (model.objects.filter(db_username = login.gb_username)) and Wishlist.objects.filter(username = login.gb_username)
    myProfile_All = db_Profile.objects.all()
    wish_cart = Wishlist.objects.values_list('db_id_wishlist','username').filter(username = login.gb_username).values()
    

    template = loader.get_template('monitor/profile.html')
    context={ 
        'myAppStore_All' : myAppStore_All,
        'count' : count,
        'myProfile_All' : myProfile_All,
        'wish_cart' : wish_cart,
        'myProfile': myProfile,
        'myAppStore': myAppStore,
    }
    return HttpResponse(template.render(context, request))
    #return render(request, "monitor/profile.html")
    

def update_Profile(request, id):
    db_username=request.POST['username']
    db_email = request.POST['email']
    db_photo = request.POST['input_imageP']
    db_firstName = request.POST['input_firstName']
    db_lastName= request.POST['input_lastName']
    db_phoneNumber = request.POST['input_phoneNumber']
    db_address = request.POST['input_address']
    db_date_DoB = request.POST['input_date_DoB']
    db_exper = request.POST['input_exper']
    db_hourly = request.POST['input_hourly']
    # db_Tproject = request.POST['input_Tproject']
    db_speak = request.POST['input_speak']
    db_available = request.POST['input_available']
    db_bio = request.POST['input_bio']

    mypersonalUpdate = db_Profile.objects.get(id=id)
    mypersonalUpdate.db_username = db_username
    mypersonalUpdate.db_email = db_email
    if len(request.FILES) !=0:
        mypersonalUpdate.db_photo =  request.FILES['input_imageP']
    
    mypersonalUpdate.db_firstName = db_firstName
    mypersonalUpdate.db_lastName = db_lastName
    mypersonalUpdate.db_phoneNumber = db_phoneNumber
    mypersonalUpdate.db_address = db_address
    # mypersonalUpdate.db_date_DoB = db_date_DoB
    mypersonalUpdate.db_exper = db_exper
    mypersonalUpdate.db_hourly = db_hourly
    # mypersonalUpdate.db_Tproject = db_Tproject
    mypersonalUpdate.db_speak = db_speak
    mypersonalUpdate.db_available = db_available
    mypersonalUpdate.db_bio = db_bio

    mypersonalUpdate.save()
    if len(db_phoneNumber) >= 13:
        messages.error(request,"Phone number Must be under 13 Digits.")
        return redirect('profile')
    else:
        messages.error(request, 'Profile Successfully Updated')
        return redirect('profile')

    return HttpResponseRedirect(reverse('profile'))

