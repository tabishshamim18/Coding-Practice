## Question 15: Square Each Odd Number Using List Comprehension

### Problem Statement
Use a list comprehension to square each odd number in a list. The list is input 
by a sequence of comma-separated numbers.

### Input
A sequence of comma-separated numbers.
```
1,2,3,4,5,6,7,8,9
```

### Expected Output
The squared values of all odd numbers printed as a comma-separated sequence.
```
1,9,25,49,81
```

### Example
| Input | Odd Numbers | Output (Squared) |
|-------|-------------|------------------|
| 1,2,3,4,5,6,7,8,9 | 1,3,5,7,9 | 1,9,25,49,81 |
| 2,3,4,5,6 | 3,5 | 9,25 |
| 1,3,5,7 | 1,3,5,7 | 1,9,25,49 |

### Calculation Breakdown
For input `1,2,3,4,5,6,7,8,9`:
| Number | Odd? | Squared |
|--------|------|---------|
| 1 | Yes ✅ | 1 |
| 2 | No ❌ | Ignored |
| 3 | Yes ✅ | 9 |
| 4 | No ❌ | Ignored |
| 5 | Yes ✅ | 25 |
| 6 | No ❌ | Ignored |
| 7 | Yes ✅ | 49 |
| 8 | No ❌ | Ignored |
| 9 | Yes ✅ | 81 |
| **Result** | | **1,9,25,49,81** |

### Concepts Covered
- `input()` function
- String `split()` method
- List comprehension
- Modulo operator (`%`) for odd check
- Exponentiation (`**2`) for squaring
- String `join()` method

### Explanation
Accept a comma-separated string from the console using `input()`. Use `split(',')` 
to break it into individual numbers and convert each to an integer. Use a list 
comprehension to iterate through the list, filter only odd numbers using the 
modulo operator `%`, and square each odd number using `**2`. Finally use `join()` 
to print the results as a comma-separated sequence.

For example when input is `1,2,3,4,5,6,7,8,9`:
- `split(',')` breaks it into → `['1','2','3','4','5','6','7','8','9']`
- Convert to integers → `[1, 2, 3, 4, 5, 6, 7, 8, 9]`
- List comprehension filters odd and squares → `[1, 9, 25, 49, 81]`
- `join()` combines into → `1,9,25,49,81`
