#!/usr/bin/python3
for num in range(0, 8):
    num2 = num + 1
    for num2 in range(num2, 10):
        print("{:d}{:d}".format(num, num2), end=", ")
print("{:d}{:d}".format(num + 1, num2))
