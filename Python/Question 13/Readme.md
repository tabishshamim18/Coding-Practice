## Question 13: Count Upper Case and Lower Case Letters

### Problem Statement
Write a program that accepts a sentence and calculates the number of upper case 
and lower case letters present in it.

### Input
A sentence containing upper case and lower case letters.
```
Hello world!
```

### Expected Output
The count of upper case and lower case letters printed separately.
```
UPPER CASE 1
LOWER CASE 9
```

### Example
| Input | Upper Case | Lower Case |
|-------|------------|------------|
| Hello world! | 1 | 9 |
| Python Is Fun | 3 | 8 |
| HELLO world | 5 | 5 |

### Character Breakdown
For input `Hello world!`:
| Character | Type |
|-----------|------|
| H | Upper Case (1) |
| e, l, l, o | Lower Case (4) |
| (space) | Ignored |
| w, o, r, l, d | Lower Case (5) |
| ! | Ignored |
| **Total** | **Upper Case 1, Lower Case 9** |

### Concepts Covered
- `input()` function
- String iteration
- `isupper()` method
- `islower()` method
- Counters / variables
- String formatting

### Explanation
Accept a sentence from the console using `input()`. Iterate through each character 
in the sentence one by one. For each character check two conditions — if it is an 
upper case letter using `isupper()` and if it is a lower case letter using 
`islower()`. Maintain two separate counters, one for upper case and one for lower 
case, and increment them accordingly. Spaces, digits and special characters are 
ignored as they are neither upper nor lower case. Print both counters at the end.

For example when input is `Hello world!`:
- Iterate through each character → `H, e, l, l, o, ' ', w, o, r, l, d, '!'`
- `isupper()` identifies upper case → `H` → count = 1
- `islower()` identifies lower case → `e, l, l, o, w, o, r, l, d` → count = 9
- Space and `!` are ignored as they fail both `isupper()` and `islower()` checks
- Final output → `UPPER CASE 1` and `LOWER CASE 9`
