## Question 6: Remove Duplicates and Sort Words

### Problem Statement
Write a program that accepts a sequence of whitespace separated words as input 
and prints the words after removing all duplicate words and sorting them 
alphanumerically.

### Input
A sequence of whitespace separated words.
```
hello world and practice makes perfect and hello world again
```

### Expected Output
The unique words sorted alphanumerically and printed on a single line.
```
again and hello makes perfect practice world
```

### Example
| Input | Output |
|-------|--------|
| hello world and practice makes perfect and hello world again | again and hello makes perfect practice world |
| cat dog cat bird dog fish | bird cat dog fish |
| one two three one two | one three two |

### Concepts Covered
- `input()` function
- String `split()` method
- `set()` for removing duplicates
- `sorted()` for alphanumeric sorting
- String `join()` method

### Explanation
Accept a whitespace separated string from the console using `input()`. Use `split()` 
to break the string into individual words which gives us a list. Convert the list 
into a `set()` to automatically remove all duplicate words since sets only store 
unique values. Then use `sorted()` to sort the unique words alphanumerically. 
Finally use `join()` to combine them back into a single space separated string 
and print it.

For example when input is `hello world and practice makes perfect and hello world again`:
- `split()` breaks it into → `['hello', 'world', 'and', 'practice', 'makes', 'perfect', 'and', 'hello', 'world', 'again']`
- `set()` removes duplicates → `{'again', 'and', 'hello', 'makes', 'perfect', 'practice', 'world'}`
- `sorted()` sorts alphanumerically → `['again', 'and', 'hello', 'makes', 'perfect', 'practice', 'world']`
- `join()` combines into → `again and hello makes perfect practice world`
