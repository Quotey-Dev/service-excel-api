from rest_framework import routers
from mainapi import views
from django.conf.urls import url

# make the url super secure as it will should be long

urlpatterns = [
    url(r'^xltyltemblem/', views.SingleInsuerQuote),
]