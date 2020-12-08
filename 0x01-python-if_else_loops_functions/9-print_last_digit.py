#!/usr/bin/python3
def print_last_digit(number):
    """prints the last digit of a number."""
    lastdigit = int(str(number)[-1])
    print(lastdigit, end="")
    return lastdigit
