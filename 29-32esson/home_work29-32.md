# Lesson 2.2

## Home work 2.2

### For each task please provide a separate file (you can do a special folder for it in your git repository to avoid a mess). If task asks you to provide a procedure/function add a call of it to your script. If procedure/function should have a specific behaviour for various cases add calls of it with args demonstrating the cases.

### Task 1
#### Self-study input() function. Write a script which accepts a sequence of comma-separated numbers from user and generate a list and a tuple with those numbers and prints these objects as-is (just print(list) without any formatting).


### Task 2
#### Develop a procedure to print all even numbers from a numbers list which is given as an argument. Keep the original order of numbers in list and stop printing if a number 254 was met. Don't forget to add a check of the passed argument type.

### Task 3
#### Something old in a new way :). Self-study positional arguments for Python scripts (sys.argv). Write a script that takes a list of words (or even phrases)aScript should ask a user to write something to stdin until user won't provide one of argument phrases.

### Task 4
#### We took a little look on os module. Write a small script which will print a string using all the types of string formatting which were considered during the lecture with the following context: This script has the following PID: <ACTUAL_PID_HERE>. It was ran by <ACTUAL_USERNAME_HERE> to work happily on <ACTUAL_OS_NAME>-<ACTUAL_OS_RELEASE>.

### Task 5
#### Develop a function that takes a list of integers (by idea not in fact) as an argument and returns list of top-three max integers. If passed list contains not just integers collect them and print the following error message: You've passed some extra elements that I can't parse: [<"elem1", "elem2" .... >]. If return value will have less than 3 elements for some reason it's ok and shouldn't cause any problem, but some list should be returned in any case.

### Task 6
#### Create a function that will take a string as an argument and return a dictionary where keys are symbols from the string and values are the count of inclusion of that symbol.

### Task 7
#### Develop a procedure that will have a size argument and print a table where num of columns and rows will be of this size. Cells of table should contain numbers from 1 to n ** 2 placed in a spiral fashion. Spiral should start from top left cell and has a clockwise direction (see the example below).

#### example:
```python
>>> print_spiral(5)
1 2 3 4 5
16 17 18 19 6
15 24 25 20 7
14 23 22 21 8
13 12 11 10 9
```
