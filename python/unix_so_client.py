#!/app/python/python2/bin/python
# -*- coding: utf-8 -*
#
#1.创建一个UNIX domain socket
#2.fork一个子进程作为domain socket server
#3.与之通信
#
import socket,os,sys
import fcntl

s = socket.socket(socket.AF_UNIX,socket.SOCK_STREAM)
parent_pid = os.getpid()
pipe_name = "/app/src/python_samples/tmp/%d.sock"%parent_pid
s.bind(pipe_name)
s.listen(1)
fd = s.fileno()


new_pid = os.fork()
if new_pid==0:
    #child process
    print "child:",os.getpid()
    os.dup2(fd,0)      
    #s.close()
    flags = fcntl.fcntl(fd,fcntl.F_GETFD)
    flags |= fcntl.FD_CLOEXEC
    fcntl.fcntl(fd,fcntl.F_SETFD,flags)
    os.execve("/app/src/python_samples/unix_so_server.py",[],{})
    #new_fd = os.dup(fd)
    """sock = socket.fromfd(fd, socket.AF_INET,socket.SOCK_STREAM)
    conn,addr = sock.accept()
    while 1:
        data = conn.recv(1024)
        if not data:
            break
        else:
            #conn.send("Fine!")
            print "child Recieved:",data
    conn.close()"""

    
    
else:
    print "parent",parent_pid
    from time import sleep
    sleep(5)
    print "parent connect" 
    sock = socket.socket(socket.AF_UNIX,socket.SOCK_STREAM)
    sock.connect(pipe_name)
    sock.send("Hello World")
    data = sock.recv(1024)
    print "parent Recieved:",data
    sock.close()
    s.close()



