from socket import *
import random
import time

serverName = 'localhost'
serverPort = 12001 

clientSocket = socket(AF_INET, SOCK_STREAM) 
clientSocket.connect((serverName, serverPort)) 

while True:
    random_number = random.randint(1, 100)
    clientSocket.send(random_number.to_bytes(1, byteorder='big'))
    time.sleep(1)

clientSocket.close()