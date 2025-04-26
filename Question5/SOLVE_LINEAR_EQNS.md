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
    def extract_coefficients(equation):
        """Extract the coefficients (a, b, c) from an equation string of form 'a x + b y = c'"""
        # Split the equation at the equals sign
        left_side, right_side = equation.split('=')
        
        # Extract constant c from right side
        c = int(right_side.strip())
        
        # Extract coefficients using a simpler approach
        parts = left_side.replace('x', ' x ').replace('y', ' y ').split()
```
- **Coefficient extraction helper function**: 
  - This function uses basic string operations that are easier for beginners to understand
  - It splits the equation into left and right sides at the equals sign
  - The right side is converted to an integer to get the constant term c
  - The left side is preprocessed by adding spaces around 'x' and 'y', then split into words
  - This preprocessing makes it easier to identify the variables and their coefficients

```python
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
```
- **Processing x coefficient**: 
  - We loop through the parts and look for 'x'
  - When we find 'x', we extract its coefficient based on what comes before it:
    - If 'x' is the first part or has a '+' before it, the coefficient is 1
    - If 'x' has a '-' before it, the coefficient is -1
    - Otherwise, the part before 'x' is the coefficient
    - We also check for a minus sign two positions back to handle cases like "- 2 x"

```python
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
```
- **Processing y coefficient**: 
  - Similar to 'x' coefficient extraction, we check for 'y' and extract its coefficient
  - The same rules apply for determining if the coefficient is 1, -1, or an explicit number
  - We also handle the case where there's a minus sign before a number

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

## How the String Parsing Works

Let's walk through an example of how our improved parsing algorithm works:

### Example: "2x + 3y = 8"

1. **Split at equals sign**: 
   - `left_side` = "2x + 3y"
   - `right_side` = "8"
   - `c` = 8 (converting right_side to integer)

2. **Add spaces around variables and split**:
   - `left_side.replace('x', ' x ').replace('y', ' y ')` = "2 x  + 3 y "
   - `parts` = ['2', 'x', '+', '3', 'y']

3. **Process each part**:
   - `i=0, parts[0]='2'` (not 'x' or 'y', so move on)
   - `i=1, parts[1]='x'` (it's 'x', so extract coefficient)
     - The previous part is '2', so `a = 2`
     - No need to check for minus sign since there isn't one
   - `i=2, parts[2]='+'` (not 'x' or 'y', so move on)
   - `i=3, parts[3]='3'` (not 'x' or 'y', so move on)
   - `i=4, parts[4]='y'` (it's 'y', so extract coefficient)
     - The previous part is '3', so `b = 3`
     - No need to check for minus sign since there isn't one

4. **Return coefficients**:
   - `a = 2, b = 3, c = 8`

### Example: "1x - 1y = 1"

1. **Split at equals sign**: 
   - `left_side` = "1x - 1y"
   - `right_side` = "1"
   - `c` = 1

2. **Add spaces around variables and split**:
   - `left_side.replace('x', ' x ').replace('y', ' y ')` = "1 x  - 1 y "
   - `parts` = ['1', 'x', '-', '1', 'y']

3. **Process each part**:
   - `i=0, parts[0]='1'` (not 'x' or 'y', so move on)
   - `i=1, parts[1]='x'` (it's 'x', so extract coefficient)
     - The previous part is '1', so `a = 1`
   - `i=2, parts[2]='-'` (not 'x' or 'y', so move on)
   - `i=3, parts[3]='1'` (not 'x' or 'y', so move on)
   - `i=4, parts[4]='y'` (it's 'y', so extract coefficient)
     - The previous part is '1', so `b = 1`
     - The part before that is '-', so we need to negate: `b = -1`

4. **Return coefficients**:
   - `a = 1, b = -1, c = 1`

This approach handles a variety of formats, including:
- Cases with no spaces: "2x+3y=8"
- Cases with many spaces: "2  x  +  3  y  =  8"
- Cases with implicit coefficients: "x+y=2" (treated as 1x+1y=2)
- Cases with negative coefficients: "-x-y=3" or "- 2 x - 3 y = 4"

## Mathematical Explanation

### System of Linear Equations

A system of linear equations with two variables x and y can be written as:
```
a₁x + b₁y = c₁
a₂x + b₂y = c₂
```

Where:
- a₁, b₁, c₁ are the coefficients and constant of the first equation
- a₂, b₂, c₂ are the coefficients and constant of the second equation

### Matrix Representation

This system can be represented in matrix form as Ax = B, where:

```
A = [a₁ b₁]    x = [x]    B = [c₁]
    [a₂ b₂]        [y]        [c₂]
```

### Why Use NumPy's Linear Algebra Functions?

NumPy's linear algebra module (`numpy.linalg`) provides efficient and numerically stable solutions for linear systems:

1. **Efficiency**: The algorithms are implemented in optimized C and Fortran code
2. **Numerical Stability**: They use techniques like pivoting to minimize rounding errors
3. **Handling Special Cases**: They can detect and handle cases where the system has no solution or infinitely many solutions

### How np.linalg.solve Works

The `np.linalg.solve` function uses LU decomposition, which:

1. Decomposes matrix A into a lower triangular matrix L and an upper triangular matrix U
2. Solves Ly = B for y using forward substitution
3. Solves Ux = y for x using backward substitution

This is much more efficient than manually solving the system using algebra, especially for larger systems.

## Why This Approach Is Good for First Semester CS Students

This solution is suitable for first-semester computer science students because:

1. **Simple String Operations**: Uses basic string methods like `split()`, `replace()`, and `strip()`
2. **Basic Control Flow**: Uses simple loops and conditionals
3. **Step-by-Step Processing**: Processes the equation piece by piece in a logical sequence
4. **Clear Variable Names**: Uses descriptive variable names that make the code's purpose clear
5. **NumPy Abstraction**: Uses NumPy to handle the complex linear algebra, letting students focus on the problem-solving aspects

## Testing the Solution

The code includes several test cases to verify that it works correctly:

```python
# Test with the example from the problem statement
eqn1 = "1 x + 0 y = 1"
eqn2 = "1 x + 1 y = 3"
result = solveEqns(eqn1, eqn2)
print(f"Solution: x = {result[0]}, y = {result[1]}")
# Expected output: x = 1.0, y = 2.0
```

This example from the problem statement should yield x = 1.0, y = 2.0.

Additional test cases check different equation formats:
- `("2x + 3y = 8", "1x - 1y = 1")` - Testing compact notation and negative coefficients
- `("3 x + 2 y = 14", "5 x - 1 y = 17")` - Testing spaced notation
- `("1x + 0y = 5", "0x + 1y = 3")` - Testing zero coefficients

These cases help verify the robustness of the solution against different input formats and equation types.