'''import time
print("This is sample time example")
time.sleep(2)
print("This is sample time example1")
time.sleep(4.3)
print("This is sample time example2")'''
import time

'''from datetime import datetime
current=datetime.now()
print(current)
print(type(current))

year=current.strftime('%Y')
print("My Year is" , year)
print(type(year))

date_time=current.strftime('%d/%m/%Y %H:%M:%S')
print(date_time)
custom_date=datetime.strftime(current, "%Y/%m/%d")
print(custom_date)
print(type(custom_date))
'''
mygmt=time.gmtime()
print(mygmt)
print(type(mygmt))

tuple1=time.localtime()
print(tuple1)
print(type(tuple1))

time_str=time.strftime("%m/%d/%Y, %H:%M:%S")
print(time_str)
