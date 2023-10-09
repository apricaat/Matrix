import unittest
from matrix import Matrix
#Код ПО
class TestMatrix(unittest.TestCase):
    def test_addition(self):
        # тест для сложения TDD
        A = Matrix(2, 2)
        A[(0, 0)] = 1
        A[(0, 1)] = 2
        A[(1, 0)] = 3
        A[(1, 1)] = 4

        B = Matrix(2, 2)
        B[(0, 0)] = 5
        B[(0, 1)] = 6
        B[(1, 0)] = 7
        B[(1, 1)] = 8

        C = A + B

        self.assertEqual(C[(0, 0)], 6)
        self.assertEqual(C[(0, 1)], 8)
        self.assertEqual(C[(1, 0)], 10)
        self.assertEqual(C[(1, 1)], 12)
        #различные веса
        A = Matrix(2, 2)
        A[(0, 0)] = 1
        A[(0, 1)] = 2
        A[(1, 0)] = 3
        A[(1, 1)] = 4

        B = Matrix(3, 3)
        B[(0, 0)] = 5
        B[(0, 1)] = 6
        B[(0, 2)] = 7
        B[(1, 0)] = 8
        B[(1, 1)] = 9
        B[(1, 2)] = 10
        B[(2, 0)] = 11
        B[(2, 1)] = 12
        B[(2, 2)] = 13

        with self.assertRaises(ValueError):
            C = A + B

    def test_matrix_minus(self):
        #тест для вычитания TDD
        A = Matrix(2, 2)
        A[(0, 0)] = 1
        A[(0, 1)] = 2
        A[(1, 0)] = 3
        A[(1, 1)] = 4

        B = Matrix(2, 2)
        B[(0, 0)] = 5
        B[(0, 1)] = 6
        B[(1, 0)] = 7
        B[(1, 1)] = 8

        C = A - B

        self.assertEqual(C[(0, 0)], -4)
        self.assertEqual(C[(0, 1)], -4)
        self.assertEqual(C[(1, 0)], -4)
        self.assertEqual(C[(1, 1)], -4)

        #тест различные веса
        A = Matrix(2, 2)
        A[(0, 0)] = 1
        A[(0, 1)] = 2
        A[(1, 0)] = 3
        A[(1, 1)] = 4

        B = Matrix(3, 3)
        B[(0, 0)] = 5
        B[(0, 1)] = 6
        B[(0, 2)] = 7
        B[(1, 0)] = 8
        B[(1, 1)] = 9
        B[(1, 2)] = 10
        B[(2, 0)] = 11
        B[(2, 1)] = 12
        B[(2, 2)] = 13

        with self.assertRaises(ValueError):
            C = A - B

if __name__ == '__main__':
    unittest.main()