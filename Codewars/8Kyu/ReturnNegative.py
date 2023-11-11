#In this simple assignment you are given a number and have to make it negative. 
#But maybe the number is already negative?


def make_negative( number ):
    #if number is positive, return it as a negative
    if number >= 1:
        return number *- 1
    #if number is negative, return as is
    elif number <= 0:
        return number
    #if number is neither positive or negative (zero), return 0
    else:
        return 0