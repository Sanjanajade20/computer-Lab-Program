# Write a program that implements a Matrix class and performs addition, multiplication and transpose operations on 3x3 matrices
class Matrix:
    def __init__(self, data):
        self.data = data

    def display(self):
        for row in self.data:
            print(row)

    def add(self, other):
        result = []
        for i in range(3):
            row = []
            for j in range(3):
                row.append(self.data[i][j] + other.data[i][j])
            result.append(row)
        return Matrix(result)

    def multiply(self, other):
        result = []
        for i in range(3):
            row = []
            for j in range(3):
                val = 0
                for k in range(3):
                    val += self.data[i][k] * other.data[k][j]
                row.append(val)
            result.append(row)
        return Matrix(result)

    def transpose(self):
        result = []
        for i in range(3):
            row = []
            for j in range(3):
                row.append(self.data[j][i])
            result.append(row)
        return Matrix(result)

def input_matrix(n):
    print(f"Enter values for Matrix {n} (3 rows, 3 numbers each):")
    matrix = []
    for i in range(3):
        while True:
            try:
                row = list(map(int, input(f"Row {i+1}: ").split()))
                if len(row) != 3:
                    raise ValueError("Please enter exactly 3 numbers.")
                matrix.append(row)
                break
            except ValueError as e:
                print(e)
    return Matrix(matrix)

matrix1 = input_matrix(1)
matrix2 = input_matrix(2)

print("\nMatrix 1:")
matrix1.display()
print("\nMatrix 2:")
matrix2.display()

print("\nAddition of Matrix 1 and Matrix 2:")
matrix1.add(matrix2).display()

print("\nMultiplication of Matrix 1 and Matrix 2:")
matrix1.multiply(matrix2).display()

print("\nTranspose of Matrix 1:")
matrix1.transpose().display()

print("\nTranspose of Matrix 2:")
matrix2.transpose().display()
