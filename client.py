import socket
import time
# create socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# conect to server
client_socket.connect(('192.168.207.70', 12345))
count = 0
while True:
    # enter message
    message = "I Am TXN\n"
    # send data to server
    client_socket.send(message.encode())
    
    # recieve data from server
    data = client_socket.recv(1024).decode()
    # print(f"Received from server: {data} {count}")
    print("Received from server: {} {}".format(data,count))
    count+=1
    time.sleep(2)

#close conection
client_socket.close()
