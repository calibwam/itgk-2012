days = ['man','tue','wed','thu','fri','sat','sun']

def is_leap_year(year):
    if not year % 400:
        return True
    elif not year % 100:
        return False
    elif not year % 4:
        return True

def weekday_newyear(year):
    day = 0
    for x in range(1900,year):
        if is_leap_year(x):
            day += 2
        else:
            day += 1
    return day % 7

def is_workday(weekday):
    if 0 <= weekday < 5:
        return True
    return False

def workdays_in_year(year):
    current_day = weekday_newyear(year)
    workdays = 0
    days_of_year = 0
    if is_leap_year(year):
        days_of_year = 366
    else:
        days_of_year = 365
    for day in range(days_of_year):
        if is_workday(current_day):
            workdays += 1
        current_day = (current_day + 1) %7
    return workdays

for a in range(1900,1920):
    print(a, workdays_in_year(a))
    #print(a, days[weekday_newyear(a)])
