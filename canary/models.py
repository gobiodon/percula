from django.db import models



class CanaryString(models.Model):
    urlstr = models.CharField("URL String", max_length=60)
    urldesc = models.CharField("Description", max_length=250)
    email = models.EmailField("Notification E-Mail")
    enabled = models.BooleanField(default=True)

    def __str__(self):
        return self.urldesc

class CanaryFile(models.Model):
    filename = models.CharField("Filename", max_length=100)
    content = models.TextField("File Content")

    def __str__(self):
        return self.filename

class CanarySetting(models.Model):
    mail_server = models.CharField("SMTP Server", max_length=100, default="localhost")
    mail_user = models.CharField("SMTP Username", max_length=100, default="user@server.exmaple")
    mail_passwd = models.CharField("SMTP Password", max_length=150, default="supersecurepassword")
    mail_port = models.CharField("SMTP Port", max_length=3, default="587")
    mail_sender_addr = models.EmailField("SMTP Sender Address", default="percula@localhost")

    def __str__(self):
        return "Percula Settings"

