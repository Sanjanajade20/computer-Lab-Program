prices = {
    'apple': 1.20,
    'banana': 0.50,
    'milk': 2.50,
    'bread': 1.80
}
quantities = {
    'apple': 3,
    'banana': 6,
    'milk': 2,
    'bread': 1
}
total = 0
for item in prices:
    if item in quantities:
        total += prices[item] * quantities[item]

print(f"Total bill: ${total:.2f}")