from django.shortcuts import render
from django.http import Http404
# from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
from django.core import serializers
from django.conf import settings
import json
import os
from django.conf import settings
import xlwings as xw
import time
import atexit
import signal
import pythoncom
import requests

MAX_EXCEL_TO_LOAD = 2

# pythoncom.CoInitialize()


def newAppExl():

    return xw.App()


# fire up some excel apps pids
for i in range(MAX_EXCEL_TO_LOAD):
    newAppExl()


PROCESS_STACK_REF = xw.apps.keys()
PROCESS_STACK = PROCESS_STACK_REF[:]

loopStack = PROCESS_STACK[:]
excelfiles = os.listdir(settings.EXCEL_FOLDER)



# Create your views here.

@api_view(["POST"])
def SingleInsuerQuote(request):
    return Response("All good")





#region Kill all excells if the program goes off

def killp(pidp):
    os.kill(pidp, signal.SIGTERM)


for pidp in PROCESS_STACK:

    # Using register()
    atexit.register(killp, pidp)

#endregion
