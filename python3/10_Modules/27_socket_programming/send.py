#!/usr/bin/python
import socket
import sys

# creating a socket

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error as error:
    print(f"Failed to create a socket. {repr(error)}")
    sys.exit()

print("socket created")

host = "www.google.com"
port = 80

try:
    remote_ip = socket.gethostbyname(host)
except Exception:
    print("Hostname could not be resolved.exiting")
    sys.exit()

print("Ip address of " + host + " is " + remote_ip)

print("connecting to the server \n")

s.connect((remote_ip, port))

print("Socket Connected to " + host + " on ip " + remote_ip)

# sending a data outside
# message = input("enter the message you want to pass on: \n")
message = "GET / HTTP/1.1\r\n\r\n"

try:
    s.sendall(message)
except socket.error:
    print("send failed")
    sys.exit()

print("Message sending succesfully")

# receiving the data from system.
reply = s.recv(4096)

print(reply)
