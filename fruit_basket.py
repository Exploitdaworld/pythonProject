import json
fruitmarket=r"C:\Users\moiza\PycharmProjects\pythonProject\Fruit_shelf.json"

with open(fruitmarket,"r") as fm:
    myfruits=json.load(fm)
print(myfruits)

fav_fruits=[]
for i in myfruits:
    if i['price'] >=1:
        total_count=(len(i.keys()))
        fav_fruits.append(i['name'])
print(f"We have our Favorite {fav_fruits} in our basket")
print(f"Total We have {total_count} Fruits in our basket")