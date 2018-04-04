"""A prefix-notation calculator.

Using the arithmetic.py file from Calculator Part 1, create the
calculator program yourself in this file.
"""

from arithmetic import *

# Your code goes here

while True:
    user_input = raw_input("> ")
    token_input = user_input.split(" ")

    if token_input[0] == "q":
        quit()

    try:
        token_input[1] = float(token_input[1])
        if len(token_input) == 3:
            token_input[2] = float(token_input[2])
    except:
        continue

    if token_input[0] == "+":
        user_output = add(token_input[1], token_input[2])
    elif token_input[0] == "-":
        user_output = subtract(token_input[1], token_input[2])
    elif token_input[0] == "*":
        user_output = multiply(token_input[1], token_input[2])
    elif token_input[0] == "/":
        user_output = divide(token_input[1], token_input[2])
    elif token_input[0] == "square":
        user_output = square(token_input[1])
    elif token_input[0] == "cube":
        user_output = cube(token_input[1])
    elif token_input[0] == "pow":
        user_output = power(token_input[1], token_input[2])
    elif token_input[0] == "mod":
        user_output = mod(token_input[1], token_input[2])
    else:
        pass

    print user_output
