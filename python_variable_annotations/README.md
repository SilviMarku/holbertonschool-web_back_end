Python - Variable Annotations

This repository focuses on utilizing variable annotations and type hints in Python 3 for improved code readability, maintainability, and static analysis. Additionally, we explore the concept of duck typing and how to validate the code using Mypy.

## Table of Contents

1. [Type Annotations in Python 3](#type-annotations-in-python-3)
2. [Using Type Annotations](#using-type-annotations)
3. [Duck Typing](#duck-typing)
4. [Validating Code with Mypy](#validating-code-with-mypy)
5. [Getting Started](#getting-started)
6. [Contributing](#contributing)
7. [License](#license)

## Type Annotations in Python 3

Type annotations in Python 3 allow developers to specify variable types, function parameters, and return types. While Python remains dynamically-typed, these annotations provide hints for developers and tools without affecting the runtime behavior of the program.

```python
def add_numbers(x: int, y: int) -> int:
    return x + y
In this example, x: int and y: int indicate that x and y should be integers, and -> int specifies that the function should return an integer.

Using Type Annotations
Function Signatures:

python
Copy code
def greet(name: str) -> str:
    return f"Hello, {name}"
Variable Types:

python
Copy code
age: int = 25
Duck Typing
Duck typing is a concept where the type of an object is less important than its behavior. In Python, this is exemplified by functions that accept objects based on their methods rather than their explicit type.

python
Copy code
def make_sound(animal):
    animal.quack()
This function accepts any object with a quack method, showcasing the flexibility of duck typing.

Validating Code with Mypy
Mypy is a powerful static type checker for Python. It uses type annotations to analyze code and catch potential type-related issues before runtime.

Install Mypy:

bash
Copy code
pip install mypy
Run Mypy on Your Code:

bash
Copy code
mypy your_code.py
Mypy will provide feedback on potential type-related errors, enhancing the reliability of your code.

Getting Started
To get started, clone this repository and explore the provided examples. Feel free to experiment with variable annotations, create your own code samples, and run Mypy for static type checking.

bash
Copy code
git clone https://github.com/your_username/python-variable-annotations.git
cd python-variable-annotations
Contributing
If you find ways to improve the examples or have additional insights, feel free to contribute! Fork the repository, make your changes, and submit a pull request.

License
This project is licensed under the MIT License, making it open for collaboration and use in various projects.