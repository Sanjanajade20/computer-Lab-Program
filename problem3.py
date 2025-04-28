string = input("Enter a string: ")
alphabets = 0
digits = 0
for char in string:
    if 'A' <= char <= 'Z' or 'a' <= char <= 'z':
        alphabets += 1
    elif '0' <= char <= '9':
        digits += 1
print("Alphabets:", alphabets)
print("Digits:", digits)
