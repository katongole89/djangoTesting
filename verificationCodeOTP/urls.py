from django.contrib import admin
from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('sendOTP/',views.sendOTP.as_view(), name='sendOTP'),
    path('verifyOTP/',views.verifyOTP.as_view(), name='verifyOTP'),
    
]
urlpatterns= format_suffix_patterns(urlpatterns)