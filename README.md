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

First you have to edit the file settings.py which you can find in the percula folder. Edit the settings starting at 
"Percula settings" and leave the rest unchanged.

The most important setting is ALLOWED_URL_STRINGS, because the strings have to match the one used in the URL. It
also allows you to track which URL you created for which purpose. URLSTRING refers to one of the strings from that list.
You can create as many entries as you like. They don't need to be in any specific form, but stay with letters and numbers.

If you used the commands at the top, you can start an instance with (this is not necessarily the best way to deploy
that for production):

```
cd percula
gunicorn3 percula.wsgi -b0.0.0.0:80 --daemon
```

If a canary is triggered, percula will send out an e-mail to the address configured in settings.py.

Currently there are 3 ways how you can create canary links:

- http(s)://your-domain.tld/**URLSTRING**/file/passwords.txt

The filename at the end can be anything you like, it always triggers the canary. Currently it shows a list of usernames and passwords, 
but you can edit that to anything you like in the templates.

- http(s)://your-domain.tld/**URLSTRING**/login

This shows a login screen and just opening the url already triggers the alarm.

- http(s)://your-domain.tld/**URLSTRING**/docfile.png

This is an image URL with a 1px-image which you can insert into e.g. an MS Office file which then triggers the
alarm when someone opens the file.


