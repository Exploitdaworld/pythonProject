'''def mycode(moiz,ruhma):
    result=moiz+ruhma
    return result

print(mycode(29,39)) '''

'''result=lambda moiz,ruhma: moiz if (moiz >= ruhma) else ruhma
print(result(10,50))'''

import os
def mycode():
    print("This is my code function")
print(os.listdir(os.getcwd()))
print("My global print")