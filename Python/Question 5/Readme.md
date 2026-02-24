## Question 5: Class with String Methods

### Problem Statement
Define a class that has at least two methods:
- `getString` : To get a string from console input
- `printString` : To print the string in upper case
Also include a simple test function to test the class methods.

### Input
A string entered by the user via console.
```
hello world
```

### Expected Output
The input string printed in upper case.
```
HELLO WORLD
```

### Example
| Input | Output |
|-------|--------|
| hello world | HELLO WORLD |
| python is fun | PYTHON IS FUN |
| data engineering | DATA ENGINEERING |

### Concepts Covered
- Class definition
- Instance methods
- `input()` function
- String `upper()` method
- Object instantiation
- Unit testing (`unittest`)

### Explanation
A class is defined with two methods:
- `getString()` takes input from the user via console and stores it as an 
instance variable inside the class.
- `printString()` takes that stored string and prints it in uppercase using 
Python's built-in `upper()` method.

A test function is also written to verify that both methods work correctly 
without needing manual console input, by directly assigning a string value 
and checking if the uppercase output matches the expected result.

For example when input is `hello world`:
- `getString()` stores → `"hello world"`
- `printString()` prints → `"HELLO WORLD"`
