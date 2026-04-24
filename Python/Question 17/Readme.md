## Question: Sort Tuples by Multiple Criteria

### Problem Statement
Write a program that accepts tuples of `(name, age, height)` from console input and sorts them in ascending order.

Sorting priority:
1. Sort by **name** (string)
2. Then by **age** (number)
3. Then by **height** (number)

The priority order is:
**name > age > height**

The program should:
1. Continuously accept input lines.
2. Stop when a blank line is entered.
3. Store each input as a tuple.
4. Sort all tuples based on the given criteria.
5. Print the sorted list.

---

### Input
Multiple lines entered by the user via console (input ends with an empty line).

Tom,19,80

John,20,90

Jony,17,91

Jony,17,93

Json,21,85

---

### Expected Output
[('John', '20', '90'), ('Jony', '17', '91'), ('Jony', '17', '93'), ('Json', '21', '85'), ('Tom', '19', '80')]


---

### Example
| Input | Output |
|------|------|
| Tom,19,80 | ('Tom', '19', '80') |
| John,20,90 | ('John', '20', '90') |
| Jony,17,91 | ('Jony', '17', '91') |

---

### Solution (Python)

```python
from operator import itemgetter

my_list = []

while True:
    s = input()
    if not s:
        break
    my_list.append(tuple(s.split(",")))

print(sorted(my_list, key=itemgetter(0, 1, 2)))
