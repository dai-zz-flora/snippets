#!/app/python/python2/bin/python
import socket,os,sys


print "child stdin:",sys.stdin.fileno()

sock = socket.fromfd(sys.stdin.fileno(), socket.AF_INET,socket.SOCK_STREAM)
conn,addr = sock.accept()
while 1:
    data = conn.recv(1024)
    if not data:
        break
    else:
        conn.send("Fine!")
        print "child Recieved:",data
conn.close()
sock.close()

