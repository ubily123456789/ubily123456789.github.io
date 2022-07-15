import socket
from _thread import *
import sys

server = "192.168.1.56"
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server, port))
except socket.error as e:
    str(e)

s.listen(4)
print("wating for conection sever started")

def threaded_client(conn):

    reply = ""
    for i in range(400):
        try:
            data = conn.recv(2048)
            reply = data.decode("utf-8")

            if not data:
                print("disconected")
                break

            else:
                print("received: ", reply)
                print("sending: ", reply)

            conn.sendall(str.encode(reply))

        except:
            break

for i in range(2):
    conn, addr = s.accept()
    print("connected to:", addr)

    start_new_thread(threaded_client, (conn))
