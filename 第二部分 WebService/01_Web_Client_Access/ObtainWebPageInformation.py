'''
Created on 2013-5-2

@author: tqcenglish
'''
import sys, urllib2
url = 'http://www.baidu.com/'
fd = urllib2.urlopen(urllib2.Request(url))
print "Retrived", fd.geturl()
info = fd.info()
for key, value in info.items():
    print "%s = %s " % (key, value)