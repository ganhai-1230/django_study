from django.http import Http404, HttpResponse
from django.shortcuts import render
import datetime


def hello(request):
    return HttpResponse("Hello world")


def homepage(request):
    return render(request, 'mypage.html', {'current_section': 'includes/nav', 'title': 'Home Page'})


def current_datetime(request):
    now = datetime.datetime.now()
    return render(request, 'current_time.html', {'current_date': now})


def hours_ahead(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    return render(request, 'hours_ahead.html', {'hour_offset':offset, 'next_time':dt})