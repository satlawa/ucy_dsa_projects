#------------------------------------------------------#
#   problem 6 - Unsorted Integer Array
#------------------------------------------------------#

import random

def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
        ints(list): list of integers containing one or more integers
    Returns:
        min_int(int), max_int(int): Minimum and maximum value
    """
    # set min to the highest possible number: infinity
    min_int = float('inf')
    # set max to the smollest possible number: -infinity
    max_int = -float('inf')

    # loop over all numbers
    for i in ints:
        # if a number is smaller than than the smallest number up till now
        if i < min_int:
            # set it as the minimum
            min_int = i
        # if a number is higher than than the highest number up till now
        if i > max_int:
            # set it as the maximum
            max_int = i

    return min_int, max_int


# Standard test cases
l = [i for i in range(0, 10)]
random.shuffle(l)
# expected output: min:0, max:10
print ("Pass min:0, max:9" if ((0, 9) == get_min_max(l)) else "Fail min:0, max:9")

l = [i for i in range(8, 24)]
random.shuffle(l)
# expected output: min:0, max:10
print ("Pass min:8, max:23" if ((8, 23) == get_min_max(l)) else "Fail min:8, max:23")

l = [i for i in range(19, 39, 3)]
random.shuffle(l)
# expected output: min:0, max:10
print ("Pass min:19, max:37" if ((19, 37) == get_min_max(l)) else "Fail min:19, max:37")


## Edge tast cases
l = [i for i in range(9, 999999)]
random.shuffle(l)
# expected output: min:9, max:999999
print ("Pass min:9, max:999998" if ((9, 999998) == get_min_max(l)) else "Fail min:9, max:999998")

l = [i for i in range(-20, 21)]
random.shuffle(l)
# expected output: min:-20, max:20
print ("Pass min:-20, max:20" if ((-20, 20) == get_min_max(l)) else "Fail min:-20, max:20")

l = [i for i in range(-999999, -8)]
random.shuffle(l)
# expected output: min:-999999, max:-9
print ("Pass min:-999999, max:-9" if ((-999999, -9) == get_min_max(l)) else "Fail min:-999999, max:-9")
