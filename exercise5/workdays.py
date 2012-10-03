days = [0,'man','tue','wed','thu','fri','sat','sun']
def weekday_newyear(year):
    day = 1
    for x in range(1900,year):
        if ((year % 4 == 0) or ((year % 100 == 0) and (year % 400 !=0))):
            day += 2
        else:
            day +=1
    return day % 7

def is_workday(weekday):
    if 0 < weekday < 6:
        return True
    return False

for a in range(1900,1920):
    print(a, days[weekday_newyear(a)])
