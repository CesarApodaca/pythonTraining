#Python Training

**Table of Contents**

[TOCM]

[TOC]

#Getting Started
##Types, Statements, and Other Goodies
###Types in Python
####Integers and Floats
```python
answer = 42  # Integer
pi = 3.14159  # Float
```
We can convert or cast a variable to an integer or to a float.
```python
int(pi) == 3
float(answer) == 42.0
```
####Strings
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
####Boolean and None
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
####Other Data Types
###If Statements
###Lists
###Loops
###Break and Continue
###While Loops
###Dictionaries
###Exceptions

