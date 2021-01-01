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
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore.
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""

def bangladore_calls(calls):
    """
    Find all of the area codes and mobile prefixes called by people
    in Bangalore.

    Args:
        calls(list):
    Return:
        codes(list): sorted list of telephone number codes (prefixes) called by
        people in Bangalore.
        counter_ratio(float): percentage of calls from fixed lines in Bangalore
        that are made to fixed lines also in Bangalore
    """
    # storing tel number codes
    codes = set()

    counter_all = 0
    counter_bang = 0

    for record in calls:
        # filter just 080 tel numbers
        if record[0].find('(080)') == 0:

            # Fixed line numbers
            if record[1].find('(') == 0:
                codes.add(record[1][1:record[1].find(')')])

                # call from 080 to 080
                if record[1].find('(080)') == 0:
                    counter_bang += 1

            # Mobile numbers
            elif (record[1].find(' ') > -1) & (record[1][0] in ['7','8','9']):
                codes.add(record[1][:4])

            # Telemarketers
            elif record[1].find('140') == 0:
                codes.add('140')

            counter_all += 1

    # converting to list and sorting
    codes = sorted(list(codes))
    # compute the percent of calls from to fixed lines in Bangalore
    counter_ratio = round(counter_bang / counter_all *100, 1)

    return codes, counter_ratio


codes, percent = bangladore_calls(calls)

print("The numbers called by people in Bangalore have codes:")
for code in codes:
    print(code)

print("{} percent of calls from fixed lines in Bangalore are calls to other \
fixed lines in Bangalore.".format(percent))
