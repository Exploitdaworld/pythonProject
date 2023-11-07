
'''def mycode(server, ip, os):
    print(f"Server is : {server}\n IP is {ip} \n OS is {os}")

mycode("Cisco","192.168.12.2","Linux")'''

def mycode(**mydata):
    for k,v in mydata.items():
        print(k,v)
mydict={'Server':'Cisco', 'IP':'192.186.37.38', 'OS':'Linux'}
mycode(**mydict)

'''def mycode(*mydata):
    for i in mydata:
        print(type(i))
        return None
mycode(4,5,6)'''