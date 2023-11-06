from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.views import View
# from django.contrib.auth import views as auth_views

import sys , os
from .views import *
from . import views

from .login import *
from . import login

from .signUp import *
from . import signUp

from .profile import *
from . import profile

from .publish import *
from . import publish

from .monitor import *
from . import monitor

from django.urls import include, path
from django.conf.urls import include

urlpatterns = [
    path('home/' , views.home, name='home'),
    path('fullView/<int:id>' , views.fullView, name='fullView'),
    path('', login.login_tab, name='login_tab'),
    path('reset_Password/', views.reset_Password, name='reset_Password'),
    path('account/register/', signUp.register, name='register'),
    path('account/register/addrecord/', signUp.addrecord, name='addrecord'),
    path('activate/<uidb64>/<token>', views.activate, name='activate'),
    path('verify/<auth_token>' , signUp.verify , name="verify"),
    path('search/', views.search, name='search'),
    path('account/error' , signUp.error_page , name="error"),
    path('profile/', profile.profile, name='profile'),
    path('profile/update_Profile/<int:id>', profile.update_Profile, name='update_Profile'),
    path('publish/', publish.publish, name='publish'),
    path('publish/add_AppStore/', publish.add_AppStore, name='add_AppStore'),
    path('accountManage/', monitor.accountManage, name='accountManage'),
    path('status/', monitor.status, name='status'),
    path('setting/', monitor.setting, name='setting'),
    path('setting/change_Email/<int:id>', monitor.change_Email, name='change_Email'),
    path('setting/change_Password/<int:id>', monitor.change_Password, name='change_Password'),
    path('gamePage/', views.gamePage, name='gamePage'),
    path('socialPage/', views.socialPage, name='socialPage'),
    path('sportPage/', views.sportPage, name='sportPage'),
    path('topPage/', views.topPage, name='topPage'),
    path('like/', views.like, name='like'),
    path('wishlist/', views.wishlist, name='wishlist'),
    path('wishlistView/', views.wishlistView, name='wishlistView'),
    path('comment/', views.comment, name='comment'),

    #path('', views.homeOut, name='homeOut'),
    path('create-session-checkout/<int:id>/<str:name>/<int:price>', views.create_session_checkout, name='checkout'),
    path('success.html/<int:id>', views.success,name='success'),
    path('cancel.html/', views.cancel,name='cancel'),
    path('webhooks/stripe/', views.webhook,name='webhook'), #updated line


    #path('', views.homeOut, name='homeOut'),
    path('create-session-out/<str:Username>/<int:price>', publish.create_session_out, name='public'),
    path('success.html/', publish.success,name='success'),
    path('cancel.html/', publish.cancel,name='cancel'),
    path('webhooks/stripe/', publish.webhook,name='webhook'), #updated line

    path('transfer/', monitor.transfer, name='transfer'),
    path('create/', monitor.create, name='create'),


# ____------------------------------------------------------------------------------------------____ #
    path('layout_account/', views.layout_account_footer, name='layout_account_footer'),
    path('layout_account/', views.layout_account_header, name='layout_account_header'),
    path('layout_main/', views.layout_main_header, name='layout_main_header'),
    path('layout_main/', views.layout_main_footer, name='layout_main_footer'),
    path('', views.logout, name='logout'),
] 
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# print(static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT))
