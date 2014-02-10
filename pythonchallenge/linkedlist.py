from urllib2 import urlopen
url_formatter='http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=%s'
next='46059'

while True:
    uo=urlopen(url_formatter % next)
    msg=uo.read()
    next=msg[msg.rfind(' ')+1:]
    print
    print msg
    #break