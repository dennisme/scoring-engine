#!venv/bin/python

import urllib2, sys, random, csv

pages = csv.reader(open('pages.csv', 'r'), delimiter=',')
useragents = csv.reader(open('user-agents.csv', 'r'), delimiter=',')

for page in pages:
    pages = page

for useragent in useragents:
    useragents = useragent

if (len(sys.argv) == 3):
    proto = sys.argv[1]
    ipaddr = sys.argv[2]
    page = pages[random.randint(0,len(pages) - 1)]
    print page
    fulluri = proto + "://" + ipaddr + page
    useragent = { 'User-Agent': useragents[random.randint(0, len(useragents) - 1)] }
    
    request  = urllib2.Request(fulluri, None, headers=useragent)
    response = urllib2.urlopen(request)
    html = response.read()

    print html
else:
    print """
        Usage: ./httpget.py <protocol> <ip or dns>
        <protocol> - HTTP or HTTPS
        <ip or dns> - IP Address of server or DNS FQDN
    """
