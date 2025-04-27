import numpy as np

def solveEqns(eqn1, eqn2):
    """
    Solves a system of two linear equations in the form "a x + b y = c".
    Assumes all coefficients (a, b, c) are non-negative integers.
    
    Args:
        eqn1 (str): First equation in the form "a x + b y = c"
        eqn2 (str): Second equation in the form "a x + b y = c"
    
    Returns:
        tuple: Solution (x, y) as a 2-element tuple of float values
    """
    def get_coefficients(equation):
        """Gets the coefficients (a, b, c) from an equation string"""
        # Clean up the equation by removing newlines and extra spaces
        equation = equation.replace('\n', ' ')
        # Make sure we have single spaces between parts
        equation = ' '.join(equation.split())
        
        # Split into left and right sides
        left_side, right_side = equation.split('=')
        left_side = left_side.strip()
        right_side = right_side.strip()
        
        # Get c (the right side number)
        c = int(right_side)
        
        # Initialize coefficients
        a = 0  # coefficient of x
        b = 0  # coefficient of y
        
        # Split left side into parts
        parts = left_side.split('+')
        
        # Look at each part (term)
        for part in parts:
            part = part.strip()
            if 'x' in part:
                # This part has x
                number = part.replace('x', '').strip()
                if number == '':
                    a = 1
                else:
                    a = int(number)
            elif 'y' in part:
                # This part has y
                number = part.replace('y', '').strip()
                if number == '':
                    b = 1
                else:
                    b = int(number)
        
        return a, b, c
    
    # Get coefficients from both equations
    a1, b1, c1 = get_coefficients(eqn1)
    a2, b2, c2 = get_coefficients(eqn2)
    
    # Use NumPy to solve the system of equations
    A = np.array([[a1, b1], [a2, b2]])
    B = np.array([c1, c2])
    solution = np.linalg.solve(A, B)
    
    # Return the solution as a tuple of floats
    return (float(solution[0]), float(solution[1]))

if __name__ == "__main__":
    # Test with the example from the problem description
    eqn1 = "1 x + 0 y = 1"
    eqn2 = "1 x + 1 y = 3"
    result = solveEqns(eqn1, eqn2)
    print(f"Solution: x = {result[0]}, y = {result[1]}")
    # Expected output: x = 1.0, y = 2.0