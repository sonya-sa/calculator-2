"""A prefix-notation calculator.

Using the arithmetic.py file from Calculator Part 1, create the
calculator program yourself in this file.
"""

from arithmetic import *

# Your code goes here

while True:

    user_input = raw_input("> ")
    token_input = user_input.split(" ")
    token_func = token_input.pop(0)

    if token_func == "q":
        quit()

    digit_input = []
    for i in token_input:
        if i.isdigit():
            digit_input.append(float(i))
        else:
            continue

    if token_func == "+":
        user_output = add(digit_input)
    elif token_func == "-":
        user_output = subtract(digit_input)
    elif token_func == "*":
        user_output = multiply(digit_input)
    elif token_func == "/":
        user_output = divide(digit_input)
    elif token_func == "square":
        user_output = square(digit_input[0])
    elif token_func == "cube":
        user_output = cube(digit_input[0])
    elif token_func == "power":
        user_output = power(digit_input)
    elif token_func == "mod":
        user_output = mod(digit_input[0:1])
    else:
        continue

    print user_output
