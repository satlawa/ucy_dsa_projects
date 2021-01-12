#------------------------------------------------------#
#   problem 2 - Search in a Rotated Sorted Array
#------------------------------------------------------#

def find_pivot(array):
    '''Find pivot index in Rotated Sorted Array

    args:
      array(list): a sorted array of items of the same type

    returns:
      int: the index of the pivot
      -1: if the pivot is not found
    '''
    pivot = -1
    start_index = 0
    end_index = len(array) - 1

    while start_index <= end_index:
        mid_index = (start_index + end_index)//2        # integer division in Python 3

        mid_element = array[mid_index]

        if array[start_index] <= array[end_index]:                       # we have found the element
            return start_index

        elif array[start_index] <= array[mid_index]:                      # the target is less than mid element
            start_index = mid_index + 1                   # we will only search in the left half

        elif array[mid_index] <= array[end_index]:
            end_index = mid_index

        else:                                           # the target is greater than mid element
            start_index = mid_element + 1               # we will search only in the right half

    return pivot


def binary_search(array, target, start_index, end_index):
    '''Binary search algorithm using iteration

    args:
      array(list): a sorted array of items
      target(int): the element you're searching for
      start_index(int): start index for the serarch
      end_index(int): end index for the serarch

    returns:
      int: the index of the target, if found, in the source
      -1: if the target is not found
    '''

    while start_index <= end_index:
        mid_index = (start_index + end_index)//2        # integer division in Python 3

        mid_element = array[mid_index]

        if target == mid_element:                       # we have found the element
            return mid_index

        elif target < mid_element:                      # the target is less than mid element
            end_index = mid_index - 1                   # we will only search in the left half

        else:                                           # the target is greater than mid element
            start_index = mid_index + 1               # we will search only in the right half

    return -1


def rotated_array_search(input_list, number):
    """
    Find the index by searching in a rotated sorted array

    Args:
       input_list(list), number(int): Input array to search and the target
    Returns:
       int: Index or -1 (if not found)
    """

    if input_list is None or not input_list or number is None:
        return -1

    pivot_index = find_pivot(input_list)

    if number <= input_list[-1]:
        start_index = pivot_index
        end_index = len(input_list)

    elif number > input_list[-1]:
        start_index = 0
        end_index = pivot_index

    index = binary_search(input_list, number, start_index, end_index)

    return index


def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1

def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass array: {}  value: {}".format(input_list, number))
    else:
        print("Fail")

# Standard test cases
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
# Pass array: [6, 7, 8, 9, 10, 1, 2, 3, 4]  value: 6
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
# Pass array: [6, 7, 8, 9, 10, 1, 2, 3, 4]  value: 1
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
# Pass array: [6, 7, 8, 1, 2, 3, 4]  value: 8
test_function([[6, 7, 8, 1, 2, 3, 4], 1])
# Pass array: [6, 7, 8, 1, 2, 3, 4]  value: 1
test_function([[6, 7, 8, 1, 2, 3, 4], 10])
# Pass array: [6, 7, 8, 1, 2, 3, 4]  value: 10

# Edge test cases
test_function([[0], 0])
# Pass array: [0]  value: 0
test_function([[], -1])
# Pass array: []  value: -1
