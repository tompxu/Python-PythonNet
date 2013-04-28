import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print ("Looking up port number ...")
port = socket.getservbyname('http','tcp')
print port
s.connect(('www.google.com.hk', port))
print s.getsockname()
print s.getpeername()