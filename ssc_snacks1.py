#!/usr/bin/env python
from csv import reader
import random
opened_file = open('ssc_snacks.csv')
read_file = reader(opened_file)
data = list(read_file)
data = data[1:]

name1 = []
count1 = []
for row in data:
	name = str(row[0])
	name1.append(name)
	count = int(row[1])
	count1.append(count)
max1 = max(count1)
max2 = (max1 - 1)
max3 = (max2 - 1)
max4 = (max3 - 1)
print(max1)
print(name1)
print(count1)

list1 = []
list2 = []
list3 = []
list4 = []
list5 = []
for row in data:
        name = str(row[0])
	count = int(row[1])
	if max1 == int(count):
	   	list1.append(name)
	elif max2 == int(count):
		list2.append(name)
	elif max3 == int(count):
		list3.append(name)
	elif max4 == int(count):
		list4.append(name) 
	else:
		list5.append(name)
print(list1)
print(list2)
print(list3)
print(list4)
print(list5)

a = random.choice(list2)
print(a)
len1 = len(list1)
len2 = len(list2)
len3 = len(list3)
len4 = len(list4)
len5 = len(list5)

print(len1)
print(len2)
print(len3)
print(len4)
print(len5)

if len5 != 0:
	a = random.choice(list5)
	print(a)
elif len4 != 0:
        a = random.choice(list4)
	print(a)
elif len3 != 0:
	a = random.choice(list3)
	print(a)
elif len2 != 0:
	a = random.choice(list2)
	print(a)
elif len1 != 0:
        a = random.choice(list1)
	print(a)
else:
	print("some bug in program")

print(a)
