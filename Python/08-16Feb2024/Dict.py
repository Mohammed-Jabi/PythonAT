#Dict
#Dictionary is a collection of key-value pairs.
from collections import OrderedDict
my_dict = {}
print(my_dict)

my_dict = {1: 'Python', 2: 'Java', 3: 'Selenium'}
print(len(my_dict))
print(my_dict[1])

my_dict1 = my_dict.pop(2)
print(my_dict1)

my_dict2 = {"Bangalore": "Karnataka", "Mumbai": "Maharashtra", "Pune": "Maharashtra"}

for i,j in my_dict2.items():
    print(i,j)


od = OrderedDict()
od[1] = 'Python'
od[2] = 'Java'
od[3] = 'Selenium'
od[4] = 'C#'
print(od)

for i,j in od.items():
    if j == 'Java':
        print(i)