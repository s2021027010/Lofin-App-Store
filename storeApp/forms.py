from dataclasses import fields
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import  db_Profile , db_AppStore

from .models import *


class db_Personal_Form(ModelForm):
    class Meta:
        model = db_Profile
        fields = ('user', 'db_username' , 'db_email' , 'db_photo' , 'db_firstName' , 'db_lastName' ,
         'db_phoneNumber' , 'db_address' , 'db_date_DoB' , 'db_date_DoB' , 'db_exper' ,
          'db_hourly' , 'db_speak' , 'db_available' , 'db_bio', 'auth_token', 'is_verified', 'created_at')

class db_AppStore_Form(UserCreationForm):
    class Meta:
        model = db_AppStore
        fields = ('db_id_App', 'db_username', 'db_AppName', 'db_Category', 'db_type', 'db_Describe',
            'db_like', 'db_wishlist', 'db_comment', 'db_link', 'db_photoApp', 'db_images_list1',
            'db_images_list2', 'db_images_list3', 'db_images_list4', 'db_create_Date', 'db_country')