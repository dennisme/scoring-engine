#!/usr/bin/python
#
# Dependencies: dnspython
#
# DNS Lookup Check
#
#   Usage: ./dnslookup.py <qname> <rdtype> <expans> <nameserver>
#       <qname> - Query Name (A/CNAME: FQDN, NS/MX: Domain Name, PTR: IP Address)
#       <rdtype> - Query Type (A, MX, NS, CNAME, PTR)
#       <expans> - Expected Answer (A/CNAME: IP Address, PTR/CNAME/MX/NS: FQDN)
#       <nameserver> - IP Address of Nameserver to perform lookup against
#
#   Author: Adam Smith

import dns.resolver, dns.reversename, sys

if (len(sys.argv) == 5):
    qname = sys.argv[1]
    rdtype = sys.argv[2]
    expans = sys.argv[3]
    nameserver = sys.argv[4]
    
    if (rdtype == 'PTR'):
        qname = dns.reversename.from_address(qname)
        expans = expans + "."
    elif (rdtype == 'MX' or rdtype == 'CNAME' or rdtype == 'NS'):
        expans = expans + "."

    try:
        resolver = dns.resolver.Resolver()
        resolver.lifetime = 3.0
        resolver.nameservers = [nameserver]
        resp = resolver.query(qname, rdtype)
        resplen = len(resp)

        def passed():
            print "PASS: ", resp.rrset.to_text()
            sys.exit(0)

        def failed():
            print "FAIL: ", resp.rrset.to_text()
        
        if (resplen > 1):
            for line in resp:
                ans = line.to_text()[(len(expans)*-1):]
                if (ans == expans):
                    passed()
                elif (ans != expans):
                    if (resplen > 1):
                        resplen -= 1
                        pass
                    else:
                        failed()
                else:
                    failed()
        else:
            print resp.rrset.to_text()[(len(expans)*-1):]
            if (resp.rrset.to_text()[(len(expans)*-1):] == expans):
                passed()
            else:
                failed()
    except dns.resolver.NXDOMAIN:
        print "FAIL: %s does not exist" % qname
        sys.exit(1)
    except dns.resolver.Timeout:
        print "FAIL: Timeout reached"
        sys.exit(1)
    except dns.resolver.NoAnswer:
        print "FAIL: No Answer"
        sys.exit(1)
    except dns.exception.DNSException:
        print "Unknown error"
        sys.exit(1)

else:
    print """
Usage: ./dnslookup.py <qname> <rdtype> <expans> <nameserver>
    <qname> - Query Name (A/CNAME: FQDN, NS/MX: Domain Name, PTR: IP Address)
    <rdtype> - Query Type (A, MX, NS, CNAME, PTR)
    <expans> - Expected Answer (A/CNAME: IP Address, PTR/CNAME/MX/NS: FQDN)
    <nameserver> - IP Address of Nameserver to perform lookup against
    """
