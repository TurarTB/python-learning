#!/bin/bash python3

import sys
import re

if len(sys.argv)-1 < 2:
	print("none")
elif (repeats := len(re.findall(sys.argv[1], sys.argv[2]))) == 0:
	print("none")
else: 
	print(repeats)

