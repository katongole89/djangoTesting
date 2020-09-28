from django.shortcuts import render
from .models import verificationDetails
from django.http import JsonResponse
from rest_framework import status
from .services import allReusableMethods
from django.utils import timezone
from rest_framework.views import APIView

#random code generation
from random import randint
#import africastalking
import string
import random

# Create your views here.

#OTP generation and sms sending
class sendOTP(APIView):
    def post(self, request):
        phoneNumber = request.data.get("phoneNumber")
        
        #generate random code
        count = 0
        code = ''
        while count<5:
            codeValue = randint(0,9)
            code += str(codeValue)
            count+=1
        #end of code generation

        #register otp in database
        registerOTP = verificationDetails(phoneNumber = phoneNumber, otp = code)
        registerOTP.save()

        #send sms
        print(code)
        
        data = {
            'status': 'success',
            'detail': 'OTP sent'
        }

        return JsonResponse(data, status = status.HTTP_200_OK)

class verifyOTP(APIView):
    def post(self, request):
        phoneNumber = request.data.get("phoneNumber")
        otp = request.data.get("otp")
        # check if phoneNumber exists
        checkPhoneNumber = verificationDetails.objects.filter(phoneNumber= phoneNumber)
        if not checkPhoneNumber:
            data = {
                'status': 'failed',
                'detail': 'this phone number has no otp related with it'
            }
            return JsonResponse(data, status = status.HTTP_401_UNAUTHORIZED)
        #get the object using phoneNumber and check if its the correct otp
        getOtp = verificationDetails.objects.get(phoneNumber= phoneNumber)
        if getOtp.otp != otp:
            data = {
                'status': 'failed',
                'detail': 'incorect otp'
            }
            return JsonResponse(data, status = status.HTTP_401_UNAUTHORIZED)
        #if true check if its not expired
        # expiration time is 15minutes
        getDate = getOtp.dateCreated

        expirationTime = 15
        currentTime = timezone.now()

        #check code if its still valid
        timeInSec = allReusableMethods.timedifference(getDate,currentTime)
        print(timeInSec)

        if timeInSec <= 900.0:
            checkPhoneNumber.update(validated= True)
            data = {
                'status': 'success',
                'detail': 'phone validated'
            }
            return JsonResponse(data, status= status.HTTP_200_OK)
        data = {
            'status': 'failed',
            'detail': 'otp expired'
        }
        return JsonResponse(data, status = status.HTTP_401_UNAUTHORIZED)
