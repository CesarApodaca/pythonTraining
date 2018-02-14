TODO

- Dar una leida a PEP20 (amacizar el PEP8 ).
- Investigar el uso y el por que de self en una clase.
- Investigar por que teniendo una variable declarada afuera de una funcion,  dentro de una funcion use el self.variable para retornarla.
- Investigar que pasa cuando se quiere sobreescribir el constructor (herencia)
- Investigar interfaces Python
- Investigar el magico @ 
- Investigar if \_\_name__ == "\_\_main__"
- Investigar mas del Virtual Environment
- Darle una checada a Flask

# Self
- Nosotros podemos poner cualquier otro nombre, no necesariamente self.
- Algunos metodos carecen de self, como cuando son estaticos.
- El uso de self como primer argumento esta en el PEP8.
- Cuando agregamos el self a una variable, indicamos que es una variable a nivel de clase.
 Cuando tenemos una variable declarada afuera de un metodo esta a nivel de clase y con el self, podemos 
 acceder a esa variable desde cualquier lugar dentro de nuestra clase.
- Imagina que tienes una clase persona con su metodo imprimir. Creas 2 objetos de tipo persona, p1 y p2.
 No se crea una copia del metodo imprimir por cada objeto, el metodo pertenece a la clase Persona y con el self se pasan
 los datos de la instancia adecuada.
 
 # PEP8
## Identation
 The recommendation is therefore to use 4 spaces for indentation. 
 ```python
if True:
    print("If works")

for element in range(0, 5):
    print(element)
```
When you write a big expression, it is best to keep the expression vertically aligned. When you do this, you'll create a "hanging indent".
```python
value = square_of_numbers(
              num1, num2,
              num3, num4)

list_of_people = [
 "Rama",
 "John",
 "Shiva"
]
```
Note that Python 3 doesn't allow mixing tabs and spaces for indentation. That's why you should choose one of the two and stick with it!

## Maximum Line Length
Generally, it's good to aim for a line length of 79 characters in your Python code.
Comments should have 72 characters of line length.

While using the + operator, you can better use a proper line break, which makes your code easier to understand:
```python
total = (A +
         B +
         C)
```
## Blank Lines
In Python scripts, top-level function and classes are separated by two blank lines. Method definitions inside classes should be separated by one blank line.

## Imports
that if you do many imports, you should make sure to state each import on a single line.
```python
from config import settings

# or

import os
import sys
```

# PEP20
- Beautiful is better than ugly.
- Explicit is better than implicit.
- Simple is better than complex.
- Complex is better than complicated.
- Flat is better than nested.
- Sparse is better than dense.
- Readability counts.
- Special cases aren't special enough to break the rules.
- Although practicality beats purity.
- Errors should never pass silently.
- Unless explicitly silenced.
- In the face of ambiguity, refuse the temptation to guess.
- There should be one-- and preferably only one --obvious way to do it.
- Although that way may not be obvious at first unless you're Dutch.
- Now is better than never.
- Although never is often better than *right* now.
- If the implementation is hard to explain, it's a bad idea.
- If the implementation is easy to explain, it may be a good idea.
- Namespaces are one honking great idea -- let's do more of those!

# @ - Decorators