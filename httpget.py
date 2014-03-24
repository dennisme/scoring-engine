#!venv/bin/python

import urllib2

response = urllib2.urlopen('https://www.google.com')
html = response.read()

print html
