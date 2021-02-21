
from random import randint
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from django.contrib.auth.models import User
from authentication.serializers import UserSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
import io
import json
from django.contrib.auth import authenticate
from authentication.models import PhoneNumber
from authentication.models import OTPCode
from twilio.rest import Client
account_sid = 'AC3115cdf0d3c573e8b23d650a90e1026d'
auth_token = '5ad18ba8e64fc837aa304c8befe30d6f'
# Create your views here.

# view all users


def viewAllUser(request):
    users = User.objects.all()
    usersSerializer = UserSerializer(users, many=True)
    jsonParse = JSONRenderer().render(usersSerializer.data)
    return HttpResponse(jsonParse, content_type='application/json')


@csrf_exempt
def registerUser(request):
    if(request.method == "POST"):
        steam = io.BytesIO(request.body)
        parse_user = JSONParser().parse(steam)
        userSerializer = UserSerializer(data=parse_user)
        print(userSerializer.is_valid())
        print(request.body)
        if(userSerializer.is_valid()):
            userSerializer.save()
            user = (User.objects.get(username=parse_user['username']))
            PhoneNumber(
                user=user, phoneNumber=parse_user['phoneNumber']).save()
        return HttpResponse(request.body, content_type='application/json')


# random number generator
def random_with_N_digits(n):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return randint(range_start, range_end)


loginUsername = ''


@csrf_exempt
def loginUser(request):
    if(request.method == 'POST'):
        print("###############################")
        print(request.body)
        print("###############################")
        steam = io.BytesIO(request.body)
        print("###############################")
        print(steam)
        print("###############################")

        parse_user = JSONParser().parse(steam)
        print("###############################")
        print(parse_user)
        print("###############################")
        user = authenticate(
            username=parse_user['username'],
            password=parse_user['password'])
        if(user is not None):
            print(user)
            print('username--->'+User.objects.get(username=user).username)
            phoneNumber = PhoneNumber.objects.get(user=user)

            client = Client(account_sid, auth_token)
            message = client.messages.create(
                from_='+17722476938',
                body=random_with_N_digits(6),
                to='+977' + str(phoneNumber.phoneNumber)
            )
            print("message.sid################")
            print(message.body)
            sms = int(str(message.body).split('-')[1].strip(' '))
            print(sms)
            print("message.sid################")
            try:

                if(OTPCode.objects.get(user=user)):
                    otpcode = OTPCode.objects.get(user=user)
                    otpcode.otpcode = sms
                    otpcode.save()
                    loginUsername = user
            except OTPCode.DoesNotExist:
                otpcode = OTPCode.objects.create(user=user, otpcode=sms)
                otpcode.save()
            # print(usernameLogin)
            # print((user.email))

            return HttpResponse(request.body, content_type='application/json')
        else:
            msg = {'error': 'Invalid credentials'}
            print(msg)
            json_msg = JSONRenderer().render(data=msg)
            return HttpResponse(json_msg, content_type='application/json')


@csrf_exempt
def verifyOTPCode(request):
    if(request.method == 'POST'):
        print(request.body)
        stream = io.BytesIO(request.body)
        parse_data = JSONParser().parse(stream)
        print(parse_data)
        user = User.objects.get(username=parse_data.get('username'))
        print(user)
        otpcode = OTPCode.objects.get(user=user)
        print(otpcode)
        print(otpcode.otpcode)
        if(otpcode.otpcode == parse_data.get('otp')):
            msg = {'msg': 'U R Authorized TO ACCESS'}
            print(msg)
            json_msg = JSONRenderer().render(data=msg)
            return HttpResponse(json_msg, content_type='application/json')

        # otpcode = OTPCode.objects.get(user=loginUsername)
        msg = {'error': "INvALID otpcode"}
        json_msg = JSONRenderer().render(data=msg)
        return HttpResponse(json_msg, content_type='application/json', status=400)
