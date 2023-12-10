import paramiko
hostname="172.23.79.49"
username='moiz'
password='moiz85032'

client= paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(hostname=hostname,username=username,password=password)

mycmd='df -h'

stdin, stdout, stderr = client.exec_command(mycmd)

'''mycmdout =stdout.read().decode()
print(mycmdout)'''

mycmdout= stdout.readlines()

print(mycmdout)
for i in mycmdout[1:]:
    myvalue = (i.split()[4])
    full_size = myvalue.replace('%','')
    if int(full_size) >= 80:
        print(i.strip('\n'))