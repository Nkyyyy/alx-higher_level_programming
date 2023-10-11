#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0

    digit = 0
    delit = 0

    for i in my_list:
        digit += i[0] * i[1]
        delit += i[1]

    return (digit / delit)
