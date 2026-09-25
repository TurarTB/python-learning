#!/bin/bash python3

import sys

def downcase_it():
    if len(sys.argv) <= 1:
        print("none")
    else:
        for i in range(1, len(sys.argv)):
            print(sys.argv[i].lower())
            i += 1

downcase_it()