# Write a program that creates and uses a Time class to perform various time arithmetic operations

class Time:
    def __init__(self, hours=0, minutes=0, seconds=0):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds
        self.normalize()

    def normalize(self):
        """Normalize time to proper hours, minutes, seconds."""
        total_seconds = self.hours * 3600 + self.minutes * 60 + self.seconds
        self.hours = total_seconds // 3600
        total_seconds %= 3600
        self.minutes = total_seconds // 60
        self.seconds = total_seconds % 60

    def display(self):
        return f"{self.hours:02d}:{self.minutes:02d}:{self.seconds:02d}"

    def to_seconds(self):
        return self.hours * 3600 + self.minutes * 60 + self.seconds

    def add_time(self, other):
        return Time(
            self.hours + other.hours,
            self.minutes + other.minutes,
            self.seconds + other.seconds
        )

    def subtract_time(self, other):
        total_self = self.to_seconds()
        total_other = other.to_seconds()
        if total_self < total_other:
            print("Result would be negative. Returning 00:00:00.")
            return Time()
        total_diff = total_self - total_other
        return Time(0, 0, total_diff)

# Example Usage
t1 = Time(2, 45, 50)
t2 = Time(1, 20, 15)

print("Time 1:", t1.display())
print("Time 2:", t2.display())

sum_time = t1.add_time(t2)
diff_time = t1.subtract_time(t2)

print("Sum:", sum_time.display())
print("Difference:", diff_time.display())
