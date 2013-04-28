'''
Created on 2013-4-27

@author: miracle
'''
import socket, traceback

def getSock(host, port):
    serverSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    serverSock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    serverSock.bind((host, port))
    return serverSock
if __name__=="__main__":
    serverSock = getSock('localhost', 12345)
    while True:
        try:
            mesage, address = serverSock.recvfrom(8192)
            print "Got data from", address
            serverSock.sendto(mesage, address)
        except (KeyboardInterrupt, SystemExit):
            raise
        except:
            traceback.print_exc()