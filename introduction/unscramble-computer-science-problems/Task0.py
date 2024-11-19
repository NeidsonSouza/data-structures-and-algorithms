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
TASK 0:
What is the first record of texts and what is the last record of calls?
Print messages:
"First record of texts, <incoming number> texts <answering number> at time <time>"
"Last record of calls, <incoming number> calls <answering number> at time <time>, lasting <during> seconds"
"""


from datetime import datetime


def get_ordered_list_by_date(out_of_order_list):
    return sorted(
        out_of_order_list,
        key=lambda x: datetime.strptime(x[2], '%d-%m-%Y %H:%M:%S')
        )


def print_sentence(first_text_record, last_call_record):
    print(
        'First record of texts, {0} texts {1} at time {2}'
        .format(*first_text_record)
        )
    print(
        'Last record of calls, {0} calls {1} at time {2}, lasting {3} seconds'
        .format(*last_call_record)
        )



def main():
    first_text_record = get_ordered_list_by_date(texts)[0]
    last_call_record  = get_ordered_list_by_date(calls)[-1]
    print_sentence(first_text_record, last_call_record)


if __name__ == '__main__':
    main()
