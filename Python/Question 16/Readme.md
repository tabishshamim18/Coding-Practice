## Question 16: Bank Account Transaction Log

### Problem Statement
Write a program that computes the net amount of a bank account based on a 
transaction log from console input.

The transaction log format is:
```
D 100
W 200
```
- `D` means **Deposit** (adds money to account)
- `W` means **Withdrawal** (deducts money from account)

### Input
A sequence of transactions, each on a new line, until an empty line is entered.
```
D 300
D 300
W 200
D 100
```

### Expected Output
The net balance of the account after all transactions.
```
500
```

### Transaction Breakdown
For the given input:
| Transaction | Type | Amount | Balance |
|-------------|------|--------|---------|
| D 300 | Deposit | +300 | 300 |
| D 300 | Deposit | +300 | 600 |
| W 200 | Withdrawal | -200 | 400 |
| D 100 | Deposit | +100 | 500 |
| **Final Balance** | | | **500** |

### Example
| Transactions | Output |
|-------------|--------|
| D 300, D 300, W 200, D 100 | 500 |
| D 500, W 100, W 200 | 200 |
| D 1000, W 500, D 200, W 300 | 400 |

### Concepts Covered
- `input()` function
- `while` loop
- String `split()` method
- Conditional statements (`if/elif`)
- Arithmetic operators (`+`, `-`)
- Type conversion (`int()`)

### Explanation
Start with a balance of 0. Accept transactions one by one from the console using 
`input()` inside a `while` loop. Keep reading until an empty line is entered. 
For each transaction, split the line into the transaction type and amount using 
`split()`. If the type is `D`, add the amount to the balance. If the type is `W`, 
subtract the amount from the balance. Print the final balance after all 
transactions are processed.

For example when input is `D 300, D 300, W 200, D 100`:
- Start balance → `0`
- `D 300` → Deposit → `0 + 300 = 300`
- `D 300` → Deposit → `300 + 300 = 600`
- `W 200` → Withdrawal → `600 - 200 = 400`
- `D 100` → Deposit → `400 + 100 = 500`
- Final output → `500`
