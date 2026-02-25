## Question: Convert Input Lines to Uppercase

### Problem Statement
Write a program that accepts a sequence of lines as input and prints the lines after converting all characters in each sentence to uppercase.

The program should:
1. Continuously accept input lines from the user.
2. Stop taking input when a blank line is entered.
3. Convert each line to uppercase.
4. Print the converted lines.

---

### Input
Multiple lines entered by the user via console (input ends with an empty line).

### Expected Output
All input lines printed in uppercase.


---

### Example
| Input | Output |
|------|------|
| Hello world | HELLO WORLD |
| Python programming | PYTHON PROGRAMMING |
| Data engineering | DATA ENGINEERING |

---

### Concepts Covered
- Infinite loops (`while True`)
- Conditional statements
- User input handling
- Lists in Python
- String methods (`upper()`)
- Loop iteration

---

### Explanation
The program continuously reads input lines from the console. Each entered line is converted to uppercase and stored in a list.

When the user enters a blank line (presses Enter without typing anything), the input process stops. The program then prints each stored line one by one.

For example:

Input lines:
- `Hello world`
- `Practice makes perfect`

After processing:
- `HELLO WORLD`
- `PRACTICE MAKES PERFECT`

These lines are printed as the final output.
