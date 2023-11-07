'''try:
    x = "ABC"
    print("My value is ", x)
    print("My value is ", y)
except Exception as e:
    print("Something went wrong please check your code again",e)'''

'''try:
 mylist=[2,4,6,8]
 print((mylist)[4])
except Exception as e:
    print("Something having issue :",e)'''

try:
    import os
    x = "MOIZ"
    y = "KHAN"
    print("My value is", x)
    print("My value is ", y)
    mylist = [2,4,5,6]
    print(mylist[3])
    os.system('hostname')
    a = int(input("Enter the number:"))
    b = int(input("Enter the number:"))

    result = a / b
    print(result)
except NameError:
    print("Something having an issue in your variable, Please check your variable is define or not")
except IndexError:
    print("Something went wrong ! Please check your data structure index value within range or not")
except ModuleNotFoundError:
    print("Please Check Module name or module variable in your machine")
except ValueError:
    print("value error occur ! You cannot divide values with strings")
except Exception as e:
    print("Something having an issue in your code")
else:
    print("This is a else statement")
finally:
    print("This statements is run always\n doesnt matter what the situation are")