from django.conf.urls import url    
from .views import register, login, logout
from django.contrib.auth import views as auth_views

    
urlpatterns = [
    url('register', register),
    url('login', login),
    url('logout', logout),    
]