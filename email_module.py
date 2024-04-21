import smtplib
from email.message import EmailMessage
mymail='moiz.ahmed223190@gmail.com'
password='x-x-x-x-x-x-x'
connection=smtplib.SMTP('smtp.gmail.com')
connection.starttls() #Transport Layer security

msg=EmailMessage()
msg['Subject']='This is a Testing prompt from python'
msg['From']= mymail
msg['To']= mymail

'''msg.set_content("Asalamualikum team ! We are testing our first SMTP Server through Python")

#This is file attachment section
with open('damnfile.csv','rb') as file:
    attach=file.read()
    file_name=file.name

msg.add_attachment(attach,maintype='application',subtype='octect-stream',filename=file_name)'''
msg.add_alternative("""
<html><b>Asalam-mu-Alaikum Team! we were trying to use bold characters messages" </b></html>""",subtype='html')
connection.login(user=mymail,password=password)
connection.send_message(msg)
connection.close()
print("Mail has been sent")
