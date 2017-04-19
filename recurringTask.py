# Repeat every k weeks on specified days of the week
# n = dates for which task is scheduled
# return an array of the first n dates
# Input firstDate,

# find day of first date
    # calculate abs between that and rest of dates

from datetime import datetime, timedelta


def recurringTask(firstDate, k, daysOfTheWeek, n):

    days_of_week = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
    week = ['Thursday', 'Wednesday', 'Tuesday', 'Monday', 'Sunday', 'Saturday', 'Friday']
    dates = []

    count = 0

    numbers = [0]

    date_format = "%d/%m/%Y"
    anchor = datetime.strptime("01/01/2015", date_format)
    new_anchor = datetime.strptime(firstDate, date_format)

    delta = anchor - new_anchor
    delta = delta.days

    delta = delta % 7

    dif = delta
    first_day = week[dif]


    for i in daysOfTheWeek:
        if days_of_week.index(i) > days_of_week.index(first_day):
            new_num = abs(days_of_week.index(first_day) - days_of_week.index(i))
            numbers.append(new_num)
        elif days_of_week.index(i) < days_of_week.index(first_day):
            new_num = 7 - (abs(days_of_week.index(first_day) - days_of_week.index(i)))
            numbers.append(new_num)

    numbers.sort()

    print(numbers)

    while count < n:

        firstDate = new_anchor

        for j in numbers:
            firstDate += timedelta(days=j)
            dates.append(datetime.strftime(firstDate, date_format))
            firstDate = new_anchor

        new_anchor += timedelta(days=(7*k))
        count += 1

    return dates[:n]

# Test case
print(recurringTask("01/02/2100", 4, ["Sunday", "Monday", 'Tuesday'], 8))
