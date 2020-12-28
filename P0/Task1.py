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
TASK 1:
How many different telephone numbers are there in the records?
Print a message:
"There are <count> different telephone numbers in the records."
"""

def get_tel_num(input_list):
    """ extract all unique telephone numbers from provided lists """
    tel_num = set()
    for recs in input_list:
        for rec in recs:
            # loop through both columns with tel numbers
            for i in range(2):
                tel_num.add(rec[i])
    return tel_num

count_tel_num = len(get_tel_num([texts, calls]))

print("There are {} different telephone numbers in the records.".format(count_tel_num))
