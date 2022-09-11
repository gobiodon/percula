import email.utils
from logging import NullHandler
import smtplib
import datetime
from django.conf import settings
from email.mime.text import MIMEText
from .models import *

def get_remote_addr(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    try:
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip
    except Exception as e:
        print(e)
        return "unknown"

def send_alert(request, canary_name, context):
    mail_settings = None    
    mailaddress = None
    sender_mail = None
    mail_server = None
    mail_server_port = None
    mail_user = None
    mail_passwd = None
    try:
        mail_settings = CanarySetting.objects.all()[:1].get()
    except:
        print("No mail settings, use defaults")

    date_time = datetime.datetime.now()
    mailaddress = context['notification_mail']
    if mail_settings:
        sender_mail = mail_settings.mail_sender_addr
        mail_server = mail_settings.mail_server
        mail_server_port = mail_settings.mail_port
        mail_user = mail_settings.mail_user
        mail_passwd = mail_settings.mail_passwd
    else:
        mail_server = "localhost"
        sender_mail = "percula@localhost"
    remote_addr = get_remote_addr(request)
    alert_message = "The {0} canary was triggered:\n\nBrowser: {1}\n\n".format(canary_name, request.META['HTTP_USER_AGENT']) + \
    "Remote IP: {0}\n\nURL string: {1}\n\nURL Descrption: {3}\n\nTimestamp: {2}".format(remote_addr, context['urlstr'], date_time, context['urldesc'])
    if "filename" in context:
        alert_message += "\n\nfilename: {0}".format(context['filename'])
    msg = MIMEText(alert_message)
    msg['To'] = email.utils.formataddr((mailaddress, mailaddress))
    msg['From'] = email.utils.formataddr(("Percula", sender_mail))
    msg['Subject'] = "(Percula) ALERT {0} Canary triggered".format(canary_name)
    if mail_server == "localhost" or mail_server == "127.0.0.1":
        server = smtplib.SMTP()
        server.connect ('localhost', 25)
        try:
            server.sendmail(mailaddress, [mailaddress], msg.as_string())
        finally:
            server.quit()
    else:
        with smtplib.SMTP(mail_server, mail_server_port) as server:
            server.ehlo()
            server.starttls()
            server.login(mail_user, mail_passwd)
            try:
                server.sendmail(mailaddress, [mailaddress], msg.as_string())
            finally:
                server.quit()