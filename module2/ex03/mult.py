#!/usr/bin/env python3
print("Enter the first number: ")
number_1 = int(input())
print("Enter the second number: ")
number_2 = int(input())
mult = number_1 * number_2
print(f"{number_1} x {number_2} = {mult}")
if mult > 0:
	print("The result is positive.")
elif mult < 0:
	print("the result is negative")
else:
	print("The result is positive and negative.")