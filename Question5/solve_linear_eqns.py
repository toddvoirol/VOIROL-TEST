import numpy as np

def solveEqns(eqn1, eqn2):
    """
    Solves a system of two linear equations in the form "a x + b y = c"
    
    Args:
        eqn1 (str): First equation in the form "a x + b y = c"
        eqn2 (str): Second equation in the form "a x + b y = c"
    
    Returns:
        tuple: Solution (x, y) as a 2-element tuple of float values
    """
    # Clean up the equations by removing extra spaces and newlines
    eqn1 = ' '.join(eqn1.replace('\n', ' ').split())
    eqn2 = ' '.join(eqn2.replace('\n', ' ').split())
    
    def extract_coefficients(equation):
        """Extract the coefficients (a, b, c) from an equation string of form 'a x + b y = c'"""
        # Split the equation at the equals sign
        left_side, right_side = equation.split('=')
        
        # Extract constant c from right side
        c = int(right_side.strip())
        
        # Extract coefficients using a simpler approach
        parts = left_side.replace('x', ' x ').replace('y', ' y ').split()
        
        # Initialize coefficients
        a, b = 0, 0
        
        # Process each part to find coefficients
        i = 0
        while i < len(parts):
            if 'x' in parts[i]:
                # Found x variable, get its coefficient
                if i == 0 or parts[i-1] == '+':
                    a = 1  # Implied coefficient is 1
                elif parts[i-1] == '-':
                    a = -1  # Implied coefficient is -1
                else:
                    a = int(parts[i-1])  # Explicit coefficient
                    if i >= 2 and parts[i-2] == '-':
                        a = -a  # Handle negative sign
            
            elif 'y' in parts[i]:
                # Found y variable, get its coefficient
                if i == 0 or parts[i-1] == '+':
                    b = 1  # Implied coefficient is 1
                elif parts[i-1] == '-':
                    b = -1  # Implied coefficient is -1
                else:
                    b = int(parts[i-1])  # Explicit coefficient
                    if i >= 2 and parts[i-2] == '-':
                        b = -b  # Handle negative sign
            i += 1
        
        return a, b, c
    
    # Extract coefficients from both equations
    a1, b1, c1 = extract_coefficients(eqn1)
    a2, b2, c2 = extract_coefficients(eqn2)
    
    # Create coefficient matrix and constant vector
    A = np.array([[a1, b1], [a2, b2]])
    B = np.array([c1, c2])
    
    # Solve the system of equations
    solution = np.linalg.solve(A, B)
    
    # Return as a tuple of float values
    return (float(solution[0]), float(solution[1]))

# Test example
if __name__ == "__main__":
    # Test with the example from the problem statement
    eqn1 = "1 x + 0 y = 1"
    eqn2 = "1 x + 1 y = 3"
    result = solveEqns(eqn1, eqn2)
    print(f"Solution: x = {result[0]}, y = {result[1]}")
    # Expected output: x = 1.0, y = 2.0
    
    # Additional test cases
    test_cases = [
        ("2x + 3y = 8", "1x - 1y = 1"),
        ("3 x + 2 y = 14", "5 x - 1 y = 17"),
        ("1x + 0y = 5", "0x + 1y = 3")
    ]
    
    for tc_eqn1, tc_eqn2 in test_cases:
        result = solveEqns(tc_eqn1, tc_eqn2)
        print(f"Equations: '{tc_eqn1}' and '{tc_eqn2}'")
        print(f"Solution: x = {result[0]}, y = {result[1]}")
        print("---")