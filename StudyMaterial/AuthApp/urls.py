from django.urls import path
from .views import *

urlpatterns = [
    path('/signup/',register_user,name='signup_form'),
    path('/login/',login_user,name='login_form'),
    path('/logout/',logout_user,name='logout_user'),
    ]
