from django.urls import path
from .views import *
from django.views.decorators.csrf import csrf_exempt

app_name = 'marie'

urlpatterns = [
    path('', csrf_exempt(MarieBiscuit.as_view()), name='index'),
]