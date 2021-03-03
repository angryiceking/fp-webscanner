from django.urls import path
from .views import *
from django.views.decorators.csrf import csrf_exempt

app_name = 'marie'

urlpatterns = [
    path('', csrf_exempt(MarieWelcome.as_view()), name='index'),
    path('register', csrf_exempt(MarieRegister.as_view()), name='register'),
    path('login', csrf_exempt(MarieLogin.as_view()), name='login'),
    path('get_user', csrf_exempt(MarieGetUser.as_view()), name='get_user'),
]