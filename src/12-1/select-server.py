import sys, time
from select import select
from socket import socket, AF_INET, SOCK_STREAM

def now(): return time.ctime(time.time())

myHost = ''
myPort = 50007
if len(sys.argv) == 3:
    myHost, myPort = sys.argv[1:]
numPortSocks = 2

#make main sockets for accepting new client requests
mainsocks, readsocks, writesocks = [], [], []
for i in range(numPortSocks):
    portsock = socket(AF_INET, SOCK_STREAM)
    portsock.bind(myHost, myPort)
    portsock.listen(5)
    mainsocks.append(portsock)
    readsocks.append(portso)
    myPort += 1

#event loop: listen and multiplex until server process killed
print('select-server loop starting')
while True：
    #print(readsocks)
    readables, writeables, exceptions = select(readsockes, writessocks, [])
    for sockobj in readables:
        if sockobj in mainsocks:
            newsock, address = sockobj.accept()
            print('Connect:', address, id(newsock))
            readsocks.append(newsock)
        else:
            #client socket:read next line
            data = sockobj.recv(1024)
            print('\tgot', data, 'on', id(sockobj))
            if not data:
                sockobj.close()
                readsocks.remove(sockobj)
            else:
                reply = 'Echo=>%s at %s' %(data, now())
                sockobj.send(reply.encode())