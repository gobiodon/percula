# percula
A small tool to create canary links written in python. 

## Install
```
git clone https://github.com/gobiodon/percula.git
pip3 install django
pip3 install whitenoise
apt-get install gunicorn3 (on Debian, on any other platform make sure to install the python3 version)
```
## Usage

First you have to edit the file settings.py which you can find in the percula folder. Edit the settings starting with 
"Percula settings" and leave the rest unchanged.

If you used the commands at the top, you can start an instance with (this is not necessarily the best way to deploy
that for production):

```
cd percula
gunicorn3 percula.wsgi -b0.0.0.0:80 --daemon
```
After the first start, you can reach the admin login via URL:

http(s)://your-domain.tls/padmin

The default credentials are admin/admin (you might wanna change that after the first login).

Then go to:

Canary -> Canary strings

Here you can add unique URL strings which will trigger an alarm. Make sure to add a fitting description so you still know what was triggering it in 6 months.

With the option "Canary Settings" you can add the mail server settings Percula should use to send emails. If you don't add anything, Percula will just use the local MTA.

Currently there are 3 ways how you can create canary links:

- http(s)://your-domain.tld/**URLSTRING**/login

This shows a login screen and just opening the url already triggers the alarm.

- http(s)://your-domain.tld/**URLSTRING**/file/$FILENAME

Files with content (e.g. user/passwords) can be added with the option "canary files". For instance, if you add the file "passwords.txt", it will be reachable (and trigger an alarm) when someone opens the following URL:

http(s)://example.tld/**URLSTRING**/file/passwords.txt

But even if you don't add any file in the admin console, as long as the URLSTRING matches, it will trigger an alarm.

- http(s)://your-domain.tld/**URLSTRING**/docfile.png

This is an image URL with a 1px-image which you can insert into e.g. an MS Office file which then triggers the
alarm when someone opens the file.


