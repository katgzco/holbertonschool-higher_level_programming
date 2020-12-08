def islower(c):
    """Return True if the letter is lowercase or False."""
    lower = ord(c)
    if (lower >= 97 and lower <= 122):
        return True
    else:
        return False
