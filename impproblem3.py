# Two date tuples (day, month, year)
date1 = (15, 5, 2023)  # May 15, 2023
date2 = (25, 12, 2023) # December 25, 2023

# Convert both dates to total days since year 0

# Helper variables for date1
d1, m1, y1 = date1
total_days1 = d1

# Add days from months in current year
for month in range(1, m1):
    if month == 2:
        if (y1 % 400 == 0) or (y1 % 100 != 0 and y1 % 4 == 0):
            total_days1 += 29  # Leap year February
        else:
            total_days1 += 28
    elif month in [4, 6, 9, 11]:
        total_days1 += 30
    else:
        total_days1 += 31

# Add days from previous years
for year in range(1, y1):
    if (year % 400 == 0) or (year % 100 != 0 and year % 4 == 0):
        total_days1 += 366  # Leap year
    else:
        total_days1 += 365

# Helper variables for date2
d2, m2, y2 = date2
total_days2 = d2

# Add days from months in current year
for month in range(1, m2):
    if month == 2:
        if (y2 % 400 == 0) or (y2 % 100 != 0 and y2 % 4 == 0):
            total_days2 += 29  # Leap year February
        else:
            total_days2 += 28
    elif month in [4, 6, 9, 11]:
        total_days2 += 30
    else:
        total_days2 += 31

# Add days from previous years
for year in range(1, y2):
    if (year % 400 == 0) or (year % 100 != 0 and year % 4 == 0):
        total_days2 += 366  # Leap year
    else:
        total_days2 += 365

# Calculate absolute difference
days_difference = abs(total_days2 - total_days1)

# Print results
print(f"Date 1: {date1[0]}/{date1[1]}/{date1[2]}")
print(f"Date 2: {date2[0]}/{date2[1]}/{date2[2]}")
print(f"Number of days between: {days_difference} days")