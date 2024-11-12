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

def is_number_in_texts(n):
    for i in texts:
        if n == i[0]:
            return True
        if n == i[1]:
            return True
    return False

def is_number_a_receiver(n):
    for i in calls:
        if n == i[1]:
            return True
    return False

def add_to_list(item, ls):
    if item not in ls:
        ls.append(item)


def get_uniq_numbers(records, uniqs):
    for item in records:
        if item[0].startswith('140'):
            if not is_number_in_texts(item[0]):
                if not is_number_a_receiver(item[0]):
                    add_to_list(item[0], uniqs)

    return uniqs

if __name__ == "__main__":
    uniqs = get_uniq_numbers(calls, [])
    print(f'These numbers could be telemarketers:')
    print(*sorted(uniqs),sep='\n')
