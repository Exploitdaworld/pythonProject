import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage
from email import encoders
from datetime import *

day=date.today()
time=datetime.now()

my_custom=day.strftime('%B %d %Y')
current_time=time.strftime('%I:%M:%S %p')

filename=r'C:\Users\moiza\PycharmProjects\pythonProject\damnfile.csv'
mylogo=r'C:\Users\moiza\PycharmProjects\pythonProject\alnafi-220930-222108.jpg'
msg=MIMEMultipart()

mymail='moiz.ahmed223190@gmail.com'
password='x-x-x-x-x-x-x'
msg['Subject']=f'Citrix Connection Alert {my_custom} {current_time}'
msg['From']=mymail
msg['To']=mymail
msg['Cc']='talktomoiz07@gmail.com'

body="""
<html><p> <b> <i>Asalammualikum Team,<br> we were testing SMTP as HTML Format via Python Script<b><i><br> <img src="cid:alogo" width='100' height='50'</p></html>"""
msg.attach(MIMEText(body,'html'))

#Logo Section
filelogo=open(mylogo,'rb')
msgIMAGE=MIMEImage(filelogo.read())
filelogo.close()
msgIMAGE.add_header('Content-ID','<alogo>')
msg.attach(msgIMAGE)

#attachment section
attachment=open(filename,'rb')
part=MIMEBase('application','octect-stream')
part.set_payload((attachment).read())
encoders.encode_base64(part)
part.add_header('Content-Disposition','attachment; filename=%s' %filename)


connection=smtplib.SMTP('smtp.gmail.com')
connection.starttls()

connection.login(user=mymail,password=password)
connection.send_message(msg)
connection.close()
print("Mail has been sent")
