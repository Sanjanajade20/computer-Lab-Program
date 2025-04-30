# Write a program to create a class Date that has a list containing day, month and year attributes. Define an overloaded == operator to compare two Date object

class Date:
    def __init__(self, day, month, year):
        self.date = [day, month, year]

    def __eq__(self, other):
        if isinstance(other, Date):
            return self.date == other.date
        return False

    def display(self):
        return f"{self.date[0]:02d}/{self.date[1]:02d}/{self.date[2]}"

# Example usage
date1 = Date(24, 4, 2025)
date2 = Date(24, 4, 2025)
date3 = Date(25, 4, 2025)

print("Date 1:", date1.display())
print("Date 2:", date2.display())
print("Date 3:", date3.display())

# Compare dates using overloaded ==
print("Date1 == Date2:", date1 == date2)  # True
print("Date1 == Date3:", date1 == date3)  # False
