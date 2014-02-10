from urllib2 import urlopen
from pickle import loads
peak_address='http://www.pythonchallenge.com/pc/def/banner.p'
peak=urlopen(peak_address).read()
banner=''
for e in loads(peak):
    banner+='\n'
    for f in e:
         banner+=f[0]*f[1]
print banner