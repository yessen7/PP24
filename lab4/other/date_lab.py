import datetime
import math


# Write a Python program to subtract five days from current date.
# Write a Python program to print yesterday, today, tomorrow.
# Write a Python program to drop microseconds from datetime.
# Write a Python program to calculate two date difference in seconds.

current = datetime.datetime.now()


def minus_5_days(time):
    print(time.day - 5)


minus_5_days(current)


def yes_tod_tom(time):
    print(time.day-1, time.day, time.day+1)


yes_tod_tom(current)


def no_microseconds(time):
    print(time.replace(microsecond=0))


no_microseconds(current)


def date_difference(date1, date2):
    # Convert the date strings to datetime objects
    # Calculate the time difference in seconds
    difference_days = abs((date1 - date2).days)
    print("Days: ", difference_days, "Years: ", difference_days/365)


my_birthday = "2004-05-07 22:22:22.666"
dt_object = datetime.datetime.strptime(my_birthday, "%Y-%m-%d %H:%M:%S.%f")

date_difference(dt_object, current)
