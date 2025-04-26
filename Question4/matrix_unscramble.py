#!/usr/bin/env python3
"""
Matrix Unscrambler

This program takes a single list of integers and extracts two matrices from it:
- A 2x2 matrix (matrix a)
- A 2xN matrix (matrix b) where N is determined by the remaining elements

Author: GitHub Copilot
Date: April 26, 2025
"""

import numpy as np

def unscramble_matrices(raw_data):
    """
    Unscramble the raw data into two matrices: a 2x2 matrix and a 2xN matrix.
    
    Args:
        raw_data (list): A list of integers containing data for both matrices.
        
    Returns:
        tuple: A tuple containing (matrix_a, matrix_b) where:
            - matrix_a is a 2x2 NumPy array
            - matrix_b is a 2xN NumPy array
    """
    # First, we know matrix a is 2x2, so it takes the first 4 elements
    matrix_a_data = raw_data[:4]
    matrix_a = np.array(matrix_a_data).reshape(2, 2)
    
    # The remaining elements belong to matrix b
    matrix_b_data = raw_data[4:]
    
    # Calculate how many columns matrix b has
    n_elements_b = len(matrix_b_data)
    n_cols_b = n_elements_b // 2
    
    # Reshape the remaining data into a 2xN matrix
    matrix_b = np.array(matrix_b_data).reshape(n_cols_b, 2).transpose()
    
    return matrix_a, matrix_b

# Example usage
if __name__ == "__main__":
    # Example from the problem description
    raw_data = [1, 2, 3, 4, 6, 5, 4, 3, 2, 1]
    
    a, b = unscramble_matrices(raw_data)
    
    print("Matrix a (2x2):")
    print(a)
    print("\nMatrix b (2xN):")
    print(b)
    
    # Additional example for verification
    print("\n--- Additional Example ---")
    test_data = [10, 20, 30, 40, 1, 2, 3, 4, 5, 6, 7, 8]
    a2, b2 = unscramble_matrices(test_data)
    print("Matrix a (2x2):")
    print(a2)
    print("\nMatrix b (2xN):")
    print(b2)