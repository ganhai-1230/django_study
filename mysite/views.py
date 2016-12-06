from django.http import Http404, HttpResponse
from django.shortcuts import render
import datetime


def hello(request):
    return HttpResponse("Hello world")


def current_datetime(request):
    now = datetime.datetime.now()
    return render(request, 'current_time.html', {'current_date':now})


def hours_ahead(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    html = "In {} hours(s), it will be {}".format(offset, dt)
    return HttpResponse(html)