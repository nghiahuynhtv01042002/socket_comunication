import socket
import time

count = 0
# Tạo một socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Lắng nghe các kết nối đến ở cổng 12345
# server_socket.bind(('127.0.0.1', 12345))
# server_socket.bind(('localhost', 12345))
server_socket.bind(('192.168.31.252', 12345))

server_socket.listen(5)

print("Server is listening...")

# Chấp nhận kết nối từ client
client_socket, addr = server_socket.accept()

# print(f"Connection from {addr} has been established.")
print("Connection from {} has been established.".format(addr))
# tạo hàm handle client ở đây
while True:
    # Nhận dữ liệu từ client
    data = client_socket.recv(1024).decode().strip()
    if not data:
        break
    # print(f"Received from client: {data} {count}")
    print("Received from client: {} {}".format(data,count))
    count +=1
 
    # Gửi dữ liệu lại cho client
    data_send = "" + data
    client_socket.send(data_send.encode())
    time.sleep(2)

# Đóng kết nối
client_socket.close()
server_socket.close()
