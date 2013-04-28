'''
Created on 2013-4-28

@author: miracle
'''
import socket, sys
from pydoc import cli

def getSock(host, port):
    clientSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    clientSock.connect((host, port))
    return clientSock
if __name__ == "__main__":
    data = "*" * 1024 * 1024
    clientSock = getSock("localhost", 12345)
    byteWrited = 0
    while byteWrited < len(data):
        senddataLen = min(1024, len(data[byteWrited:]))
        clientSock.sendall(data[byteWrited:byteWrited+senddataLen])
        byteWrited += senddataLen
        sys.stdout.write("Wrote %d kbytes\r" % (byteWrited / 1024))
        sys.stdout.flush()
    clientSock.shutdown(1)
    
    print "All data send."
    while True:
        buf = clientSock.recv(1024)
        if not len(buf):
            break
        sys.stdout.write(buf)