# Linear Equation Solver Explanation

## Problem Statement

Create a function `solveEqns(eqn1, eqn2)` that takes a system of linear equations as strings in the form "a x + b y = c" and solves for x and y using NumPy.

## Logic and Solution Breakdown

The solution involves several key steps:

1. **Parsing the input strings** to extract the coefficients and constants
2. **Setting up the system in matrix form** using NumPy arrays
3. **Solving the linear system** using NumPy's linear algebra capabilities
4. **Returning the solution** as a tuple

### Detailed Explanation

```python
import numpy as np
```
- **Import statements**: We import NumPy for its linear algebra functionality.

```python
def solveEqns(eqn1, eqn2):
    """
    Solves a system of two linear equations in the form "a x + b y = c"
    
    Args:
        eqn1 (str): First equation in the form "a x + b y = c"
        eqn2 (str): Second equation in the form "a x + b y = c"
    
    Returns:
        tuple: Solution (x, y) as a 2-element tuple of float values
    """
```
- **Function definition and documentation**: The function takes two string parameters representing linear equations and returns a tuple with the solution.

```python
    # Clean up the equations by removing extra spaces and newlines
    eqn1 = ' '.join(eqn1.replace('\n', ' ').split())
    eqn2 = ' '.join(eqn2.replace('\n', ' ').split())
```
- **Input sanitization**: This normalizes the input by:
  - Replacing newlines with spaces
  - Splitting the string into words and rejoining with single spaces
  - This helps handle inputs where formatting might be inconsistent or include line breaks

```python
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
```
- **Coefficient extraction helper function**: 
  - This function uses basic string operations that are easier for beginners to understand
  - It extracts the coefficients of x and y and the constant from an equation string
  - The function works by:
    1. Splitting the equation at the equals sign to get left and right sides
    2. Getting the constant (c) from the right side
    3. Finding where 'x' and 'y' occur in the left side
    4. Extracting the part before 'x' to get coefficient a
    5. Extracting the part between 'x' and 'y' to get coefficient b
    6. Handling special cases like if the coefficient is 1 (often written without a number)

```python
    # Extract coefficients from both equations
    a1, b1, c1 = extract_coefficients(eqn1)
    a2, b2, c2 = extract_coefficients(eqn2)
```
- **Extract all coefficients**: 
  - Calls the helper function on both equation strings
  - Extracts six values in total: a1, b1, c1 from the first equation and a2, b2, c2 from the second

```python
    # Create coefficient matrix and constant vector
    A = np.array([[a1, b1], [a2, b2]])
    B = np.array([c1, c2])
```
- **Matrix setup**: 
  - Creates matrix A with the coefficients of x and y
  - Creates vector B with the constants
  - This transforms our system into the form Ax = B where x is the vector [x, y] we want to solve for

```python
    # Solve the system of equations
    solution = np.linalg.solve(A, B)
```
- **Linear algebra solution**: 
  - `np.linalg.solve()` is a NumPy function that solves a linear matrix equation
  - It computes the solution to the system of equations

```python
    # Return as a tuple of float values
    return (float(solution[0]), float(solution[1]))
```
- **Result formatting**: 
  - The solution is explicitly converted to float type
  - The solution is returned as a tuple (x, y) as requested in the problem statement

## Beginner-Friendly String Parsing

The updated solution uses a simple string parsing approach instead of regular expressions, making it more accessible for beginners. Here's how it works step-by-step:

### 1. Splitting the Equation

```python
left_side, right_side = equation.split('=')
```

This divides the equation at the equals sign. For "1 x + 0 y = 1":
- `left_side` becomes "1 x + 0 y"
- `right_side` becomes "1"

### 2. Getting the Constant

```python
c = int(right_side.strip())
```

This converts the right side of the equation to an integer after removing any extra spaces.

### 3. Finding Variable Positions

```python
x_index = left_side.find('x')
y_index = left_side.find('y')
```

This finds where the variables 'x' and 'y' appear in the left side. For "1 x + 0 y":
- `x_index` would be 2 (the position of 'x')
- `y_index` would be 8 (the position of 'y')

### 4. Extracting the x Coefficient

```python
x_part = left_side[:x_index].strip()
if not x_part or x_part == '+':
    a = 1
elif x_part == '-':
    a = -1
else:
    a = int(x_part)
```

This gets everything before 'x', then handles special cases:
- If there's nothing or just a '+' before 'x' (like in "+x"), the coefficient is 1
- If there's just a '-' before 'x' (like in "-x"), the coefficient is -1
- Otherwise, convert the string to an integer

### 5. Extracting the y Coefficient

```python
middle_part = left_side[x_index+1:y_index].strip()
if middle_part.startswith('+'):
    middle_part = middle_part[1:].strip()  # Remove the '+' sign
    
if not middle_part:
    b = 1
elif middle_part == '-':
    b = -1
else:
    b = int(middle_part)
```

This gets the part between 'x' and 'y', handles the '+' sign if present, and determines the coefficient with the same rules as for 'x'.

### Benefits of This Approach

1. **More beginner-friendly**: Uses basic string methods that new programmers are likely familiar with
2. **Better readability**: Each step explicitly states what it's trying to extract
3. **Easier to debug**: If something goes wrong, it's easier to figure out which specific step failed
4. **Educational value**: Demonstrates how to break down text parsing into simple steps

## Mathematical Explanation

### Coefficient Matrix

A coefficient matrix is a rectangular array of numbers arranged in rows and columns that represents the coefficients of variables in a system of linear equations. In our case, for a system of two linear equations with two variables (x and y), the coefficient matrix is a 2×2 matrix:

```
A = [a1 b1]
    [a2 b2]
```

Where:
- `a1` is the coefficient of x in the first equation
- `b1` is the coefficient of y in the first equation
- `a2` is the coefficient of x in the second equation
- `b2` is the coefficient of y in the second equation

For example, with the system:
```
1x + 0y = 1
1x + 1y = 3
```

The coefficient matrix is:
```
A = [1 0]
    [1 1]
```

The coefficient matrix encodes the relationships between the variables in our system. Each row corresponds to one equation, and each column corresponds to one variable.

### Constant Vector

A constant vector (sometimes called the "right-hand side" or RHS vector) contains the constant terms from each equation in the system. For our system of two equations, it's a column vector with two elements:

```
B = [c1]
    [c2]
```

Where:
- `c1` is the constant term in the first equation
- `c2` is the constant term in the second equation

For our example:
```
1x + 0y = 1
1x + 1y = 3
```

The constant vector is:
```
B = [1]
    [3]
```

### What np.linalg.solve Does

The `np.linalg.solve(A, B)` function in NumPy solves a system of linear equations in the form Ax = B, where:
- A is the coefficient matrix
- B is the constant vector
- x is the vector of variables we want to solve for

Specifically, it performs the following operations:

1. **Matrix Decomposition**: It uses a technique called LU decomposition (Lower-Upper) to factorize the coefficient matrix into the product of a lower triangular matrix L and an upper triangular matrix U. This decomposition is efficient for solving linear systems.

2. **Forward and Backward Substitution**: After decomposition, it applies forward and backward substitution algorithms to solve the system. Forward substitution solves Ly = B for y, and backward substitution solves Ux = y for x.

3. **Solution Verification**: It checks if the solution is valid (checks for singular matrices, which would indicate no unique solution exists).

4. **Optimization**: The implementation uses highly optimized LAPACK routines (Linear Algebra PACKage), which are written in Fortran and are extremely efficient for numerical linear algebra operations.

The result of `np.linalg.solve(A, B)` is a NumPy array containing the values of the variables that satisfy the system of equations. In our case, it returns [x, y], the solution to the system.

For the example system:
```
[1 0] [x] = [1]
[1 1] [y]   [3]
```

The solution is x = 1.0, y = 2.0, which you can verify:
1. First equation: 1(1.0) + 0(2.0) = 1 ✓
2. Second equation: 1(1.0) + 1(2.0) = 3 ✓

## Why Use NumPy Instead of Manual Calculation?

For a simple 2×2 system, we could have used Cramer's Rule or direct substitution to solve the system. However, using NumPy offers several advantages:

1. **Scalability**: The same approach works for larger systems with many variables
2. **Numerical Stability**: NumPy uses algorithms that minimize numerical errors
3. **Efficiency**: The underlying LAPACK routines are highly optimized for performance
4. **Simplicity**: The code is cleaner and easier to understand