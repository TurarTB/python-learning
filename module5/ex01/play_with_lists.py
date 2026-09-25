#!/usr/bin/bash python3

# list_1 = [2, 8, 9, 48, 8, 22, -12, 2]
# print(f"Original list: {list_1}")
# for i in range(len(list_1)):
# 	list_1[i] += 2
# print(f"New list: {list_1}")

	
list_1 = [2, 8, 9, 48, 8, 22, -12, 2]
print(f"Original list: {list_1}")
list_2 = []
for x in list_1:
	x += 2
	list_2.append(x)
print(f"New list: {list_2}")