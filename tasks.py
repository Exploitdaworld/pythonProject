'''salary = [
['moiz', 20000],
['Ruhma', 30000],
['kashif', 25000],
['Katrina', 50000],
['sarah', 27000]
]
max_salary = [i for i in salary if i[1] >= 30000]
print(max_salary)'''

'''even_num = []
for i in range(20):
    if i%2 == 0:
        even_num.append(i)
        print(even_num)'''

salary ={'Abdeali': 20000,'Ali' :40000,'Kazim': 25000,'Katrina': 50000,'sarah': 27000}
new_dict = {k:v for (k, v) in salary.items() if v >= 20000 if v <= 30000}
print(new_dict)
