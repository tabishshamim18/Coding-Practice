## Question 1: Numbers Divisible by 7 but Not a Multiple of 5

### Problem Statement
Write a program that finds all numbers which are divisible by 7 but are not a multiple of 5, 
within the range of 2000 to 3200 (both inclusive). The results should be printed in a 
comma-separated sequence on a single line.

### Input
No input required. The range is fixed between 2000 and 3200.

### Expected Output
All qualifying numbers printed in a comma-separated sequence on a single line.
```
2002,2009,2016,2023,2037,2044,...
```

### Conditions
| Condition | Description |
|-----------|-------------|
| Divisible by 7 | Number % 7 == 0 |
| Not a multiple of 5 | Number % 5 != 0 |
| Range | 2000 to 3200 (inclusive) |

### Concepts Covered
- Loops (`for` / `range`)
- Conditional statements (`if`)
- Modulo operator (`%`)
- String joining (`join`)

### Explanation
Iterate through every number from 2000 to 3200. For each number check two conditions —
it must be divisible by 7 (remainder 0 when divided by 7) and it must not be divisible 
by 5 (remainder should not be 0 when divided by 5). All numbers satisfying both conditions 
are collected and printed as a comma-separated sequence.
