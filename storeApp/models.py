from asyncio.windows_events import NULL
from email.policy import default
from enum import auto
from datetime import datetime, time, date
from random import choices
from django.db import models
from django.contrib.auth.models import User


class db_Profile(models.Model):
    user = models.OneToOneField(User , on_delete=models.CASCADE)
    db_username = models.CharField(max_length=255)
    db_email = models.EmailField(max_length=255)
    db_photo = models.ImageField(upload_to = "media/Profile/", width_field=None, height_field=None, max_length=255, blank=True)
    db_firstName = models.CharField(max_length=255)
    db_lastName = models.CharField(max_length=255)
    db_phoneNumber = models.CharField(max_length=255)
    db_address = models.CharField(max_length=255)
    db_date_DoB = models.DateField(auto_now_add=False, auto_now=False, blank=True)
    db_exper = models.CharField(max_length=255)
    db_hourly = models.CharField(max_length=255)
    db_speak = models.CharField(max_length=255)
    db_available = models.CharField(max_length=255)
    db_bio = models.TextField(max_length=1000)
    auth_token = models.CharField(max_length=100 )
    created_at = models.DateTimeField(auto_now_add=True)
    
    is_account = models.BooleanField(default=False)
    is_verified = models.BooleanField(default=False)
    db_price = models.IntegerField()
    SuperUser_is_verified = models.BooleanField(default=False)
  
    

    def __str__(self):
        return self.user.username
    @property
    def total_price(self):
        return self.db_price.all().count()
    def get_user_by_email(username):
        try:
            return db_Profile.objects.get(user=username)
        except:
            return False

    def isExists(self):
        if db_Profile.objects.filter(username=self.user):
            return True

        return False




#-----------------------------------------------   APP Store  -------------------------------------------------------------------#


class db_AppStore(models.Model):
    db_id_App = models.AutoField(primary_key=True)
    db_username = models.CharField(max_length=255,)
    db_AppName = models.CharField(max_length=255,)
    db_Category = models.CharField(max_length=255,)
    db_type = models.CharField(max_length=255,)
    db_link_type = models.CharField(max_length=255,)
    db_price = models.IntegerField()
    db_paid = models.ManyToManyField(User, related_name='db_paid')
    db_Describe = models.TextField(max_length=1000,)
    db_like = models.ManyToManyField(User, related_name='db_like')
    db_wishlist = models.ManyToManyField(User, related_name='db_wishlist')
    db_comment = models.ManyToManyField(User, related_name='db_comment')
    db_link = models.FileField(upload_to="media/AppsFile/", max_length=500)
    db_photoApp = models.ImageField(upload_to="media/AppsImage/", width_field=None, height_field=None, max_length=255, blank=True)
    db_images_list1 = models.FileField(upload_to="media/ImageList/", blank=True)
    db_images_list2 = models.FileField(upload_to="media/ImageList/", blank=True)
    db_images_list3 = models.FileField(upload_to="media/ImageList/", blank=True)
    db_images_list4 = models.FileField(upload_to="media/ImageList/", blank=True)
    db_create_Date = models.DateField(auto_now_add=True, auto_now=False)
    db_country = models.CharField(max_length=255)
    

    def __str__(self):
        return (self.db_AppName)
    
    @property
    def total_price(self):
        return sum[(self.db_price)]
    @property
    def total_likes(self):
        return self.db_like.all().count()
    @property
    def total_wishlist(self):
        return self.db_wishlist.all().count()
    
    @property
    def total_comment(self):
        return self.db_comment.all().count()

    def get_user_by_email(appname):
        try:
            return db_AppStore.objects.get(db_AppName=appname)
        except:
            return False

    def isExists(self):
        if db_AppStore.objects.filter(appname=self.db_AppName):
            return True

        return False

class db_Amount_With(models.Model):
    db_id_App = models.CharField(max_length=255)
    db_username_Publisher = models.CharField(max_length=255,)
    db_username_PaidBy = models.CharField(max_length=255,)
    db_AppName = models.CharField(max_length=255,)
    db_price = models.IntegerField()
    db_type = models.CharField(max_length=255,)
    is_paid = models.BooleanField(default=False)

    def __str__(self):
        return (self.db_AppName) + ":" + (self.db_username_PaidBy)

    def isExists(self):
        if db_Amount_With.objects.filter(db_username_PaidBy = self.db_username_PaidBy, db_id_App = self.db_id_App ) :
            return True

        return False

class Withdrawal(models.Model):
    db_username_Publisher = models.ManyToOneRel(db_AppStore ,'db_username',"db_username_Publisher", on_delete=models.CASCADE)
    db_username_Pub = models.CharField(max_length=255,)
    db_price = models.IntegerField()
    def __str__(self):
        return (self.db_username_Pub)
    def isExists(self):
        if db_Amount_With.objects.filter(db_username_Pub = self.db_username_Pub) :
            return True

        return False

    

class Like(models.Model):
    db_id_Like = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    AppStore =  models.CharField(max_length=255)
    value = models.CharField(max_length=255)

    def __str__(self):
        return str(self.AppStore)

    def isExists(self):
        if Like.objects.filter(val=self.value):
            return True

        return False

class Wishlist(models.Model):
    db_id_wishlist = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    AppStore =  models.CharField(max_length=255)
    type_wish = models.CharField(max_length=255)
    Category_wish = models.CharField(max_length=255)
    value_wish = models.CharField(max_length=255)


    def __str__(self):
        return str(self.AppStore)

    def isExists(self):
        if Wishlist.objects.filter(val=self.value_wish):
            return True

        return False


class Comment(models.Model):
    db_id_comment = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    AppStore =  models.CharField(max_length=255)
    type_comment = models.CharField(max_length=255)
    Category_comment = models.CharField(max_length=255)
    value_comment = models.CharField(max_length=255)
    subject_comment = models.CharField(max_length=255)
    text_comment = models.TextField(max_length=2000)
    date_comment = models.DateTimeField(auto_now_add=False, auto_now=True)


    def __str__(self):
        return str(self.AppStore)

    def isExists(self):
        if Comment.objects.filter(val=self.value_comment):
            return True

        return False

class Transuction(models.Model):
    username_trans = models.CharField(max_length=255)
    price = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    date = models.DateField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return (self.username_trans)

