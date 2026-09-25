#!/usr/bin/bash python3
number = input("Give me a number: ")
number_float = float(number)
#number_int = int(number_float)
#number_float_str = str(number_float)
#number_int_str = str(number_int)
if str(number_float) == number:
	print("This number is a decimal")
else:
	print("This number is an integer")
