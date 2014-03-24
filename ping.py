#!venv/bin/python

import os
ip = '10.235.5.2'
response = os.system("ping -c 1 " + ip)

if response == 0:
    print ip, 'is up!'
else:
    print ip, 'is down!'
