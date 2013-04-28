'''
Created on 2013-4-28

@author: miracle
'''
import sys, socket

def getDNS(host):
    try:
        result = socket.gethostbyaddr(host)
        print "primary hostname:"
        print (result[0])
        for item in result[1]:
            print item
    except socket.herror, e:
        print "Couldn't look up name", e  
if __name__ == "__main__":
    getDNS('127.0.0.1')
    getDNS('192.168.104.252')
    getDNS('8.8.4.4')
    getDNS('8.8.8.8')
    getDNS('2001:6b0:1:ea:a00:20ff:fe8f:708f') #ipv6