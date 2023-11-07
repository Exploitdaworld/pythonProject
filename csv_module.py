import csv

mypath=r"C:\Users\moiza\PycharmProjects\pythonProject\serverhealth.csv"
mylist=[12,'10.226.17.104','UBUNTU','d6:60:7b:6e:f6:8c','25 GB']
with open(mypath, 'w') as datafile:
    data_write=csv.writer(datafile)
    data_write.writerow(mylist)
'''data=csv.reader(datafile, delimiter='.')
    for each in data:
        print(each)'''