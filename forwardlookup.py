#!venv/bin/python
#
# Forward DNS Lookup Check
#
# Accepts 3 arguments
# qname, rdtype, and resip
#
# qname - Query Name (www.yzguy.com)
# rdtype - Query Type (A, AAAA, MX)
# resip - Response IP or Response (10.235.5.2, email.yzguy.com.)
# nameserv - Nameserver IP (8.8.8.8)

import dns.resolver, sys

if (len(sys.argv) == 5):
    qname = sys.argv[1]
    rdtype = sys.argv[2]
    respip = sys.argv[3]
    nameserv = sys.argv[4]
    
    try:
        resolver = dns.resolver.Resolver()
        resolver.lifetime = 3.0
        resolver.nameservers = [nameserv]
        resp = resolver.query(qname, rdtype)
        
        if (resp.rrset.to_text()[(len(respip)*-1):] == respip):
            print "PASS: ", resp.rrset.to_text()
        else:
            print "FAIL: ", resp.rrset.to_text()
    except dns.resolver.NXDOMAIN:
        print "FAIL: %s does not exist" % qname
    except dns.resolver.Timeout:
        print "FAIL: Timeout reached"
    except dns.resolver.NoAnswer:
        print "FAIL: No Answer"
    except dns.exception.DNSException:
        print "Unknown error"

else:
    print """
Usage: ./forwardlookup.py <query> <type> <response> <nameserver>
    <query> - FQDN to lookup (ex. www.yzguy.io, yzguy.io)
    <type> - query type (A, AAAA, MX)
    <response> - expected ip response (ex. 10.235.5.6, mail.yzguy.io.)
    <nameserver> - nameserver to query against (ex. 8.8.8.8)
    """
