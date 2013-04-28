'''
Created on 2013-4-27

@author: miracle
'''
import socket
import struct
import time
import traceback
def getSock(host, port):
    serverSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    serverSock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    serverSock.bind((host, port))
    return serverSock
if __name__ == "__main__":
    serverSock = getSock("", 12345)
    try:
        message, address = serverSock.recvfrom(1024)
        secs = int(time.time())
        secs -= 60 * 60 * 24
        secs += 2208988800
        reply = struct.pack("!I", secs)
        serverSock.sendto(reply, address)
    except (KeyboardInterrupt, SystemExit):
        raise
    except:
        traceback.print_exc()