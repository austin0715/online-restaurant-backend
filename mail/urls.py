from django.urls import path
from . import views

urlpatterns = [
    path('mail/', views.SendEmail.as_view(), name ='mail'),
    path('sms/', views.SendSMS.as_view(), name ='sms')
]
