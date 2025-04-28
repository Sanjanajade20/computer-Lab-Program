lst = ['madam','Python','malayalam',12321]
palindromes = list(filter(lambda x: isinstance(x, str) and x == x[::-1], lst))
print(palindromes)

