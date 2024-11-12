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

def add_to_list(item, ls):
    if item not in ls:
        ls.append(item)


def get_uniq_numbers(records, uniqs):
    for item in records:
        add_to_list(item[0], uniqs)
        add_to_list(item[1], uniqs)

    return uniqs

if __name__ == "__main__":
    uniqs = get_uniq_numbers(texts, [])
    uniqs = get_uniq_numbers(calls, uniqs)

    sentence = f'There are {len(uniqs)} different telephone numbers in the records.'
    print(sentence)
