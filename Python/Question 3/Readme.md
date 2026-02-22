## Question 3: Generate a Dictionary of Squares

### Problem Statement
With a given integral number `n`, write a program to generate a dictionary that contains 
`(i, i*i)` such that `i` is an integral number between 1 and n (both included). 
The program should then print the dictionary.

### Input
A single integer number.
```
8
```

### Expected Output
A dictionary where each key is a number and its value is the square of that number.
```
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}
```

### Example
| Input (n) | Output |
|-----------|--------|
| 3 | {1: 1, 2: 4, 3: 9} |
| 5 | {1: 1, 2: 4, 3: 9, 4: 16, 5: 25} |
| 8 | {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64} |

### Concepts Covered
- Dictionary
- Dictionary Comprehension
- Loops (`for` / `range`)
- Exponentiation (`i*i` or `i**2`)

### Explanation
Iterate through every number `i` from 1 to n (inclusive). For each number, create a 
key-value pair where the key is `i` and the value is `i*i` (square of i). 
All pairs are stored in a dictionary and printed at the end.

For example when n = 8:
- i=1 → 1:1
- i=2 → 2:4
- i=3 → 3:9
- and so on until i=8 → 8:64
