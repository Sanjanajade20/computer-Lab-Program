s1 = int(input("Enter the marks of Maths: "))
s2 = int(input("Enter the marks of Physics: "))
s3 = int(input("Enter the marks of Biology: "))


total = s1 + s2 + s3
average = (s1 + s2 + s3) / 3

print("The total is:", total)
print("The average is:", average)


if s1 < 39 or s2 < 39 or s3 < 39:
    print("Fail")
else:
    
    if 0 <= s1 <= 39:
        print("Grade for Maths: F")
    elif 40 <= s1 <= 44:
        print("Grade for Maths: P")
    elif 45 <= s1 <= 49:
        print("Grade for Maths: C")
    elif 50 <= s1 <= 54:
        print("Grade for Maths: B")
    elif 55 <= s1 <= 59:
        print("Grade for Maths: B+")
    elif 60 <= s1 <= 69:
        print("Grade for Maths: A")
    elif 70 <= s1 <= 79:
        print("Grade for Maths: A+")
    elif 80 <= s1 <= 100:
        print("Grade for Maths: O")

    
    if 0 <= s2 <= 39:
        print("Grade for Physics: F")
    elif 40 <= s2 <= 44:
        print("Grade for Physics: P")
    elif 45 <= s2 <= 49:
        print("Grade for Physics: C")
    elif 50 <= s2 <= 54:
        print("Grade for Physics: B")
    elif 55 <= s2 <= 59:
        print("Grade for Physics: B+")
    elif 60 <= s2 <= 69:
        print("Grade for Physics: A")
    elif 70 <= s2 <= 79:
        print("Grade for Physics: A+")
    elif 80 <= s2 <= 100:
        print("Grade for Physics: O")

    
    if 0 <= s3 <= 39:
        print("Grade for Biology: F")
    elif 40 <= s3 <= 44:
        print("Grade for Biology: P")
    elif 45 <= s3 <= 49:
        print("Grade for Biology: C")
    elif 50 <= s3 <= 54:
        print("Grade for Biology: B")
    elif 55 <= s3 <= 59:
        print("Grade for Biology: B+")
    elif 60 <= s3 <= 69:
        print("Grade for Biology: A")
    elif 70 <= s3 <= 79:
        print("Grade for Biology: A+")
    elif 80 <= s3 <= 100:
        print("Grade for Biology: O")
