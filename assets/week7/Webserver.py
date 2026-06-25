#import socket module 
from socket import * 
import sys # In order to terminate the program 

serverSocket = socket(AF_INET, SOCK_STREAM) 

# Prepare a sever socket 
serverPort = 6790 
serverSocket.bind(('', serverPort))
serverSocket.listen(1)

while True: 
    # Establish the connection 
    print('Ready to serve...') 
    connectionSocket, addr = serverSocket.accept()
    
    try: 
        message = connectionSocket.recv(1024).decode()
        if not message: 
            continue
            
        print(f"{message.split()[1]}") 
        
        filename = message.split()[1]                
        f = open(filename[1:], encoding="utf-8")                         
        
        outputdata = f.read() 
        
        # Send one HTTP header line into socket 
        header = "HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n"
        print(f"Mengirim Header ke Browser:\n{header}") 
        connectionSocket.send(header.encode())

        # Send the content of the requested file to the client 
        for i in range(0, len(outputdata)):            
            connectionSocket.send(outputdata[i].encode())
            
        connectionSocket.send("\r\n".encode()) 
        connectionSocket.close()
        print("File berhasil terkirim!\n") 
        
    except IOError: 
        print("File tidak ditemukan!\n")
        connectionSocket.send("HTTP/1.1 404 Not Found\r\n\r\n".encode())
        connectionSocket.send("<html><body><h1>404 Not Found</h1></body></html>\r\n".encode())
        connectionSocket.close()

serverSocket.close() 
sys.exit() 
