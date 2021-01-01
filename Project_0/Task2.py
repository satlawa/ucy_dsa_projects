"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during
September 2016.".
"""

def get_tel_num_max_time(calls):
    """
    Function for finding the telephone number that spent the longest time on the phone.

    Args:
        calls(list): list containing call records
    Return:
        max_len(tuple): tuple containing the telephone number and the time spend on
        the phone from the telephone number that spent the longest time on the phone.
    """
    # dictionary for keeping track of the time of every tel number
    tel_nums = {}
    # loop all records
    for record in calls:
        # loop both columns
        for i in range(2):
            # if key already exists summ values
            if record[i] in tel_nums:
                tel_nums[record[i]] += int(record[3])
            # key does not exist create key with value
            else:
                tel_nums[record[i]] = int(record[3])
    # find tel number with max length
    max_len = ("0",0)
    for tel_num, length in tel_nums.items():
        if length > max_len[1]:
            max_len = (tel_num, length)

    return max_len

tel_num, lenght = get_tel_num_max_time(calls)

print("{} spent the longest time, {} seconds, on the phone during September 2016."\
.format(tel_num, lenght))
