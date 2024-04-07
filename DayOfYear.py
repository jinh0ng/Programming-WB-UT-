# File: DayOfYear.py
# Student: Yejin Hong   
# UT EID: yh25386
# Course Name: CS303E
# 
# Date: 02/13/24
# Description of Program: This program computes the ordinal date for a given date.

# Function to check if a year is a leap year
def is_leap_year(year):
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False

# Function to compute the ordinal date
def compute_ordinal_date(year, month, day):
    # Check if it's a leap year
    if year % 400 == 0:
        is_leap = True
    elif year % 100 == 0:
        is_leap = False
    elif year % 4 == 0:
        is_leap = True
    else:
        is_leap = False

    # Check if the month is valid
    if month < 1 or month > 12:
        return "Illegal date entered!"

    # Check if the day is valid
    if (month == 2 and is_leap) or (month in [4, 6, 9, 11]):
        if day < 1 or day > 29:
            return "Illegal date entered!"
    elif month == 2 and not is_leap:
        if day < 1 or day > 28:
            return "Illegal date entered!"
    else:
        if day < 1 or day > 31:
            return "Illegal date entered!"

    # Compute the ordinal date
    ordinal_date = day
    if month >= 2:
        ordinal_date += 31
    if month >= 3 and is_leap:
        ordinal_date += 29
    elif month >= 3:
        ordinal_date += 28
    if month >= 4:
        ordinal_date += 31
    if month >= 5:
        ordinal_date += 30
    if month >= 6:
        ordinal_date += 31
    if month >= 7:
        ordinal_date += 30
    if month >= 8:
        ordinal_date += 31
    if month >= 9:
        ordinal_date += 31
    if month >= 10:
        ordinal_date += 30
    if month >= 11:
        ordinal_date += 31

    return ordinal_date

def main():

    year = int(input("Specify a year: "))
    month = int(input("Specify a month (1-12): "))
    day = int(input("Specify a day of the month: "))

    # Compute the ordinal date
    ordinal_date = compute_ordinal_date(year, month, day)

    # Print the result
    if type(ordinal_date) == int:
        print(f"{month}/{day}/{year} is day {ordinal_date} of the year.")
    else:
        print(ordinal_date)

if __name__ == "__main__":
    main()