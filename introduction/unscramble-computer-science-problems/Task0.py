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

text_ordered_list = sorted(texts, key=lambda x: datetime.strptime(x[2], '%d-%m-%Y %H:%M:%S'))[0]
text_final_string = f'First record of texts, {text_ordered_list[0]} texts {text_ordered_list[1]} at time {text_ordered_list[2]}'
print(text_final_string)
