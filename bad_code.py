# bad_code.py

PASSWORD = "admin123"  # Security issue: hardcoded password

def calculate():
    x = 10
    y = 0
    result = x / y  # Bug: division by zero
    unused_value = 100  # Code smell: unused variable

    if True:  # Code smell: condition always true
        print("This always runs")

def risky_function(user_input):
    return eval(user_input)  # Security issue: unsafe eval

def empty_method():
    pass
