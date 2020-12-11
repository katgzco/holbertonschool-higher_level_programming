#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    hold = 0
    length = len(sys.argv)
    for i in range(1, length):
        hold += int((sys.argv[i]))
    print(hold)
