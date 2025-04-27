import unittest
import numpy as np
from matrix_unscramble import unscramble_matrices

class TestMatrixUnscramble(unittest.TestCase):
    """
    Unit tests for the matrix unscrambling function.
    Tests various input sizes and edge cases.
    """
    
    def test_example_from_description(self):
        """Test the example provided in the problem description"""
        raw_data = [1, 2, 3, 4, 6, 5, 4, 3, 2, 1]
        
        a, b = unscramble_matrices(raw_data)
        
        # Check matrix a
        expected_a = np.array([[1, 2], [3, 4]])
        np.testing.assert_array_equal(a, expected_a)
        
        # Check matrix b
        expected_b = np.array([[6, 5], [4, 3], [2, 1]]).T  # Transpose to get 2x3
        np.testing.assert_array_equal(b, expected_b)
    
    def test_different_size_b(self):
        """Test with a matrix b of different size"""
        # Matrix a: 2x2, Matrix b: 2x4
        raw_data = [10, 20, 30, 40, 1, 2, 3, 4, 5, 6, 7, 8]
        
        a, b = unscramble_matrices(raw_data)
        
        # Check matrix a
        expected_a = np.array([[10, 20], [30, 40]])
        np.testing.assert_array_equal(a, expected_a)
        
        # Check matrix b
        expected_b = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
        np.testing.assert_array_equal(b, expected_b)
    
    def test_minimum_size_b(self):
        """Test with a matrix b of minimum size (2x1)"""
        raw_data = [1, 2, 3, 4, 5, 6]
        
        a, b = unscramble_matrices(raw_data)
        
        # Check matrix a
        expected_a = np.array([[1, 2], [3, 4]])
        np.testing.assert_array_equal(a, expected_a)
        
        # Check matrix b
        expected_b = np.array([[5], [6]])
        np.testing.assert_array_equal(b, expected_b)
    
    def test_large_size_b(self):
        """Test with a larger matrix b (2x10)"""
        # Create test data: 4 elements for matrix a, 20 elements for matrix b
        matrix_a_data = [1, 2, 3, 4]
        matrix_b_data = list(range(5, 25))  # 20 numbers from 5 to 24
        raw_data = matrix_a_data + matrix_b_data
        
        a, b = unscramble_matrices(raw_data)
        
        # Check matrix a
        expected_a = np.array([[1, 2], [3, 4]])
        np.testing.assert_array_equal(a, expected_a)
        
        # Check matrix b shape
        self.assertEqual(b.shape, (2, 10))
        
        # Check the first few elements of b to ensure correct formatting
        self.assertEqual(b[0, 0], 5)
        self.assertEqual(b[1, 0], 6)
        self.assertEqual(b[0, 1], 7)
    
    def test_negative_numbers(self):
        """Test with negative numbers in the data"""
        raw_data = [-1, -2, -3, -4, -5, -6, -7, -8]
        
        a, b = unscramble_matrices(raw_data)
        
        # Check matrix a
        expected_a = np.array([[-1, -2], [-3, -4]])
        np.testing.assert_array_equal(a, expected_a)
        
        # Check matrix b
        expected_b = np.array([[-5, -7], [-6, -8]])
        np.testing.assert_array_equal(b, expected_b)
    
    def test_odd_number_of_elements(self):
        """Test error handling with an odd number of elements"""
        # This should raise an error because we need an even number for the 2xN matrices
        raw_data = [1, 2, 3, 4, 5, 6, 7]  # 7 elements (odd number)
        
        # The function should raise a ValueError because the remaining elements 
        # after taking the first 4 for matrix a would be odd (3), which cannot form a 2xN matrix
        with self.assertRaises(ValueError):
            a, b = unscramble_matrices(raw_data)
    
    def test_insufficient_elements(self):
        """Test error handling with insufficient elements for matrix a"""
        # This doesn't have enough elements for matrix a
        raw_data = [1, 2, 3]
        
        # The function should raise an error when there are less than 4 elements
        with self.assertRaises(ValueError):
            a, b = unscramble_matrices(raw_data)

if __name__ == '__main__':
    unittest.main()