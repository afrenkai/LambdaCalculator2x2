import unittest
from eigenvalues import calculate_eigenvalues
from eigenvectors import calculate_eigenvectors
class TestCalculateEigenvalues(unittest.TestCase):
    def test_basic_matrix(self):
        matrix = [[5, 2], [8, 4]]
        expected = [8.5311, 0.4689]
        self.assertEqual(calculate_eigenvalues(matrix), expected)
    
    def test_identity_matrix(self):
        matrix = [[1, 0], [0, 1]]
        expected = [1.0, 1.0]
        self.assertEqual(calculate_eigenvalues(matrix), expected)
    
    def test_zero_matrix(self):
        matrix = [[0, 0], [0, 0]]
        expected = [0.0, 0.0]
        self.assertEqual(calculate_eigenvalues(matrix), expected)


class TestCalculateEigenvectors(unittest.TestCase):
    def test_basic_matrix(self):
        matrix = [[5, 2], [8, 4]]
        expected = [[0.49282869280659514, 0.8701263583793694], [-0.4038018054942862, 0.9148464908822433]]
        self.assertEqual(calculate_eigenvectors(matrix, calculate_eigenvalues(matrix)), expected)
if __name__ == '__main__':
    unittest.main()