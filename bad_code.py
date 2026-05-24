# fixed_code.py

import os
import ast

PASSWORD = os.getenv("APP_PASSWORD")

def calculate(x, y):
    if y == 0:
        return "Cannot divide by zero"
    return x / y

def safe_function(user_input):
    try:
        return ast.literal_eval(user_input)
    except (ValueError, SyntaxError):
        return "Invalid input"

def show_message():
    print("Code quality improved")
