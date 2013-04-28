'''
Created on 2013-4-19

@author: tqc
'''
import socket, sys

def New_Socket(host, port):
    """
        by host, port , get a socket
    """
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.connect((host, port))
    except socket.gaierror, e:
        print("Error connection to server:%s" % e)
        sys.exit(1)
    except socket.error, e:
        print("socket.err exit")
        sys.exit(1)
    return s

if __name__ == '__main__':
     
    sock = New_Socket('www.google.com.hk', 80,)  
    fd = sock.makefile('rw', 0)
    fd.write('/' + "\r\n")
    for line in fd.readlines():
        sys.stdout.write(line)
    
    sock.sendall('/' + "\r\n")
    while True:
        buf = sock.recv(2024)
        if not len(buf):
            break
    sys.stdout.write(buf)
