#!/bin/bash python3

import sys

def shrink():
    print(sys.argv[i][0:8])


def enlarge():
    n = 7 - len(sys.argv)
    print(sys.argv[i] + "Z"*n)

if len(sys.argv) == 1:
    print("none")
else:
    for i in range(1, len(sys.argv)):
        if len(sys.argv[i]) < 8:
            enlarge()
        elif len(sys.argv[i]) > 8:
            shrink()
        else:
            print(sys.argv[i])
        i += 1








