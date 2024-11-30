import paramiko
hostname="172.23.79.49"
username='moiz'
password='x-x-x-x'

client= paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(hostname=hostname,username=username,password=password)

mysftp = client.open_sftp()
mysftp.chdir('/home/moiz/python-automation')
file=mysftp.open('file1.txt')
print(file.read())
mysftp.close()
client.close()