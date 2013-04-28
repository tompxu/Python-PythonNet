'''
Created on 2013-4-28

@author: miracle
'''
import sys, socket
from duplicity.globals import hostname
def getipaddrs(hostname):
    """
    Give a host name, perform a standard looup and return a list of Ip address for the host
    """
    result = socket.getaddrinfo(hostname, None, 0, socket.SOCK_STREAM)
    return [x[4][0] for x in result]
if  __name__ == "__main__":
    hostname = socket.gethostname()
    print("host name:", hostname)
    print "Fully-qualified name:", socket.getfqdn(hostname)
    try:
        print "ip address:", ",".join(getipaddrs(hostname))
    except socket.gaierror, e:
        print "Couldn't not ge Ip address", e
        