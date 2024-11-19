## Task0

**Description**: The problem involves finding the first record of texts and the last record of calls.

**Approach**: Order text and call records by date, then pick the oldest record of texts and the newest record of calls.

**Complexity Analysis**:
- **Algorithm**: Both records was ordered using the `sorted()` built-in Python function and passing a datetime object based on the date and time of the record. The date and time of each record are used as input for the `datetime.strptime()` function in order to get a `datetime` object as a return value.
- **Big O Notation**: `sorted()` has $O(n$ $log$ $n)$ as worst-case performance where n is the number of elements in the list.
- **Justification**: The `sorted()` function uses less memory than the quicksort approach.

## Task1

**Description**: The problem involves calculating how many different telephone numbers are there in the records.

**Approach**: Iterate through the records a single time, saving the telephone numbers of that specific position in a set that automatically avoids adding repetitive items.

**Complexity Analysis**:
- **Algorithm**: A single loop runs through each element of each record.
- **Big O Notation**: $O(n)$ where $n$ is the number of elements in total.
- **Justification**: Each element is accessed once; hence, the time complexity is directly proportional to the amount of records.

## Task2

**Description**: The problem involves finding the telephone number that spent the longest time on the phone during the period.

**Approach**: Iterate through the records twice: first, save the caller and receiver phone numbers along with their respective call durations in a set to get unique phone numbers. During the second iteration, determine the longest call duration and its corresponding phone number.

**Complexity Analysis**:
- **Algorithm**: Two loops run through each record. The first loop sends unique values and the sum of calls for each number to a `set()`, and the second loop gets the phone number and the duration of the longest time record.
- **Big O Notation**: $O(2n)$ where $n$ is the number of elements in total.
- **Justification**: Each element is accessed twice; hence, the time complexity is directly proportional to the amount of records.

## Task3

**Description**: The problem involves finding the area codes of telephone numbers from people who called from Bangalore, then calculating the percentage of calls from fixed lines in Bangalore that are made to other fixed lines in Bangalore.

**Approach**: Iterate through the list a single time, saving the codes (numbers between parentheses) and mobile prefixes if the call destination number has 080 as the area code, checking for duplication to ensure we have unique values in the list, and counting the records that were from 080 to 080 area code. Use the `sorted()` built-in function to order the area codes and mobile prefixes in lexicographic order.

**Complexity Analysis**:
- **Algorithm**: A single loop runs through each element of the calls list once, then order it using `sorted()` built-in function.
- **Big O Notation**: One part of the algorithm has $O(n)$ time complexity, but the `sorted()` function has $O(n$ $log$ $n)$ as worst-case performance, where $n$ is the number of records in the list, so consider $O(n$ $log$ $n)$ as the worst-case scenario.
- **Justification**: Each element is accessed once in part A; hence, the time complexity is directly proportional to the list size, and the `sorted()` function uses less memory than the quicksort approach.

## Task4

**Description**: The problem involves identifying numbers that make outgoing calls but never send or receive texts or incoming calls.

**Approach**: For each unique phone number that begins with '140' in the calls list:

* A single loop runs through each telephone number in the texts list to check if it has never sent or received any text message.
* A single loop runs through previous call records to check if this number has never received any calls
* If the number passes both checks (no texts, never received calls), add it to our unique-number list
* Order the list using `sorted()` built-in function.

**Complexity Analysis**:
- **Algorithm**: For each unique phone number that begins with '140' in the calls list, the loop runs through each telephone number of the texts list, also runs through the previous receiver column in the call records, then sorts the created list using the `sorted()` function.
- **Big O Notation**: $O(n²)$ where $n$ is the number of records in the list, as it grows faster than $O(n$ $log$ $n)$.
- **Justification**: Each unique caller phone number that begins with '140' needs to be compared with each telephone number in the texts list.
