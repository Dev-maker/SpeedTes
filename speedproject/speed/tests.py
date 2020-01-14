from django.test import TestCase

# Create your tests here.
from datetime import datetime
import threading
import firebase_admin
import pyspeedtest
from firebase_admin import credentials, db
from firebase_admin import firestore

from . import models
from .models import Data

import time


cred = credentials.Certificate("/Users/dev/PycharmProjects/0000/geotutorial/geodjango/first-251520-firebase-adminsdk-2basx-1678420d8f.json")
firebase_admin.initialize_app(cred)







db = firestore.client()


def location(request):
    response_string = '{0}'.format(
        request.ipinfo.all

    )

    try:
        if request.method == 'GET' or 'POST' or None:
            while True:
                # More statements comes here
                print(datetime.now().__str__() + ' : Start task in the background')

                time.sleep(5)
                st = pyspeedtest.SpeedTest()
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
                # to sqlite database
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
                download_thread = threading.Thread(target=location, args=request)
                download_thread.start()


    except KeyError as error:
        print(error)
    # context = {
    #     "data": Data.objects.all()
    # }
    # return render(request, 'world/index.html', context)

