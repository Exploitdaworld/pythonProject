mylist=[1,'Moiz','Ahmed','Karachi']
mylist2=[2,'Ruhma','Khan','Islamabad']
myfinalist=[[1,'Moiz','Ahmed','Karachi'], [2,'Ruhma','Khan','Islamabad']]

import csv
with open('myfile.csv','w') as newfile:
    data_write=csv.writer(newfile)
    data_write.writerows(myfinalist)
