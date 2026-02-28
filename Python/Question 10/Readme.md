## Question 10: Binary Numbers Divisible by 5

### Problem Statement
Write a program that accepts a sequence of comma-separated 4-digit binary numbers 
as input and checks whether they are divisible by 5 or not. The numbers that are 
divisible by 5 should be printed in a comma-separated sequence.

### Input
A sequence of comma-separated 4-digit binary numbers.
```
0100,0011,1010,1001
```

### Expected Output
Binary numbers that are divisible by 5, printed in a comma-separated sequence.
```
1010
```

### Example
| Input | Output |
|-------|--------|
| 0100,0011,1010,1001 | 1010 |
| 0101,1010,1111,0001 | 0101,1010 |
| 0001,0010,0011 | No numbers divisible by 5 |

### Binary to Decimal Reference
| Binary | Decimal | Divisible by 5? |
|--------|---------|-----------------|
| 0100 | 4 | No |
| 0011 | 3 | No |
| 1010 | 10 | Yes |
| 1001 | 9 | No |
| 0101 | 5 | Yes |

### Concepts Covered
- `input()` function
- String `split()` method
- `int()` with base conversion (`int(n, 2)` for binary to decimal)
- Modulo operator (`%`)
- List comprehension
- String `join()` method

### Explanation
Accept a comma-separated string of 4-digit binary numbers from the console using 
`input()`. Use `split(',')` to break them into individual binary numbers. For each 
binary number, convert it to decimal using `int(n, 2)` where base 2 indicates binary. 
Then check if the decimal value is divisible by 5 using the modulo operator `%`. 
Collect all binary numbers that pass the condition and print them as a comma-separated 
sequence using `join()`.

For example when input is `0100,0011,1010,1001`:
- `split(',')` breaks it into → `['0100', '0011', '1010', '1001']`
- Convert to decimal → `[4, 3, 10, 9]`
- Check divisibility by 5 → `[False, False, True, False]`
- Filter and join → `1010`
