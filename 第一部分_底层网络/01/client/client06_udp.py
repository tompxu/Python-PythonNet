'''
Created on 2013-4-27

@author: miracle
'''
import socket, sys, struct, time

def getSock(host, port):
    client_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    client_sock.sendto('', (host, port))
    print "Looking for replies:"
    buf = client_sock.recvfrom(2048)[0]
    if len(buf) != 4:
        print "Wrong-sized reply %d:%s" %(len(buf), buf)
        sys.exit(1)
    secs = struct.unpack("!I", buf)[0]
    secs -= 2208988800
    print time.ctime(int (secs))
if __name__ == "__main__":
    getSock('localhost', 12345)