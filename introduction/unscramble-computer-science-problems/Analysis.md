## Task0

**Description**: The problem involves finding the first record of texts and the last record of calls.

**Approach**: Order text and call records by date, then pick the oldest record of texts and the newest record of calls.

**Complexity Analysis**:
- **Algorithm**: Both records was ordered using the `sorted()` built-in Python function and passing a datetime object based on the date and time of the record. The date and time of each record are used as input for the `datetime.strptime()` function in order to get a `datetime` object as a return value.
- **Big O Notation**: `sorted()` has $O(n$ $log$ $n)$ as average performance where $n$ is the number of elements in each list.
- **Justification**: `sorted()` uses less memory than using quicksort approach.

## Task1

**Description**: The problem involves calculating how many different telephone numbers are there in the records.

**Approach**: Iterated through the records a single time, saving the telephone numbers of that specific position in the list if it wasn't found in any of the loops before.

**Complexity Analysis**:
- **Algorithm**: A single loop runs through each element of each record.
- **Big O Notation**: $O(n)$ where $n$ is the number of elements in in total.
- **Justification**: Each element is accessed once; hence, the time complexity is directly proportional to the amount of records in total.

## Task2

**Description**: The problem involves finding the telephone number that had the longest call duration.

**Approach**: Sorted the call records by time duration, then picked the record with the greatest duration value.

**Complexity Analysis**:
- **Algorithm**: 
- **Big O Notation**: 
- **Justification**: 

## Task3


## Task4


