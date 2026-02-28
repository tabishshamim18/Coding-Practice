
## Question 6: Formula-Based Calculation

### Problem Statement

Write a program that calculates and prints values using the formula:

Q = √((2 × C × D) / H)

Where:

* **C = 50** (constant)
* **H = 30** (constant)
* **D** is a sequence of numbers provided by the user as comma-separated input.

The program should:

1. Read the input values.
2. Apply the formula to each number.
3. Round the result to the nearest integer.
4. Print all results as a comma-separated sequence on a single line.

---

### Input

Comma-separated integers entered by the user via console.

```
100,150,180
```

### Expected Output

Calculated values printed in a comma-separated format.

```
18,22,24
```

### Example

| Input       | Output   |
| ----------- | -------- |
| 100,150,180 | 18,22,24 |
| 200,300     | 26,32    |
| 50          | 13       |

---

### Concepts Covered

* User input handling
* String splitting and parsing
* Type conversion (`int`)
* Mathematical operations in Python
* Square root using exponentiation (`** 0.5`)
* Rounding numbers (`round()`)
* String joining (`','.join()`)
* Loop iteration

---

### Explanation

The program reads a comma-separated line of numbers from the console and splits it into individual values. Each value is converted into an integer and processed using the given formula.

For each number D:

* The formula is applied.
* The square root is calculated.
* The result is rounded to the nearest integer.
* The value is converted to a string and stored.

Finally, all results are joined together into a single comma-separated string and printed.

For example when input is `100,150,180`:

* Computed values → 18, 22, 24
* Printed output → `18,22,24`
