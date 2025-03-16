# Python Fundamentals: Operators & Control Flow

***⚡ Operators – The true warriors of calculations, making numbers bend to our will.***



## Examples

 ## Logical Operators
Logical operators are used to combine conditional statements.

***and operator***
```
age = 20
is_student = True
if age < 18 and is_student:
    print('You can go to the picnic')
else:
    print('You cannot go to the picnic')
```
***or operator***
```
age = 65
if age < 18 or age > 60:
    print('You can get a discount')
else:
    print('You cannot get a discount')
```
***not operator***
```
is_teacher = False
if not is_teacher:
    print('You are a teacher')
else:
    print('You are not a teacher')
```

## ⚡ Keywords – The sacred words of Python, holding hidden powers.

Python keywords are reserved words that have a special meaning and cannot be used as variable names.
Examples: *if, *else, elif, not, and, or, def, return, etc.

## ⚡ Length & Indexing – The ultimate tools to command strings and lists.


***Length of a string***
```
name = "Hania"
print(len(name))  # Output: 5
```

***Indexing in a string***
```
print(name[0])  # Output: H
```

## ⚡ Control Flow – The strategy game of coding, where if-else and loops decide the fate of execution.

***If Statement***
```
name = 'hania'
if name:
    print('Hi, my name is Hania')
```
***Else  Statement***
```
name = 'rohan'
if name == 'hania':
    print('Hi, my name is Hania')
else:
    print('Hi, my name is Rohan')
```

***Elif Statement***
```
name = 'saima'

if name == 'hania':
    print('Hi, I am Hania')
elif name == 'saima':
    print('I am Saima')
elif name == 'rohan':
    print('Hi, I am Rohan')
else:
    print('Unknown name')
```

***Nested If Statement***
```
invite = True
age = 20

if invite:
    print('You can join the party')
    if age >= 20:
        print('Your age is correct')
    else:
        print('You are too young')
else:
    print('You are not invited')
```


## 📂 Project Structure
```
Python-Operators-Project/
│
├── main.py            # Main Python file with operator examples
├── README.md          # Project documentation
```
**🚦 How to Run**

* Make sure Python is installed: ```python --version```

* Clone the repository:

```git clone https://github.com/hania-1/Class-3-Q3.git```

* Navigate to the project folder:

```cd Class-3-Q3/class_3```

* Run the main.py file:

```python main.py```

## 🛠 Tech Stack

* Python – Core programming language

* VS Code / PyCharm – Recommended code editors

* Google Colab – For cloud-based coding

## 📌 Summary

* Operators: Used to perform operations on variables and values.

* Keywords: Reserved words in Python.

* Length & Indexing: Useful for handling strings and lists.

* Control Flow: Determines the logic of execution using if, elif, else, and nested conditions

## 🤝 Contributions

Contributions are welcome! Feel free to fork the repository and submit pull requests.

