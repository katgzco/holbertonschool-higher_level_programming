#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    length = len(sys.argv)
    if length > 1:
        arg = "argument:" if (length == 2) else "arguments:"
        print("{} {}".format(length-1, arg))
        for i in range(1, length):
            print("{}: {}".format(i, (sys.argv[i])))
    else:
        print("0 arguments.")
