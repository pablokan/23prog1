def inputDate(datePar):
    d, m, a = [int(x) for x in datePar.split('/')]
    from datetime import date
    print(date(a, m, d))

inputDate('31/05/2001')
