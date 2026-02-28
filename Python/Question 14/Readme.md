## Question 14: Compute a+aa+aaa+aaaa

### Problem Statement
Write a program that computes the value of `a+aa+aaa+aaaa` with a given digit 
as the value of `a`.

### Input
A single digit number.
```
9
```

### Expected Output
The sum of `a+aa+aaa+aaaa` printed as a single value.
```
11106
```

### Example
| Input (a) | a | aa | aaa | aaaa | Output |
|-----------|---|----|-----|------|--------|
| 9 | 9 | 99 | 999 | 9999 | 11106 |
| 2 | 2 | 22 | 222 | 2222 | 2468 |
| 5 | 5 | 55 | 555 | 5555 | 6170 |

### Calculation Breakdown
For input `9`:
| Term | Value |
|------|-------|
| a | 9 |
| aa | 99 |
| aaa | 999 |
| aaaa | 9999 |
| **Sum** | **11106** |

### Concepts Covered
- `input()` function
- String repetition (`*` operator)
- `int()` type conversion
- Arithmetic operators
- String to integer conversion

### Explanation
Accept a single digit from the console using `input()`. Store it as a string so 
we can use string repetition to build `aa`, `aaa`, and `aaaa` by simply 
multiplying the string by 1, 2, 3, and 4 respectively. Convert each of these 
string representations back to integers using `int()` and add them all together. 
Print the final sum.

For example when input is `9`:
- `a` as string → `"9"`
- String repetition → `"9" * 1 = "9"`, `"9" * 2 = "99"`, `"9" * 3 = "999"`, `"9" * 4 = "9999"`
- Convert to integers → `9, 99, 999, 9999`
- Sum → `9 + 99 + 999 + 9999 = 11106`
- Final output → `11106`
