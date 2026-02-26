## Question 4: Generate a List and Tuple from Console Input

### Problem Statement
Write a program that accepts a sequence of comma-separated numbers from the console 
and generates both a list and a tuple containing every number from the sequence.

### Input
A sequence of comma-separated numbers.
```
34,67,55,33,12,98
```

### Expected Output
A list and a tuple both containing the numbers from the input sequence.
```
['34', '67', '55', '33', '12', '98']
('34', '67', '55', '33', '12', '98')
```

### Example
| Input | List Output | Tuple Output |
|-------|-------------|--------------|
| 34,67,55,33,12,98 | ['34', '67', '55', '33', '12', '98'] | ('34', '67', '55', '33', '12', '98') |
| 1,2,3 | ['1', '2', '3'] | ('1', '2', '3') |

### Concepts Covered
- `input()` function
- String `split()` method
- List
- Tuple
- Type conversion

### Explanation
Accept a comma-separated string from the console using `input()`. Use the `split(',')` 
method to break the string at every comma, which gives us a list by default. 
Then convert that list into a tuple using `tuple()`. Both the list and tuple will 
contain the numbers as strings since no integer conversion is applied.

For example when input is `34,67,55,33,12,98`:
- `split(',')` breaks it into → `['34', '67', '55', '33', '12', '98']`
- `tuple()` converts list into → `('34', '67', '55', '33', '12', '98')`
