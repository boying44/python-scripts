#import socket module 
from socket import *                                   

TCP_HOST = gethostname()
TCP_PORT = 8000
BUFF_SIZE = 1024

serverSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
serverSocket = socket(AF_INET, SOCK_STREAM) 
serverSocket.bind((TCP_HOST, TCP_PORT))

#Listen for one connection
serverSocket.listen(1)
while True: 
    #Establish the connection 
    print 'Ready to serve...' 
    connectionSocket, addr = serverSocket.accept() 
    try: 
        message = connectionSocket.recv(BUFF_SIZE).decode() #Why decode?
        filename = message.split()[1]                  
        f = open(filename[1:])                         
        outputdata = f.read()
        #Send one HTTP header line into socket
        connectionSocket.send('HTTP/1.1 200 OK\n\n')
        #Send the content of the requested file to the client
        for i in range(0, len(outputdata)):       
            connectionSocket.send(outputdata[i])   
        connectionSocket.close()
    except IOError: 
        connectionSocket.send('HTTP/1.1 404 Not Found\n\n')
        connectionSocket.send('404 Not Found\n')
        connectionSocket.close()
serverSocket.close()                                     