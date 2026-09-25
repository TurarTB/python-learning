#!/bin/bash python3

import sys

if len(sys.argv) - 1 != 1:
	print("none")
# x is a user input to compare with the parameter
elif (x := input("What was the parameter? ")) == sys.argv[1]:
	print("Good job!")
else:
	print("Nope, sorry...")



