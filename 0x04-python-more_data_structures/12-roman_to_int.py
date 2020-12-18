def roman_to_int(r_s):
    if r_s and type(r_s) == str:
        r_n = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        num = 0
        lt = len(r_s)
        for let in range(len(r_s)):
            if let < lt - 1 and r_n.get(r_s[let]) < r_n.get(r_s[let + 1]):
                num -= r_n[r_s[let]]
            else:
                num += r_n[r_s[let]]
    return num
