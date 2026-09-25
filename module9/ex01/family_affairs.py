#!/bin/bash python3

#import re

def find_the_redheads(x):
    y = list(filter(lambda item: item[1] == "red", x.items()))
    for i in range(0, len(y)):
        y[i] = y[i][0]
    return y


dupont_family = {
"florian": "red",
"marie": "blond",
"virginie": "brunette",
"david": "red",
"franck": "red"
}

#find_the_redheads(dupont_family)
print(find_the_redheads(dupont_family))