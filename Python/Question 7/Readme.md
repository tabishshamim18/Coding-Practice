## Question: Alphabetical Word Sorting

### Problem Statement
Write a program that accepts a comma-separated sequence of words as input and prints the words in a comma-separated sequence after sorting them alphabetically.

The program should:
1. Take input words from the user.
2. Sort the words in alphabetical order.
3. Print the sorted words in the same comma-separated format.

---

### Input
Comma-separated words entered by the user via console.

### Expected Output
Sorted words printed in a comma-separated format.


### Example
| Input | Output |
|------|------|
| without,hello,bag,world | bag,hello,without,world |
| python,data,analysis | analysis,data,python |
| cat,dog,apple | apple,cat,dog |

---

### Concepts Covered
- User input handling
- String splitting (`split`)
- Lists in Python
- Sorting (`list.sort()`)
- String joining (`','.join()`)

---

### Explanation
The program reads a comma-separated list of words from the console and splits the string into individual words using the comma `,` delimiter.

The words are stored in a list and sorted alphabetically using Python's built-in `sort()` method. After sorting, the list elements are combined back into a single comma-separated string using `join()` and printed.

For example when input is `without,hello,bag,world`:
- Words split → `["without", "hello", "bag", "world"]`
- After sorting → `["bag", "hello", "without", "world"]`
- Printed output → `bag,hello,without,world`
