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
    
    # Extract coefficients using simple string operations
    def extract_coefficients(equation):
        # Split the equation at the equals sign
        left_side, right_side = equation.split('=')
        
        # Get the constant (c) from the right side
        c = int(right_side.strip())
        
        # Find the position of 'x' and 'y' in the left side
        x_index = left_side.find('x')
        y_index = left_side.find('y')
        
        # Extract the coefficient of x
        x_part = left_side[:x_index].strip()
        # If x_part is empty or just a '+', coefficient is 1
        # If x_part is '-', coefficient is -1
        if not x_part or x_part == '+':
            a = 1
        elif x_part == '-':
            a = -1
        else:
            a = int(x_part)
        
        # Extract the coefficient of y
        # Find the part between 'x' and 'y'
        middle_part = left_side[x_index+1:y_index].strip()
        if middle_part.startswith('+'):
            middle_part = middle_part[1:].strip()  # Remove the '+' sign
            
        if not middle_part:
            b = 1
        elif middle_part == '-':
            b = -1
        else:
            b = int(middle_part)
            
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
    eqn1 = "1 x + 0 y = 1"
    eqn2 = "1 x + 1 y = 3"
    result = solveEqns(eqn1, eqn2)
    print(f"Solution: x = {result[0]}, y = {result[1]}")
    # Expected output: x = 1.0, y = 2.0