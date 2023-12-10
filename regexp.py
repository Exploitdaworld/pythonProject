import re

myword="My jboss server ip address is 192.168.1.8 \nMy Docker server ip address is 192.168.1.11 \n My broadcast addres is 255.255.255.255 \n My invalid address 192.168.1234.12345"
pattern=r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}"
#print(re.findall(pattern,myword))
myiter=(re.finditer(pattern,myword))

for i in myiter:
    print(type(i))