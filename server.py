from socket import * 
import matplotlib.pyplot as plt
import random
import time

serverPort = 12001 
serverSocket = socket(AF_INET, SOCK_STREAM) 
serverSocket.bind(('', serverPort)) 
serverSocket.listen(1) 
print("Sunucu almak icin hazir")

plt.ion()

data = []

time_data = []

fig, ax = plt.subplots()

connectionSocket, addr = serverSocket.accept()

while True: 
    recv_data = connectionSocket.recv(1)
    if not recv_data:
        break
    number = int.from_bytes(recv_data, byteorder='big')

    data.append(number)
    time_data.append(len(data) - 1)

    ax.clear()
    ax.plot(time_data, data, marker = 'o', linestyle='-', color='b')
    ax.set_title("Random sayilarin cizimi")
    ax.set_xlabel("Time")
    ax.set_ylabel("Random Number")
    ax.set_ylim(0, 100)
    plt.draw()
    plt.pause(0.1)
    
plt.ioff()
plt.show()

connectionSocket.close()