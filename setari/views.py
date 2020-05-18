from django.shortcuts import render
from tan1.monopost import Monopost
import time
import os
from django.conf import settings
import json
from tancparts.models import Panzer
import requests
import random


def home(request):
    obstacol = {"copac":10, "zid":20} # obstacole hardcoded
    ##### PANZER #####
    try:
        dataP = requests.get("http://127.0.0.1:8000/api/panzer/").json()
    except:
        raise Exception(
        'something wrong with the api \n \
        I cant connect to http://127.0.0.1:8000/api/panzer/'
        )
    dataPanzer = random.choice(dataP) # choose a PANZER profile
    healthPanzer = dataPanzer.pop('health') # extract health from profile
    
    #### ABRAMS ####
    try:
        dataA = requests.get("http://127.0.0.1:8000/api/abrams/").json()
    except:
        raise Exception(
        'something wrong with the api \n \
        I cant connect to http://127.0.0.1:8000/api/abrams/'
        )
    dataAbrams = random.choice(dataA) # choose a ABRAMS profile
    healthAbrams = dataAbrams.pop('health') # extract health from profile
    
    f1 = Monopost("Abrams", dataPanzer, obstacol, healthPanzer) # the health of Panzer
    f2 = Monopost("Panzer", dataAbrams, obstacol, healthAbrams) # the health of Abrams
    # start threads
    f1.start()
    f2.start()
    # wait threads to finish and keep main thread running
    f1.join()
    f2.join()
    # send the profile parts and health to the template
    # in order to be displayed if user wants
    return render(request, "home.html", {'dP':dataPanzer, 'hP':healthPanzer, 'dA':dataAbrams, 'hA':healthAbrams})

def zoom(request):
    """
    This reads the text file (logs) and send it to the template
    in order to be handled and displayed by javascript
    """
    file = os.path.join(settings.BASE_DIR, 'logs.txt')
    with open(file) as f:
        lines = f.read().splitlines()
    json_m = json.dumps(lines)
    return render(request, "jo.html", {"lis":json_m})
