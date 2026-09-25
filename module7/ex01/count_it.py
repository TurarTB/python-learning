#!/bin/bash python3

import sys

if (x := len(sys.argv)-1) == 0:
    print("none")
else:
    print(f"parameters: {x}")
    for i in range(1, len(sys.argv)):
        print(f"{sys.argv[i]}: {len(sys.argv[i])}")
        i += 1