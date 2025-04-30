import csv

students_data = {}

try:
    with open('10 File hendling/2nd/students.csv', mode='r', newline='') as file:
        reader = csv.reader(file)
        headers = next(reader) 

        for row in reader:
            if len(row) != 5:
                print(f"Skipping invalid row: {row}")
                continue  

            rollno = int(row[0])
            name = row[1]
            sub1 = int(row[2])
            sub2 = int(row[3])
            sub3 = int(row[4])
            total = sub1 + sub2 + sub3

            students_data[rollno] = {
                'Name': name,
                'Subject 1': sub1,
                'Subject 2': sub2,
                'Subject 3': sub3,
                'Total Marks': total
            }

except FileNotFoundError:
    print("Error: File 'students.csv' not found.")
except Exception as e:
    print(f"An error occurred: {e}")

for rollno, info in students_data.items():
    print(f"Roll No: {rollno}")
    for key, value in info.items():
        print(f"  {key}: {value}")
    print("-" * 40)
