#!/bin/bash python3

import sys

if len(sys.argv) == 1:
    print("none")

else:
    for i in range(1, len(sys.argv)):
        if sys.argv[i].find("ism") != -1:
            continue
        print(sys.argv[i] + ("ism"))