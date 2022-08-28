import email.utils
import smtplib
import datetime
from django.conf import settings
from email.mime.text import MIMEText

def get_remote_addr(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

def send_alert(request, canary_name, context):
    date_time = datetime.datetime.now()
    mailaddress = settings.NOTIFICATION_MAIL
    sender_mail = settings.MAIL_SERVER_SENDER_ADDR
    mail_server = settings.MAIL_SERVER_ADDRESS
    mail_server_port = settings.MAIL_SERVER_PORT
    mail_user = settings.MAIL_SERVER_USER
    mail_passwd = settings.MAIL_SERVER_PASSWD
    remote_addr = get_remote_addr(request)
    alert_message = "The {0} canary was triggered:\n\nBrowser: {1}\n\n\
    Remote IP: {2}\n\nURL string: {3}\n\nTimestamp: {4}".format(canary_name, request.META['HTTP_USER_AGENT'], remote_addr, context['urlstr'], date_time)
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