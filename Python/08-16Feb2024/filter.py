#filter
#it can filter the data by the given condition

namber = [1,2,3,4,5,6,7,8,9,10]
evennumber = list(filter(lambda x: x%2==0, namber))
print(evennumber)