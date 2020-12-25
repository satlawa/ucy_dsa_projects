## imports

def sqrt(number):
    """
    Calculate the floored square root of a number using the binary search algorithm

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """

    if (number == 0) or (number == 1):
        return number

    elif (number < 0) or (number is None):
        return None

    else:
        # set lower and upper bound for searching
        lower_bound = 1
        upper_bound = number // 2 + 1

        # loop as long
        while lower_bound <= upper_bound:
            # estimate square root
            mid_elem = (lower_bound + upper_bound) // 2
            # square estimate for comparison
            est_number = mid_elem * mid_elem

            # found the element
            if number == est_number:
                return mid_elem
            # the target is less than mid element
            elif number < est_number:
                # search in the left half
                upper_bound = mid_elem - 1
            #  the target is greater than mid element
            else:
                # search in the right half
                lower_bound = mid_elem + 1
                # in case it is the last element
                sqrt_int = mid_elem

    return sqrt_int


# standard tests
print ("Pass sqrt(9)" if  (3 == sqrt(9)) else "Fail")
print ("Pass sqrt(16)" if  (4 == sqrt(16)) else "Fail")
print ("Pass sqrt(27)" if  (5 == sqrt(27)) else "Fail")
print ("Pass sqrt(27)" if  (5 == sqrt(27)) else "Fail")
# edge cases
print ("Pass sqrt(0)" if  (0 == sqrt(1)) else "Fail")
print ("Pass sqrt(1)" if  (1 == sqrt(1)) else "Fail")
print ("Pass sqrt(-10)" if  (None == sqrt(-10)) else "Fail")
print ("Pass sqrt(None)" if  (None == sqrt(None)) else "Fail")
