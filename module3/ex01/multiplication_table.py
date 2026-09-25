#!/usr/bin/env python3
print("Enter a number")
number = int(input())
i = 0
while i < 10:
	mult = i * number
	print(f"{i} x {number} = {mult}")
	i += 1