#!/bin/bash python3

def array_of_names(x):
    first_names = list(x.keys())
    last_names = list(x.values())
    full_name_list = []
    for i in range(0, len(first_names)):
        first_names_cap = first_names[i].capitalize()
        last_names_cap = last_names[i].capitalize()
        full_name = first_names_cap + " " + last_names_cap
        full_name_list.append(full_name)
    return full_name_list
    

persons = {
"jean": "valjean",
"grace": "hopper",
"xavier": "niel",
"fifi": "brindacier"
}
#print(array_of_names(persons))
print(array_of_names(persons))