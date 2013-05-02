'''
Created on 2013-5-2

@author: tqcenglish
'''
#Submit GET Data 
import sys, urllib2, urllib
def addGETdata(url, data):
    """Adds data to url
    """
    return url + '?' + urllib.urlencode(data)
zipcode = '10001'
url = addGETdata('http://www.wunderground.com/cgi-bin/findweather/getForecast', [('query', zipcode)])
print "Using URL", url
req = urllib2.Request(url)
fd = urllib2.urlopen(req)
while True:
    data = fd.read(1024)
    if not len(data):
        break
    sys.stdout.write(data)