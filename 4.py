
num = int(input("Enter a number: "))


if num <= 1:
    is_prime = False
else:
    is_prime = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break


num_str = str(num)
num_digits = len(num_str)
sum_of_powers = 0
for digit in num_str:
    sum_of_powers += int(digit) ** num_digits
is_armstrong = (sum_of_powers == num)

is_palindrome = (str(num) == str(num)[::-1])


print(f"{num} is prime: {is_prime}")
print(f"{num} is Armstrong: {is_armstrong}")
print(f"{num} is palindrome: {is_palindrome}")
