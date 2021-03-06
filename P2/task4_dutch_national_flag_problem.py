## imports

def sort_012(input_list):
    """
    Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal.

    Args:
       input_list(list): List to be sorted
    """
    # variables for holding the count
    count_0 = 0
    count_1 = 0
    count_2 = 0

    # loop through list and count 0, 1 and 2
    for i in input_list:
        if i == 0:
            count_0 += 1
        elif i == 1:
            count_1 += 1
        elif i == 2:
            count_2 += 1
    # create list with the counts of 0 1 and 2
    return [0] * count_0 + [1] * count_1 + [2] * count_2

def test_function(test_case):
    sorted_array = sort_012(test_case)
    print(sorted_array)
    if sorted_array == sorted(test_case):
        print("Pass")
    else:
        print("Fail")


# Standard test cases
test_function([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2])
test_function([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1])
test_function([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2])
# Edge test cases
test_function([])
test_function([0, 0, 0, 0])
test_function([1, 1, 1, 0, 0, 0, 1, 1, 1])
test_function([2, 2, 0, 0, 0, 0, 2, 2, 2, 2, 0, 0, 2])
test_function([1, 1, 1, 1, 2, 2, 2, 2, 1, 1, 1])
