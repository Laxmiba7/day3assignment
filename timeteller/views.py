from django.shortcuts import render
from django.http import HttpResponse
import datetime
import time

# Create your views here.
def homePageView(request):
    return HttpResponse('Hello, World!')

def date(request):
    date = datetime.date.today()
    return HttpResponse("Today's date is: {}".format(date))

def timestamp(request):
    ts = time.time()
    return HttpResponse("Timestamp: {}".format(ts))

    