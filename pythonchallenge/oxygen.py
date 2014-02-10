from urllib2 import urlopen
from StringIO import StringIO
import Image
import ImageDraw

oxygen_address='http://www.pythonchallenge.com/pc/def/oxygen.png'

oxygen=StringIO(urlopen(oxygen_address).read())

im=Image.open(oxygen)


pixels = list(im.getdata())
msg=''
for e in range(0,im.size[0],7):
    current=pixels[45*im.size[0]+e][0]
    if pixels[45*im.size[0]+e][0]!=pixels[45*im.size[0]+e][1]:
        break
    msg+= chr(int(current))
print msg


for e in [105, 110, 116, 101, 103, 114, 105, 116, 121]:
    print chr(e),


#for e in range(0,im.size[0]*im.size[1],im.size[0])  :
#    p=pixels[e]
#    if p[0]==p[1]==p[2]:
#        print e/im.size[0]



#for e in range(im.size,5):
#    print str(im.getpixel(3,e))
    
#im.show()