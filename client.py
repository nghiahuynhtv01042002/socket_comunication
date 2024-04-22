import socket
import time
# Tạo một socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Kết nối tới server
client_socket.connect(('192.168.31.252', 12345))
count = 0
while True:
    # Nhập dữ liệu từ người dùng
    message = "I Am TXN\n"
    # Gửi dữ liệu tới server
    client_socket.send(message.encode())
    
    # Nhận dữ liệu từ server
    data = client_socket.recv(1024).decode()
    # print(f"Received from server: {data} {count}")
    print("Received from server: {} {}".format(data,count))
    count+=1
    time.sleep(2)

# Đóng kết nối
client_socket.close()
