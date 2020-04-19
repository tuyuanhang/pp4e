import sys
from urllib.request import urlopen
showline = 16
try:
    servername, filename = sys.argv[1:]
except:
    servername, filename = 'learning-python.com', '/index.html'

remoteaddr = 'http://%s%s' %(servername, filename)
print(remoteaddr)
remotefile = urlopen(remoteaddr)
remotedata = remotefile.readline()
remotefile.close()
for line in remotedata[:showline]: print(line)