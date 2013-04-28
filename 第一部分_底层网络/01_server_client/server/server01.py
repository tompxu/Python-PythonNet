'''
Created on 2013-4-19

@author: tqc
'''
import socket, sys
def getServerSock(host , port ):
    
    serv_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serv_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    serv_socket.bind((host, port))
    serv_socket.listen(1)
    return serv_socket

if __name__ == '__main__':
    port = 12345
    serv_socket = getServerSock('', port)
    print("Server is running on port %d; press Ctrl-C to terminate" % port)
    while True:
        clientsock, clientaddr = serv_socket.accept()
        clientfile = clientsock.makefile("rw", 0)
        clientfile.write("welcome, " + str(clientaddr) + '\n')
        clientfile.write("please enter a string:")
        line = clientfile.readline().strip()
        clientfile.write("You entered %d characters.\n" % len(line))
        clientfile.write(line + '\n')
        clientsock.close()
        clientfile.close()