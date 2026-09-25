#!/usr/bin/bash python3

import math

number = input("Give me a number: ")
number_float = float(number)
rounded_up = math.ceil(number_float)
print(rounded_up)