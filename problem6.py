fahrenheit = [32, 68, 95, 104, 212]
print("Fahrenheit temperatures:", fahrenheit)

celsius = [(f-32)*5/9 for f in fahrenheit]
print("Celsius temperatures:", celsius)