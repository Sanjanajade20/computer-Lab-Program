import random

nums = [random.randint(1, 10) for _ in range(20)]
print("Generated list:", nums)

target = int(input("Enter number to find: "))

positions = [i for i, x in enumerate(nums) if x == target]
print(f"Number {target} found at positions:", positions)