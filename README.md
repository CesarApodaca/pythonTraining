# Python Training - Getting Started
## Types, Statements, and Other Goodies
### Types in Python
#### Integers and Floats
```python
answer = 42  # Integer
pi = 3.14159  # Float
```
We can convert or cast a variable to an integer or to a float.
```python
int(pi) == 3
float(answer) == 42.0
```
#### Strings
Strings can be defined using single quotes and double quotes.
```python
'Hello World'  # String
"Hello World"  # String
```
We can capitalize a string, replace chars, verify if the string is alpha or if is a digit, split our string & escape chars.
```python
print("hello".capitalize())  # capitalize the first letter
print("hello".replace("e","a"))  # replace the letter e with the letter a
print("hello".isalpha())  # true
print("hello".isdigit())  # false
print("some,csv,values".split(","))
print("This is a string \' ")
```
We can use the String Format Function
```python
name = "Python"
machine = "Frank"
"Nice to meet you {0}, I am {1}".format(name, machine)
```
Also we can use the interpolation.
```python
name = "Python"
machine = "Frank"
f"Nice to meet you {name}, I am {machine}"  # We must to add the letter f
```
#### Boolean and None
```python
python_course = True  # The first letter needs to start with a capital letter T
java_course = False
```
We can convert from Boolean to an integer or String.
```python
int(python_course) == 1
int(java_course == 0)
str(python_course) == "True"
```
None is similar to null in other languages.
```python
aliens_found = None
```
#### Other Data Types
### If Statements
```python
number = 5
if number == 5:
    print("number is 5")
else:
    print("Number is not 5")
```

We can use the Truthy and Falsy values.
```python
text = "Python"
if text:
    print("Text is defined and truthy")
```
this code will not execute.
```python
aliens_found = None
if aliens_found:
    print("this will NOT execute")
```

we can use the Not If statements
```python
number = 5
if number != 5:
    print("This code will NOT execute")
    
python_course = True
if not python_course:
    print("This code will also NOT execute")
```
Also we have multiple if conditions.
```python
number = 3
python_course = True
if number == 3 and python_course:
    print("This will execute")
    
if number == 17 or python_course:
    print("this code will also execute")
```
We can save ourselves some space with ternary if statements.
```python
a = 1
b = 2
"bigger" if a > b else "smaller"
# We get smaller because 1 is smaller than 2
```

### Lists
```python
student_names = []
student_names = ["Mark", "Katarina", "Jessica"]

student_names[0] == "Mark"
student_names[2] == "Jessica"
```
If we want to get the last element in our list, we can write something like.
```python
student_names[-1] == "Jessica"
```

If we want to add more elements in our list we use this,
```python
student_names.apppend("Cesarin")
```

If we want to verify if an element exists in our list we use.
```python
"Mark" in student_names == True
```

If we need to know the length of a string or list we use.
```python
len(student_names) == 4
```


### Loops
### Break and Continue
### While Loops
### Dictionaries
### Exceptions

