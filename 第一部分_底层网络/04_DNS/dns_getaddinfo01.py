'''
Created on 2013-4-28

@author: miracle
'''
import sys, socket
count = 1
#result = socket.getaddrinfo('www.baidu.com', None)
result = socket.getaddrinfo('www.baidu.com', None, 0, socket.SOCK_STREAM) # set protool and family
print result
for item in result:
    print "%-2d: %s" %(count, item[4])
    count += 1
