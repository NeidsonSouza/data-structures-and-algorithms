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


if __name__ == '__main__':
    first_text_record = get_ordered_list_by_date(texts)[0]
    last_call_record = get_ordered_list_by_date(calls)[-1]

    text_str = (
        f'First record of texts, {first_text_record[0]} '
        f'texts {first_text_record[1]} at time {first_text_record[2]}'
        )
    
    call_str = (
        f'Last record of calls, {last_call_record[0]} '
        f'calls {last_call_record[1]} at time {last_call_record[2]}, '
        f'lasting {last_call_record[3]} seconds'
    )

    print(text_str)
    print(call_str)
