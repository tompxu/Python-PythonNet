'''
Created on 2013-4-28

@author: miracle
'''
import sys, socket
def getipaddrs(hostname):
    result = socket.getaddrinfo(hostname, None, 0, socket.SOCK_STREAM)
    return [x[4][0] for x in result]
def gethostname(ipaddr):
    return socket.gethostbyaddr(ipaddr)[0]

if __name__== "__main__":
    try:
        hostname = gethostname("8.8.8.8")
        ipaddrs = getipaddrs(hostname)
        #print ipaddrs
    except socket.herror, e:
        print "No host name available"; 
        sys.exit(0)
    except socket.gaierror, e:
        print "Got hostname %s, but it could not be forward-resolve" % (hostname, str(e))
        sys.exit(1)
    if not '8.8.8.8' in ipaddrs:
        print "Got hostname %s  but on forward lookup," % hostname
        print "original IP %s did not appear in IP address list" % '8.8.8.8' 
        sys.exit(1)
    else:
        print "Validated hostname", hostname
        