#!/usr/bin/python

import socket
import random

ips = ['10.235.5.6', '10.235.5.7', '10.235.5.8']

i = random.randint(0,len(ips)-1)
response = socket.gethostbyaddr(ips[i])
print ips[i] + ' ' +  response[0]
