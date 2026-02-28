## Question 11: Numbers with All Even Digits

### Problem Statement
Write a program that finds all numbers between 1000 and 3000 (both included) such 
that each digit of the number is an even number. The numbers obtained should be 
printed in a comma-separated sequence on a single line.

### Input
No input required. The range is fixed between 1000 and 3000.

### Expected Output
All qualifying numbers printed in a comma-separated sequence on a single line.
```
2000,2002,2004,2006,2008,2020,2022,2024,...
```

### Conditions
| Condition | Description |
|-----------|-------------|
| Range | 1000 to 3000 (inclusive) |
| Each digit must be even | Digits can only be 0, 2, 4, 6, 8 |

### Even vs Odd Digits Reference
| Even Digits | Odd Digits |
|-------------|------------|
| 0, 2, 4, 6, 8 | 1, 3, 5, 7, 9 |

### Example Breakdown
| Number | Digits | All Even? |
|--------|--------|-----------|
| 2024 | 2, 0, 2, 4 | Yes ✅ |
| 2003 | 2, 0, 0, 3 | No ❌ (3 is odd) |
| 2468 | 2, 4, 6, 8 | Yes ✅ |
| 1234 | 1, 2, 3, 4 | No ❌ (1 and 3 are odd) |

### Concepts Covered
- Loops (`for` / `range`)
- String conversion (`str()`)
- Modulo operator (`%`)
- `all()` function
- String `join()` method
- List comprehension

### Explanation
Iterate through every number from 1000 to 3000 (inclusive). For each number, 
convert it to a string so we can access each digit individually. Check if every 
digit is even by converting each character back to an integer and applying the 
modulo operator `%`. If all digits pass the even check using `all()`, the number 
is added to our result list. Finally all qualifying numbers are joined into a 
comma-separated sequence and printed.

For example for number 2024:
- Convert to string → `"2024"`
- Extract digits → `['2', '0', '2', '4']`
- Check each digit → `[True, True, True, True]`
- `all()` returns → `True` ✅ → included in result

For number 2003:
- Convert to string → `"2003"`
- Extract digits → `['2', '0', '0', '3']`
- Check each digit → `[True, True, True, False]`
- `all()` returns → `False` ❌ → excluded from result
