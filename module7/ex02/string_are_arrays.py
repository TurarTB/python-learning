#!/bin/bash python3

import sys
import re

if len(sys.argv)-1 != 1:
    print("none")
elif (x := len(re.findall("z", sys.argv[1]))) == 0:
    print("none")
else:
    print("z"*x)