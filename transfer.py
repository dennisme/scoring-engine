#!venv/bin/python

import dns.query
import dns.zone

teams = [ ['10.235.1.10', 'team1.asist'],
          ['10.235.5.2', 'yzguy.io'],
          ['10.235.2.10', 'team2.asist'],
          ['10.235.3.10', 'team3.asist'],
          ['10.235.4.10', 'team4.asist'],
          ['10.235.5.10', 'team5.asist'],
          ['10.235.6.10', 'team6.asist'],
          ['10.235.7.10', 'team7.asist'],
          ['10.235.8.10', 'team8.asist'] ]

for i in teams:
    try:
        z = dns.zone.from_xfr(dns.query.xfr(i[0], i[1]))
        names = z.nodes.keys()
        names.sort()
        for n in names:
            print z[n].to_text(n)
        print '\n'
    except Exception:
        print 'FAIL: [%s, %s]\n' % (i[0], i[1])
        pass
