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
in Bangalore. In other words, the calls were initiated by "(080)" area code
to the following area codes and mobile prefixes:
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

def get_percentage(count_bang_to_bang, count_bang_to_all):
    return round((count_bang_to_bang / count_bang_to_all) * 100, 2)


def get_codes():
    fixed_line_prefixes = set()
    mobile_prefixes = set()

    count_bang_to_all = 0
    count_bang_to_bang = 0

    for record in calls:
        src_num = record[0]
        dst_num = record[1]
        if src_num.startswith("(080)"):
            count_bang_to_all += 1
            if dst_num.startswith("("):
                fixed_line_prefixes.add(dst_num[: dst_num.find(")") + 1])
                if dst_num.startswith("(080)"):
                    count_bang_to_bang += 1
            elif dst_num.__contains__(" "):
                mobile_prefixes.add(dst_num[: dst_num.find(" ")])

    codes = fixed_line_prefixes.union(mobile_prefixes)

    return codes, count_bang_to_bang, count_bang_to_all


def print_sentence(codes, percentage):
    print(
        "The numbers called by people in Bangalore have codes:",
        *sorted(codes),
        sep="\n"
    )
    print(
        "{} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore."
        .format(
            percentage
        )
    )


def main():
    codes, count_bang_to_bang, count_bang_to_all = get_codes()
    percentage = get_percentage(count_bang_to_bang, count_bang_to_all)
    print_sentence(codes, percentage)


if __name__ == "__main__":
    main()
