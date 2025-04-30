# operator overlaoding 
class Complex:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag
    def __str__(self):
        return f"{self.real} + {self.imag}i"
    def add(self, other):
        if isinstance(other, complex):   
            return complex(self.real + other.real, self.imag + other.imag)
        else:
            raise TypeError("Unsupported operand type for +")
    def __sub__(self, other):
        if isinstance(other, complex):
            print("the substration is:")
            return complex(self.real - other.real, self.imag - other.imag)
        else:
            raise TypeError("Unsupported operand type for -")
    def __mul__(self, other):
        if isinstance(other, complex):
            return complex(self.real * other.real - self.imag * other.imag, self.imag * other
                          .real + self.real * other.imag)
        else:
            raise TypeError("Unsupported operand type for *")
    def __del__(self):
        print("Complex number deleted")
    
    com1 = complex(5,6)
    print(com1)
    com2 = complex(7,8)
    print(com2)
    print(com1 + com2)  
    print(com1 - com2)
    print(com1 * com2)
    del com1
    del com2