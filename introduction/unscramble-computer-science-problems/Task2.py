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

if __name__ == '__main__':
    phone_dict = {}

    for call in calls:
        phone_dict[call[0]] = phone_dict.get(call[0], 0) + int(call[3])
        phone_dict[call[1]] = phone_dict.get(call[1], 0) + int(call[3])

    call_durations = list(phone_dict.values())
    longest_time   = max(call_durations)
    id             = call_durations.index(longest_time)
    
    print(f'{list(phone_dict.keys())[id]} spent the longest time, {longest_time} seconds, on the phone during September 2016.')
