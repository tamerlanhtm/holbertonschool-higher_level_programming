#!/usr/bin/python3
def uniq_add(my_list=[]):
    unique_values = []
    total = 0
    for num in my_list:
        if num not in unique_values:
            unique_values.append(num)
            total += num
    return total
