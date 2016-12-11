from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import render
import datetime
from mysite.forms import ContactForm
from django.core.mail import send_mail


def hello(request):
    return HttpResponse("Welcome to the page at %s" % request.path)


def meta(request):
    values = request.META.items()
    values = sorted(values)
    html = []
    for k, v in values:
        html.append('<tr><td>%s</td><td>%s</td></tr>' % (k, v))
    return HttpResponse('<table>%s</table>' % '\n'.join(html))


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
    return render(request, 'hours_ahead.html', {'hour_offset': offset, 'next_time': dt})


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            send_mail(cd['subject'], cd['message'],cd.get('email','noreply@example.com'),['siteowner@example.com'])
            return HttpResponseRedirect('/contact/thanks')
    else:
        form = ContactForm(initial={'subject':'I love your sizte!'})
    return render(request, 'contact_form.html', {'form':form})