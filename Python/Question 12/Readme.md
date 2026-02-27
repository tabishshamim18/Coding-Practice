## Question 9: Count Letters and Digits in a Sentence

### Problem Statement
Write a program that accepts a sentence and calculates the number of letters 
and digits present in it.

### Input
A sentence containing letters, digits and other characters.
```
hello world! 123
```

### Expected Output
The count of letters and digits printed separately.
```
LETTERS 10
DIGITS 3
```

### Example
| Input | Letters | Digits |
|-------|---------|--------|
| hello world! 123 | 10 | 3 |
| Python 3.9 is great! | 13 | 1 |
| abc 123 xyz 456 | 6 | 6 |

### Character Breakdown
For input `hello world! 123`:
| Character | Type |
|-----------|------|
| h, e, l, l, o | Letters (5) |
| (space) | Ignored |
| w, o, r, l, d | Letters (5) |
| ! | Ignored |
| (space) | Ignored |
| 1, 2, 3 | Digits (3) |
| **Total** | **Letters 10, Digits 3** |

### Concepts Covered
- `input()` function
- String iteration
- `isalpha()` method
- `isdigit()` method
- Counters / variables
- String formatting

### Explanation
Accept a sentence from the console using `input()`. Iterate through each character 
in the sentence one by one. For each character check two conditions — if it is a 
letter using `isalpha()` and if it is a digit using `isdigit()`. Maintain two 
separate counters, one for letters and one for digits, and increment them 
accordingly. Print both counters at the end.

For example when input is `hello world! 123`:
- Iterate through each character → `h, e, l, l, o, ' ', w, o, r, l, d, '!', ' ', 1, 2, 3`
- `isalpha()` identifies letters → `h, e, l, l, o, w, o, r, l, d` → count = 10
- `isdigit()` identifies digits → `1, 2, 3` → count = 3
- Spaces and `!` are ignored as they are neither letters nor digits
- Final output → `LETTERS 10` and `DIGITS 3`
