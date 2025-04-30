#Implement a String class containing the following functions:
#a. Overloaded += operator function to perform string concatenation
# b. Method toLower() to convert upper case letters to lower case.
# c. Method toUpper() to convert lower case letters to upper cas

class String:
    def __init__(self, value=""):
        self.value = value

    def __iadd__(self, other):
        """Overload the += operator for string concatenation."""
        if isinstance(other, String):
            self.value += other.value
        elif isinstance(other, str):
            self.value += other
        else:
            raise TypeError("Only String or str types can be concatenated.")
        return self

    def toLower(self):
        """Convert the string to lowercase."""
        self.value = self.value.lower()

    def toUpper(self):
        """Convert the string to uppercase."""
        self.value = self.value.upper()

    def __str__(self):
        return self.value

# Example usage
s1 = String(input("1st word"))
s2 = String(input("2nd word"))

print("Original s1:", s1)
print("Original s2:", s2)

# Concatenate using +=
s1 += s2
print("After concatenation:", s1)

# Convert to lowercase
s1.toLower()
print("Lowercase:", s1)

# Convert to uppercase
s1.toUpper()
print("Uppercase:", s1)
