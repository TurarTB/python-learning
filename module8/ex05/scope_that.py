#!/bin/bash python3

def add_one(parameter):
    global variable
    print(parameter + 1)

variable = 1

print(variable)

add_one(variable)

print(variable)