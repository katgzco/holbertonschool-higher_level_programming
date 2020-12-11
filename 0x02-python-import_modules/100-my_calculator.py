#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div
    length = len(sys.argv)
    if length != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    num1 = int((sys.argv[1]))
    num2 = int((sys.argv[3]))
    sign = (sys.argv[2])
    if (sign == "+"):
        result = add(num1, num2)
    elif (sign == "-"):
        result = sub(num1, num2)
    elif (sign == "*"):
        result = mul(num1, num2)
    elif (sign == "/"):
        result = div(num1, num2)
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
    print("{} {} {} = {}".format(num1, sign, num2, result))
