#!venv/bin/python

import urllib2, sys, random

pages = ['/', '/admin', '/store']

if (len(sys.argv) == 2):
    ipaddr = sys.argv[1]
    page = random.randint(0,len(pages)-1)
    pagetoget = pages[page]
    


#response = urllib2.urlopen('https://www.google.com')
#html = response.read()

#print html
else:
    print """

    """
