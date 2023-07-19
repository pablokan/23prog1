def edad(fN):
    from datetime import date
    d, m, a = [int(e) for e in fN.split('/')]
    hoy = date.today()
    e = hoy.year - a
    if (m > hoy.month) or (m == hoy.month and d > hoy.day):
        e -= 1
    return e

if __name__ == '__main__':
    print(edad('30/06/2005'))
    print(edad('02/07/2005'))

