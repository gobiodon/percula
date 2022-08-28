from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse
from django.http import FileResponse
from .percuhe import *


def loginpage(request, urlstr):
    allowed_url = settings.ALLOWED_URL_STRINGS
    context = {'urlstr': urlstr, 'allowed_url': allowed_url}

    if urlstr in allowed_url:
        send_alert(request, "loginpage", context)
        return render(request, 'canary/loginpage.html', context)
    else:
        return HttpResponse(".")

def files(request, urlstr, filename):
    allowed_url = settings.ALLOWED_URL_STRINGS
    context = {'urlstr': urlstr, 'allowed_url': allowed_url, 'filename': filename}

    if urlstr in allowed_url:
        send_alert(request, "files", context)
        return render(request, 'canary/files.html', context)
    else:
        return HttpResponse(".")

def docfile(request, urlstr):
    allowed_url = settings.ALLOWED_URL_STRINGS
    context = {'urlstr': urlstr, 'allowed_url': allowed_url}

    if urlstr in allowed_url:
        send_alert(request, "docfile", context)
        image = open('static/img/bg.png', 'rb')
        response = FileResponse(image)
        return response
    else:
        return HttpResponse(".")
    