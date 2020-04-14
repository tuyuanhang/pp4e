#!/usr/local/bin/python
"""
pymail mail command client
"""

import poplib, smtplib, email.utils, mailconfig
from email.parser import Parser
from email.message import Message
fetchEncoding = mailconfig.fetchEncoding

def decodeToUnicode(messageBytes, fetchEncoding=fetchEncoding):
    return [line.decode(fetchEncoding) for line in messageBytes]

def splitaddrs(field):
    pairs = email.utils.getaddresses([field]) #[(name,address)]
    return [email.utils.formataddr(pair) for pair in pairs] #[(name <address>)]

def inputmessage():
    import sys
    From = input('From? ').strip()
    To = input('To? ').strip()
    To = splitaddrs(To)
    Subj = input('Subj? ').strip()
    print('Type message text, end with line="."')
    text = ''
    while True:
        line = sys.stdin.readline()
        if line == '.\n': break
        text += line
    return From, To, Subj, text

def sendmessage():
    From, To, Subj, text = inputmessage()
    msg = Message()
    msg['From'] = From
    msg['To'] = ', '.join(To)
    msg['Subject'] = Subj
    msg['Date'] = email.utils.formatdate()
    msg.set_payload(text)
    server = smptlib.SMTP(mailconfig.smtpservername)
    try:
        failed = server.sendmail(From, To, str(msg))
    except:
        print('Error - send failed')
    else:
        if failed: print('Failed:', failed)

def connect(servername, user, passwd):
    print('Connecting...')
    server = poplib.POP3(servername)
    server.user(user)
    server.pass_(passwd)
    print(server.getwelcome())
    return server
    
