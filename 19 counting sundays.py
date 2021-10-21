count = 0
day = 7
for year in range(1901, 2000):
    leap = year % 4 == 0 and (year % 400 == 0 or year % 100 != 0)
    days = [31, [28, 29][leap], 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    month = 0
    while month < 12:
        day += 7
        if day > days[month]:
            day -= days[month]
            month += 1
        if day == 1:
            count += 1
print(count)
