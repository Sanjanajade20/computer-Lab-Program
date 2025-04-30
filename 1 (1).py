import csv

data = [
    ["Name", "Age", "City"],
    ["Jiya", 17, "Gandhinagar"],
    ["nishu", 19, "Patan"],
    ["Honey", 35, "Ahemdabad"]
]

filename = "people.csv"

with open(filename, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)

print(f"CSV file '{filename}' created successfully!")
