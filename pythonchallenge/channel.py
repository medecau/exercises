from urllib import urlretrieve
from zipfile import ZipFile
zip_address='http://www.pythonchallenge.com/pc/def/channel.zip'
file_name, headers = urlretrieve(zip_address)

zip_file=ZipFile(file_name)
info_list=zip_file.infolist()
print zip_file.comment
next='90052.txt'
while True:
    print zip_file.getinfo(next).comment,
    msg=zip_file.read(next)
    next=msg[msg.rfind(' ')+1:]+'.txt'
    
