'''file=open('moiz.txt')
data=file.read()
print(data)
file.close()'''

'''with open('myfile.txt', mode='a') as file:
    file.write("Hello ")'''

mydata=['Python', 'Python2' , 'Python3']
with open("newfile.txt", mode='w') as file:
    for i in mydata:
        file.write(i+"\n")