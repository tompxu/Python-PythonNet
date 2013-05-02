'''
Created on 2013-5-2

@author: tqcenglish
'''
import sys, urllib2
req = urllib2.Request("http://httpd.apache.org/nonexistent")
try:
    fd = urllib2.urlopen(req)
except urllib2.HTTPError, e:
    print "Error retriveing data:", e
    print "Server error document follows:\n"
    print e.read()
    sys.exit(1)
except urllib2.URLError, e:
    print "Error retrieving ddata:" , e
    sys.exit(2)
print "Retrieved", fd.geturl()
info = fd.info()
for key, value in info.items():
    print "%s = %s" % (key, value)
    sys.exit(2)

    