'''
Created on 2013-4-27

@author: miracle
'''
import socket, sys
def getSocket(host, textport):
    client_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        port = int(textport)
    except ValueError:
        port = socket.getservbyname(textport, 'udp')
    client_sock.connect((host, port))
if __name__ == "__main__":
    client_sock = getSocket('localhost', 12345)
    print ("Enter data to transmit:")
    data = sys.stdin.readline().strip()
    client_sock.sendall(data)
    print 'Looking for replies:'
    while True:
        buf = client_sock.recv(1024)
        if not len(buf):
            break
        sys.stdout.write(buf)
