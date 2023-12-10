import mysql.connector
from datetime import *

time=datetime.now()
mycustom = time.strftime("%y-%m-%d %H:%M:%S")
mydb= mysql.connector.connect(host="172.23.79.49",user="mysql_user",password="test123",database="alnafi")

# mysql connection object create
cur = mydb.cursor()

#Fetching data
#sql = ''' select * from trainer_details '''
sql = " insert into trainer_details (fname,lname,desig,username,password,salary,datetime) values (%s,%s,%s,%s,%s,%s,%s) "
data = ('Bakhtawar','Ali','Engineer','Bakhtawar','Ali123','70000',mycustom)


#Executing
cur.execute(sql,data)
'''result = cur.fetchall()
for data in result:
    print(data)'''
mydb.commit()
mydb.close()

