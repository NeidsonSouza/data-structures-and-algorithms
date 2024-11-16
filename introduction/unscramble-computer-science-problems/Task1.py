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


def add_unique_values_into_set(records, unique_values):
    for record in records:
        unique_values.add(record[0])
        unique_values.add(record[1])


def main():
    unique_tele_nums = set()

    add_unique_values_into_set(calls, unique_tele_nums)
    add_unique_values_into_set(texts, unique_tele_nums)

    print(
        f"There are {len(unique_tele_nums)} different telephone numbers in the records."
    )


if __name__ == "__main__":
    main()
