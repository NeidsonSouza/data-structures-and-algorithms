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

**Approach**: Iterate through the list a single time, counting how many calls was from Bangalore to any number and from Bangalore to Bangalore. It also save fixed line codes and mobile prefixes in a `set()`.

**Complexity Analysis**:
- **Algorithm**: A single loop runs through each call record, then order it using `sorted()` built-in function.
- **Big O Notation**: $O(n)$ where $n$ is the number of elements in total.
- **Justification**: Each element is accessed once; hence, the time complexity is directly proportional to the amount of records.

## Task4

**Description**: The problem involves identifying numbers that make outgoing calls but never send or receive texts or incoming calls.

**Approach**: A single loop runs through each record, keeping the caller phone numbers in a `set()` and the not-caller phone numbers in another `set()`. Another loop goes through these two created sets using the `union()` method and removes the first collection, the items that are in the second one.

**Complexity Analysis**:
- **Algorithm**: A single loop runs through each record, save each one in *sets* according to some conditions, the run another loop to find difference between them.
- **Big O Notation**: $O(2n)$ where $n$ is the number of elements in total.
- **Justification**: In the worst case two loops was necessary.
The fisrt one sabe caller numbers and the second one save the rest of it. Then a second loop is need to find the difference between the lists.
