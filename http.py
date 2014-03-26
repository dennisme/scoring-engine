#!venv/bin/python

import urllib2, sys, random, csv

pages = ['/', '/admin/', '/store/', '/store/products/']
useragents = csv.reader(open('user-agents.csv', 'r'), delimiter=',')

for i in useragents:
    useragents = i

if (len(sys.argv) == 3):
    proto = sys.argv[1]
    ipaddr = sys.argv[2]
    page = pages[random.randint(0,len(pages) - 1)]
    fulluri = proto + "://" + ipaddr + page
    useragent = { 'User-Agent': useragents[random.randint(0, len(useragents) - 1)] }
    
    request  = urllib2.Request(fulluri, None, headers=useragent)
    response = urllib2.urlopen(request)
    html = response.read()

    print html
else:
    print """
    Usage: ./http.py <protocol> <ip or dns>
        <protocol> - HTTP or HTTPS
        <ip or dns> - IP Address of server or DNS FQDN
    """
