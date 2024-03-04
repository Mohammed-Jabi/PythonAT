#FileHandeling
#File Handeling is a way to store the data in a file
# and read the data from the file.

#There are 3 types of files:
#1. Text files
#2. Binary files
#3. JSON files

#Function -
#open() - open the file

#Modes of file handeling:
#1. Read mode 'r'
#2. Write mode 'w'
#3. Append mode 'a'
#4. Binary mode 'b'  ex: binary file
#5. For updating 'r+'

#Closing the file
import csv
import pandas as pd

file = open('file.txt', 'r')
content = file.read()
print(content)

with open('data.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    for row in readCSV:
        print(row)
        print(row[0])
        print(row[0], row[1])

df = pd.read_csv('data.csv')
print(df)

testdata = [
    ['Name', 'Age', 'City'],
    ['John', '25', 'New York'],
    ['Anna', '22', 'London'],
    ['Sam', '32', 'Paris']
]

with open('mydata.csv','w') as file:
    writer = csv.writer(file)
    # for row in testdata:
    #     writer.writerow(row)
    writer.writerows(testdata)