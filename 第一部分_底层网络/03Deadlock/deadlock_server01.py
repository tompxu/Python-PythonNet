'''
Created on 2013-4-28

@author: miracle
'''
import socket, traceback

def getSock(host, port):
    servletSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    servletSock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    servletSock.bind((host, port))
    servletSock.listen(1)
    return servletSock
if __name__ == "__main__":
    while True:
        try:
            clientsock, clientaddr = getSock('', 12345).accept()
        except KeyboardInterrupt:
            raise
        except:
            traceback.print_exc()
            continue
        try:
            print "Got connection from", clientsock.getpeername()
            while True:
                data = clientsock.recv(4096)
                if not len(data):
                    break
                clientsock.sendall(data)
        except (KeyboardInterrupt, SystemExit):
            raise
        except:
            traceback.print_exc()
        
        try:
            clientsock.close()
        except KeyboardInterrupt:
            raise
        except:
            traceback.print_exc()
        