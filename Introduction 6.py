def is_leap(year):
    leap = False
    if year%400==0 or (year%4==0 and not year%100==0):
        leap=True
    return leap