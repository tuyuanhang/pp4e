#!usr/local/bin/python

import smtplib, sys, email.utils, mailconfig

mailserver = mailconfig.smtpservername

From = input('From? ').strip()
To = input('To? ').strip()
Tos = To.split(';')
Subj = input('Subj? ').strip()
Date = email.utils.formatdate()

text = ('From: %s\nTo: %s\nDate: %s\nSubject: %s\n\n' %(From, To, Date, Subj))

print('Type message text, end with line=[Ctrl+d(Unix), Ctrl+z(Windows)]')
while True:
    line = sys.stdin.readline()
    if not line:
        break
    #if line[:4] == 'From':
    #line = '>' + line
        text += line
        
print('Connecting...')
server = smtplib.SMTP(mailserver)
failed = server.sendmail(From, Tos, text)
server.quit()
if failed:
    print('Failed recipients:', failed)
else:
    print('No errors.')
print('Bye.')
