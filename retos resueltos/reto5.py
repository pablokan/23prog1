# p and (not(q) or r)
def isLeapYear(a):
    p = a % 4 == 0
    q = a % 100 == 0
    r = a % 400 == 0
    if p and (not(q) or r):
        return True
    else:
        return False

assert isLeapYear(1999) == False
assert isLeapYear(2000) == True
assert isLeapYear(2001) == False
assert isLeapYear(2004) == True
assert isLeapYear(2100) == False
assert isLeapYear(2400) == True