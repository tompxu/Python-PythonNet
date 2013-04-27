'''
Created on 2013-4-26

@author: miracle
'''
import urllib, sys
f = urllib.urlopen('http://www.baidu.com:80')
for line in f.readlines():
    sys.stdout.write(line)