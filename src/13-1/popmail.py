#!/usr/local/bin/python

import poplib, getpass, sys, mailconfig

mailserver = mailconfig.popservername
mailuser = mailconfig.popusername
mailpasswd = getpass.getpass('Password for %s?' %mailserver)

print('Connecting...')
server = poplib.POP3(mailserver)
server.user(mailuser)
server.pass_(mailpasswd)

try:
    print(server.getwelcome())
    msgCount, msgBytes = server.stat()
    print('There are', msgCount, 'mail message in', msgBytes,  'bytes')
    print(server.list())
    print('-' * 80)
    input('[Press Enter key]')
    
    for i in range(msgCount):
        hdr, message, octets = server.retr(i + 1)
        for line in message: print(line.decode())
        print('-' * 80)
        if  i < msgCount - 1:
            input('[Press Enter key]')
            
finally:
    server.quit()
    
print('Bye.')
            