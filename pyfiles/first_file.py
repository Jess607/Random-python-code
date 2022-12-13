def is_leap(year):
    leap = False
    if year%4==0:
        if year%100!=0:
            return not leap
        elif year%100==0 and year%400==0:
            return not leap
        elif year%100==0 and year%400!=0:
            return leap

    elif year%4!=0:
         return leap



year = int(input('Enter:'))
print(is_leap(year))
