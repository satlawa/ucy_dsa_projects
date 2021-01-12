#------------------------------------------------------#
#   problem 3 - Rearrange Array Digits
#------------------------------------------------------#

def mergesort(items):
    """
    Implementation of mergesort

    Args:
       items(list): Input List to be sorted
    Returns:
       (list): Sorted list
    """
    if len(items) <= 1:
        return items

    mid = len(items) // 2
    left = items[:mid]
    right = items[mid:]

    left = mergesort(left)
    right = mergesort(right)

    return merge(left, right)


def merge(left, right):
    """ Merge two lists into one, part of mergesort """
    merged = []
    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] > right[right_index]:
            merged.append(right[right_index])
            right_index += 1
        else:
            merged.append(left[left_index])
            left_index += 1

    merged += left[left_index:]
    merged += right[right_index:]

    return merged


def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """

    if len(input_list) < 2:
        return input_list

    sorted_list = mergesort(input_list)

    # check if the length of input_list is odd
    if len(sorted_list) % 2 == 1:
        odd = True
    else:
        odd = False

    # list holding the rearranged Array Elements
    sum_max = [0,0]

    # loop over every second index (i) and enumerate exponent (e)
    for e, i in enumerate(range(0, len(sorted_list), 2)):
        # find last element if the lenght of the list is odd
        if i == len(sorted_list)-1 and odd:
            sum_max[0] += sorted_list[i] * 10**e
        else:
            sum_max[1] += sorted_list[i] * 10**e
            sum_max[0] += sorted_list[i+1] * 10**e

    return sum_max


def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass array: {}  max_sum: {}".format(test_case[0], output))
    else:
        print("Fail")

# standard test cases
test_function([[1, 2, 3, 4, 5], [542, 31]])
# Pass array: [1, 2, 3, 4, 5]  max_sum: [542, 31]
test_function([[4, 6, 2, 5, 9, 8], [964, 852]])
# Pass array: [4, 6, 2, 5, 9, 8]  max_sum: [964, 852]
test_function([[1,1,6,1,7,8,1,1,9,7,2], [987211, 76111]])
# Pass array: [1,1,6,1,7,8,1,1,9,7,2]  max_sum: [987211, 76111]

# edge test cases
test_function([[0, 0, 0], [0, 0]])
# Pass array: [0, 0, 0]  max_sum: [0, 0]
test_function([[1, 1], [1, 1]])
# Pass array: [1, 1]  max_sum: [1, 1]
test_function([[2], [2]])
# Pass array: [2]  max_sum: [2]
test_function([[], []])
# Pass array: []  max_sum: []
