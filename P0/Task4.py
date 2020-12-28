"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

def find_possible_marketers(input_list):
    """
    Function for finding possible marketers from a calls and a texts list.

    Args:
        input_list(list): list containing two lists: calls and texts
    Return:
        possible_marketers(set): set of possible marketers
    """
    calls, texts = input_list
    # set to add possible non marketers
    non_marketers = set()
    # loop all rows in texts
    for record in texts:
        # both columns
        for i in range(2):
            non_marketers.add(record[i])
    # loop all rows in calls
    for record in calls:
        non_marketers.add(record[1])
    # set to add possible marketers
    possible_marketers = set()
    for record in calls:
        if not(record[0] in non_marketers):
            possible_marketers.add(record[0])

    return possible_marketers

possible_marketers = find_possible_marketers([calls, texts])

print("These numbers could be telemarketers: {}".format(possible_marketers))
