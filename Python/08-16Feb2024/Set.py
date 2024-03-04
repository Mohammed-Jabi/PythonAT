#Set
#Set is a collection of unique elements
set1 = {1,2,3,4,5,6,7,8,9,10}
print(set1)

set1 = {1,2,3,4,5,6,7,8,9,10}
set2 = {2,4,6,8,10,12,14,16,18,20}
my_set = set1.union(set2)
print(my_set)
my_set = set1.intersection(set2)
print(my_set)
my_set = set1.difference(set2)
print(my_set)
my_set = set1.issubset(set2)
print(my_set)