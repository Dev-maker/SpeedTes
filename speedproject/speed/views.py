from datetime import datetime
import threading
from urllib import request

import firebase_admin
import pyspeedtest
from django.shortcuts import render
from firebase_admin import credentials, db
from firebase_admin import firestore

from speed import models
from .models import Data

import time

cred = credentials.Certificate(
    "/Users/dev/PycharmProjects/0000/geotutorial/geodjango/first-251520-firebase-adminsdk-2basx-1678420d8f.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

st = pyspeedtest.SpeedTest()


"""to display all the data """
def list(request):
   data = Data.objects.all()
   context = {
        'data': data
    }
   return render(request, 'speed/show_data.html', context)


def home(request):
    return render(request, 'speed/index.html')







# main function to get all user data and store it the database
def get_data(request):
    try:
        if request.method == 'GET' or 'POST' or None:
            # while True:

            # print(datetime.now().__str__() + ' : Start task in the background')

            # time.sleep(300)

            download = st.download()
            upload = st.upload()
            ping = st.ping()
            # to firebase database
            doc_ref = db.collection(u'userData')
            doc_ref.add({
                u'ip': request.ipinfo.all['ip'],
                u'post': request.ipinfo.all['postal'],
                u'city': request.ipinfo.all['region'],
                u'location': request.ipinfo.all['loc'],
                u'hostname': request.ipinfo.all['hostname'],
                u'organisation': request.ipinfo.all['org'],
                u'Date': datetime.now(),
                u'download': download,
                u'upload': upload,
                u'ping': ping,

            })
            # to sqlite ,sql and postgresql database
            save = models.Data()
            save.IpAddress = request.ipinfo.all['ip']
            save.city = request.ipinfo.all['region']
            save.location = request.ipinfo.all['loc']
            save.hostname = request.ipinfo.all['hostname']
            save.post = request.ipinfo.all['postal']
            save.organisation = request.ipinfo.all['org']
            save.date = datetime.now()
            save.download = st.download()
            save.upload = st.upload()
            save.ping = st.ping()

            save.save()

            # download_thread = threading.Thread(target=location, args=request)
            # download_thread.start()


    except KeyError as error:
        print(error)
    #     the data that will be showed to the user
    response_string = 'o'.format(
        request.ipinfo.all)
    download = st.download()
    upload = st.upload()
    ping = st.ping()

    context = {'response_string': response_string,
               'download': download, 'upload': upload, 'ping': ping}
    return render(request, 'speed/index.html', context)
