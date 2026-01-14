def date_diff(date1, date2):
    
    d1, m1, y1 = map(int, date1.split("-"))
    d2, m2, y2 = map(int, date2.split("-"))

    if y1 == y2:
        return day_of_year(d2, m2, y2) - day_of_year(d1, m1, y1) + 1
    days = day_in_year(y1) - day_of_year(d1, m1, y1) + 1

    for year in range(y1 + 1, y2):
        days += day_in_year(year)

    days += day_of_year(d2, m2, y2)

    return days

print(date_diff("25-12-1999", "9-3-2000")) # 76