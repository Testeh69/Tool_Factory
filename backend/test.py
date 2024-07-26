import socket
import time


address_ip = "169.254.215.36"
port = 29999
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
    client_socket.connect((address_ip, port))
    client_socket.send("power on\n".encode())
    time.sleep(5)
    client_socket.send("brake release\n".encode())
    time.sleep(5)