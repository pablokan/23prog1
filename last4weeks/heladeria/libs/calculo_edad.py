from datetime import date
def edad(fN):
    hoy = date.today()
    dN, mN, aN = fN.split("/")
    dN = int(dN)
    mN = int(mN)
    aN = int(aN)
    dH = hoy.day
    mH = hoy.month
    aH = hoy.year
    e = aH - aN
    if (mN > mH) or (mN == mH and dN > dH):
        e -= 1
    return e

if __name__ == "__main__":
    print(edad("03/06/1965"))

