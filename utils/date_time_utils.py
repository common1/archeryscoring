from datetime import date, timedelta

def weeknum(dayname):
    if dayname == 'Monday':   return 0
    if dayname == 'Tuesday':  return 1
    if dayname == 'Wednesday':return 2
    if dayname == 'Thursday': return 3
    if dayname == 'Friday':   return 4
    if dayname == 'Saturday': return 5
    if dayname == 'Sunday':   return 6

def alldays(year, dayOfWeek):
    d = date(year, 1, 1)
    d += timedelta(days = (weeknum(dayOfWeek) - d.weekday()) % 7)
    while d.year == year:
        yield d
        d += timedelta(days = 7)


 # Indoor 18 meter Donderdag 18 December 1025
 
# for d in alldays(2020,'Sunday'):
#     print(d)
