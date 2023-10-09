import numpy as np
class Matrix:
    def __init__(self, rows, cols, sparse=False):
        self.rows = rows
        self.cols = cols
        self.sparse = sparse
        self.matrix = {}

    def __getitem__(self, index):
        if self.sparse:
            return self.matrix.get(index, 0)
        else:
            return self.matrix[index]

    def __setitem__(self, index, value):
        self.matrix[index] = value
    #сложение матриц
    def __add__(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Matrices must have the same dimensions to add them.")
        result = Matrix(self.rows, self.cols, sparse=self.sparse)
        for i in range(self.rows):
            for j in range(self.cols):
                index = (i, j)
                result[index] = self[index] + other[index]
        return result
    #вычитание матриц
    def __sub__(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Matrices must have the same dimensions to subtract them.")
        result = Matrix(self.rows, self.cols, sparse=self.sparse)
        for i in range(self.rows):
            for j in range(self.cols):
                index = (i, j)
                result[index] = self[index] - other[index]
        return result
    #умножение матриц
    def __mul__(self, other):
        if self.cols != other.rows:
            raise ValueError("The number of columns in the first matrix must match the number of rows in the second matrix.")
        result = Matrix(self.rows, other.cols, sparse=self.sparse)
        for i in range(self.rows):
            for j in range(other.cols):
                dot_product = 0
                for k in range(self.cols):
                    dot_product += self[(i, k)] * other[(k, j)]
                result[(i, j)] = dot_product
        return result

    def __str__(self):
        result = ""
        for i in range(self.rows):
            row = ""
            for j in range(self.cols):
                row += str(self[(i, j)]) + " "
            result += row.strip() + "\n"
        return result.strip()
    #транспонирование A
    def transpose(self):
        result = Matrix(self.cols, self.rows, sparse=self.sparse)
        for i in range(self.rows):
            for j in range(self.cols):
                result[(j, i)] = self[(i, j)]
        return result
    #детерминант A
    def determinant(self):
        if self.rows != self.cols:
            raise ValueError("The matrix must be square to calculate the determinant.")
        if self.rows == 1:
            return self[(0, 0)]
        elif self.rows == 2:
            return self[(0, 0)] * self[(1, 1)] - self[(0, 1)] * self[(1, 0)]
        else:
            det = 0
            for j in range(self.cols):
                minor = Matrix(self.rows - 1, self.cols - 1, sparse=self.sparse)
                for i in range(1, self.rows):
                    for k in range(self.cols):
                        if k < j:
                            minor[(i - 1, k)] = self[(i, k)]
                        elif k > j:
                            minor[(i - 1, k - 1)] = self[(i, k)]
                det += ((-1) ** j) * self[(0, j)] * minor.determinant()
            return det
    # инверсирование А(реальзованно с помощью использования numpy и linalg)
    def inversse(self):
        return None
    #преобразование матрицы А в разреженную
    def to_sparse(self):
        if self.sparse:
            return self
        else:
            sparse_matrix = Matrix(self.rows, self.cols, sparse=True)
            for i in range(self.rows):
                for j in range(self.cols):
                    if self[(i, j)] != 0:
                        sparse_matrix[(i, j)] = self[(i, j)]
            return sparse_matrix
    #преобразование матрицы в плотную матрицу
    def to_dense(self):
        if not self.sparse:
            return self
        else:
            dense_matrix = Matrix(self.rows, self.cols, sparse=False)
            for i in range(self.rows):
                for j in range(self.cols):
                    dense_matrix[(i, j)] = self[(i, j)]
            return dense_matrix


def main():
    A = Matrix(3, 3)
    A[(0, 0)] = 1
    A[(0, 1)] = 0
    A[(0, 2)] = 0
    A[(1, 0)] = 2
    A[(1, 1)] = -1
    A[(1, 2)] = 0
    A[(2, 0)] = 1
    A[(2, 1)] = 0
    A[(2, 2)] = 1
    A1 = np.array([[1, 0, 0],[2, -1, 0], [1,0,1]])
    A_inv = np.linalg.inv(A1)
    B = Matrix(3, 3)
    B[(0, 0)] = 9
    B[(0, 1)] = 8
    B[(0, 2)] = 7
    B[(1, 0)] = 6
    B[(1, 1)] = 5
    B[(1, 2)] = 4
    B[(2, 0)] = 3
    B[(2, 1)] = 2
    B[(2, 2)] = 1

    print("A + B:")
    print(A + B)

    print("A - B:")
    print(A - B)

    print("A * B:")
    print(A * B)

    print("A transposed:")
    print(A.transpose())

    print("A determinant:")
    print(A.determinant())

    print("A inverse:")
    print(np.linalg.inv(A1))

    print("A to sparse:")
    print(A.to_sparse())

    print("A to dense:")
    print(A.to_dense())


if __name__ == "__main__":
    main()