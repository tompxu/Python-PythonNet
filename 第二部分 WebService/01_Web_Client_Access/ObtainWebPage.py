'''
Created on 2013-5-2

@author: tqcenglish
'''
import sys, urllib2
url = 'http://www.baidu.com'
fd = urllib2.urlopen(urllib2.Request(url))
while True:
    data = fd.readline()
    if not len(data):
        break
    sys.stdout.write(data)
