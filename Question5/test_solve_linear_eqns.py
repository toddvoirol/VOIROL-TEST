import unittest
import numpy as np
from solve_linear_eqns import solveEqns

class TestLinearEquationSolver(unittest.TestCase):
    """
    Unit tests for the linear equation solver function.
    Tests a variety of equation formats and numeric values.
    """
    
    def test_example_from_description(self):
        """Test the example provided in the problem description"""
        eqn1 = "1 x + 0 y = 1"
        eqn2 = "1 x + 1 y = 3"
        x, y = solveEqns(eqn1, eqn2)
        self.assertAlmostEqual(x, 1.0)
        self.assertAlmostEqual(y, 2.0)
    
    def test_different_spacing(self):
        """Test equations with different spacing patterns"""
        # No spaces
        eqn1 = "2x+3y=8"
        eqn2 = "1x-1y=1"
        x, y = solveEqns(eqn1, eqn2)
        self.assertAlmostEqual(x, 1.0)
        self.assertAlmostEqual(y, 2.0)
        
        # Extra spaces
        eqn1 = "2  x  +  3  y  =  8"
        eqn2 = "1  x  -  1  y  =  1"
        x, y = solveEqns(eqn1, eqn2)
        self.assertAlmostEqual(x, 1.0)
        self.assertAlmostEqual(y, 2.0)
    
    def test_zero_coefficients(self):
        """Test equations with zero coefficients"""
        eqn1 = "1x + 0y = 5"
        eqn2 = "0x + 1y = 3"
        x, y = solveEqns(eqn1, eqn2)
        self.assertAlmostEqual(x, 5.0)
        self.assertAlmostEqual(y, 3.0)
    
    def test_negative_coefficients(self):
        """Test equations with negative coefficients"""
        eqn1 = "3x - 2y = 5"
        eqn2 = "-1x + 4y = 3"
        x, y = solveEqns(eqn1, eqn2)
        self.assertAlmostEqual(x, 1.0)
        self.assertAlmostEqual(y, 1.0)
    
    def test_implicit_coefficients(self):
        """Test equations with implicit coefficients (x instead of 1x)"""
        eqn1 = "x + y = 5"
        eqn2 = "x - y = 1"
        x, y = solveEqns(eqn1, eqn2)
        self.assertAlmostEqual(x, 3.0)
        self.assertAlmostEqual(y, 2.0)
    
    def test_negative_sign_before_coefficient(self):
        """Test equations with negative sign before the coefficient"""
        eqn1 = "- 2x + 3y = 4"
        eqn2 = "4x - 5y = 10"
        x, y = solveEqns(eqn1, eqn2)
        # Calculate expected values to verify our test is correct
        # Solving manually: 
        # -2x + 3y = 4
        # 4x - 5y = 10
        # Using elimination or substitution method
        expected_x = -2.0
        expected_y = 0.0
        self.assertAlmostEqual(x, expected_x)
        self.assertAlmostEqual(y, expected_y)
    
    def test_with_newlines(self):
        """Test equations with newlines"""
        eqn1 = "2x \n+ 3y = \n8"
        eqn2 = "1x - \n1y = 1"
        x, y = solveEqns(eqn1, eqn2)
        self.assertAlmostEqual(x, 1.0)
        self.assertAlmostEqual(y, 2.0)

if __name__ == '__main__':
    unittest.main()