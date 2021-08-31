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




# This is responsible to read and write to excel apis
@api_view(["POST"])
def SingleInsuerQuote(request):
    returnValue = {}
    # request should have
    # 1. file name with extension
    # 2. sheet name
    # 3. input range
    # 4. output range
    # 5. input data

    filename = None
    sheetname = None
    inputrange = None
    outputrange = None
    inputdata = None

    try:
        incomingdata = json.loads(request.body)
        filename = incomingdata["filename"]
        sheetname = incomingdata["sheetname"]
        inputrange = incomingdata["inputrange"]
        outputrange = incomingdata["outputrange"]
        inputdata = incomingdata["inputdata"]
    except:
        return Response("INVALID_BODY")

    
    # preserve pid from the PROCESS STACK
    poppedProcess = []
    while(not poppedProcess):
        try:
            poppedProcess = PROCESS_STACK.pop()
            print(str(PROCESS_STACK))
        except:
            time.sleep(2)
            print("stack empty -- ")

        # FILE OPENING SECTION
    wb = None
    sht = None

    insurerfile = os.path.join(
            settings.EXCEL_FOLDER, filename)

    try:
        wb = xw.apps[poppedProcess].books.open(
            insurerfile, read_only=True, ignore_read_only_recommended=True, update_links=False)
    except:
        PROCESS_STACK.append(poppedProcess)
        print(PROCESS_STACK)
        return Response("COULD NOT OPEN FILE " + str(insurerfile))
    try:
        sht = wb.sheets[sheetname]
    except:
        PROCESS_STACK.append(poppedProcess)
        print(PROCESS_STACK)
        return Response("COULD NOT OPEN SHEET " + str(sheetname) + " OF FILE " + str(insurerfile))

    # print(str(AUTOinputmap))
    # print(str(AUTOoutputmap))

    # Use the pid and put values and read values also if anything goes wrong generate a new pid and add to process id
    try:
        #input data should in the form : [[],[],[],...]
        sht.range(inputrange).value = inputdata
    except:
        PROCESS_STACK.append(poppedProcess)
        print(PROCESS_STACK)
        return Response("COULD NOT WRITE IN SHEET " + str(sheetname) + " OF FILE " + str(insurerfile) + " " + "with input range " + inputrange)

    try:
        returnValue["covers"] = sht.range(outputrange).value
    except:
        # TODO ADD new pid by calling special function and do not append it
        return Response({"action": "ADD_PID", "message": "COULD NOT READ COVERS"})


    # erasing the data
    try:
        sht.range(inputrange).value = [[""]]*(len(inputdata)) # this will produce [[""],[""],[""],...]
    except:
        # TODO ADD new pid by calling special function and do not append it
        return Response({"action": "ADD_PID", "message": "COULD NOT ERASE BACK"})

    PROCESS_STACK.append(poppedProcess)
    print(PROCESS_STACK)

    return Response(returnValue)





#region Kill all excells if the program goes off

def killp(pidp):
    os.kill(pidp, signal.SIGTERM)


for pidp in PROCESS_STACK:

    # Using register()
    atexit.register(killp, pidp)

#endregion
