import time
import socket
import sys

print("\nWelcome\n")
print("Verifying...\n")
time.sleep(1)

s = socket.socket()
host = socket.gethostname()
ip = socket.gethostbyname(host)
port = 2024
s.bind((host, port))
print(host, "(", ip, ")\n")
name = input(str("Enter your name: "))
           
s.listen(1)
print("\nWaiting...\n")
conn, addr = s.accept()
print("Received connection - ", addr[0], "(", addr[1], ")\n")

s_name = conn.recv(1024)
s_name = s_name.decode()
print(s_name, "has connected\nEnter [x] to leave\n")
conn.send(name.encode())

while True:
    message = input(str("Me : "))
    if message == "[x]":
        message = "Left chat room!"
        conn.send(message.encode())
        print("\n")
        break 
    conn.send(message.encode())
    message = conn.recv(1024)
    message = message.decode()
    print(s_name, ":", message)
