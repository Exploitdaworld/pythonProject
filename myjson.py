import json

jsonfile=r"C:\Users\moiza\PycharmProjects\pythonProject\os.json"

with open(jsonfile, "r") as jf:
    my_dict=json.load(jf)
    #print(my_dict)

'''for i in my_dict:
    #print(f"My Dictionary is {i}")
    for k,v in i.items():
        if v=='Ubuntu':
            print(f'My Ubuntu version is : {my_dict[1]["Version"]}')'''

for i in my_dict:
    for k,v in i.items():
        if v == "Ubuntu":
            print("My Ubuntu version is ", i["Version"])
        if v == "CentOs":
            print("My CentOs version is ", i["Version"])