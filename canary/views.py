from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse
from django.http import FileResponse
from .percuhe import *
from .models import *


def loginpage(request, urlstr):
    allowed_url = CanaryString.objects.filter(enabled=True)

    for url in allowed_url:
        if url.urlstr == urlstr:
            context = {
                "urlstr": url.urlstr,
                "urldesc": url.urldesc,
                'notification_mail': url.email,
            }
            send_alert(request, "loginpage", context)
            return render(request, 'canary/loginpage.html', context)

    return HttpResponse(".")

def files(request, urlstr, filename):
    allowed_url = CanaryString.objects.filter(enabled=True)
    for url in allowed_url:
        if url.urlstr == urlstr:
            context = {
                "urlstr": url.urlstr,
                "urldesc": url.urldesc,
                "filename": filename,
                'notification_mail': url.email,
            }
            send_alert(request, "files", context)
            try:
                file_data = CanaryFile.objects.filter(filename=filename)[:1].get()
                context['content'] = file_data.content
                return render(request, 'canary/files.html', context)
            except:
                return render(request, 'canary/files.html', {'content': "admin:Dmwc954n3s9245"})

    return HttpResponse(".")


def docfile(request, urlstr):
    allowed_url = CanaryString.objects.filter(enabled=True)
    for url in allowed_url:
        if url.urlstr == urlstr:
            context = {
                'urlstr': urlstr, 
                'allowed_url': allowed_url, 
                'urldesc': url.urldesc,
                'notification_mail': url.email,
                }
            send_alert(request, "docfile", context)
            image = open('static/img/bg.png', 'rb')
            response = FileResponse(image)
            return response
    return HttpResponse(".")

    