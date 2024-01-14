#from django.shortcuts import render

# Create your views here.
from django.core.mail import EmailMessage
from django.conf import settings
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from twilio.rest import Client

class SendEmail(APIView):
    def post(self, request):
        subject = request.data["subject"]
        recipient_list = request.data["email"]
        message = request.data["message"]
        EmailMessage(subject=subject, body=message, to=[recipient_list]).send()
        return Response('Email Sent!')

class SendSMS(APIView):
    def post(self, request):
        account_sid = settings.SMS_ACCOUNT_SID
        auth_token = settings.SMS_AUTH_TOKEN
        client = Client(account_sid, auth_token)
        message = client.messages.create(
                      from_ = settings.SMS_SENDER,
                      body = request.data["SMS_text"],
                      to = request.data["phone"]
                  )
        print(message.sid)
        return Response('SMS Sent!')
