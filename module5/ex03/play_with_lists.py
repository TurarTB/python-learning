#!/usr/bin/bash python3

list_1 = [2, 8, 9, 48, 8, 22, -12, 2]
print(list_1)
list_2 = []
for x in list_1:
	x += 2
	if x > 5:
		list_2.append(x)
#list_2 = sorted(set(list_2), key=list_2.index)

print(set(list_2))