#!/bin/bash python3

def average(x):
    score = list(x.values())
    total_score = 0
    for i in range(0, len(score)):
        total_score += score[i]
    average_score = total_score / len(score)
    return average_score


class_3B = {
"marine": 18,
"jean": 15,
"coline": 8,
"luc": 9
}
class_3C = {
"quentin": 17,
"julie": 15,
"marc": 8,
"stephanie": 13
}

#average(class_3B)
print(f"Average for class 3B: {average(class_3B)}.")
print(f"Average for class 3C: {average(class_3C)}.")