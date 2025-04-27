# Linear Equation Solver - Solution Explanation

This document explains how to solve a system of linear equations using Python and NumPy.

## Understanding the Problem

We need to write a function that:
1. Takes two strings as input, each representing a linear equation like "2x + 3y = 8"
2. Extracts the coefficients of x and y, and the constant from each equation
3. Uses NumPy to solve the system of equations
4. Returns the solution as (x, y) coordinates

## Step-by-Step Solution

### Step 1: Clean Up the Input
For each equation string:
1. Remove any newline characters by replacing them with spaces
2. Remove extra spaces by splitting and rejoining with single spaces
3. Split the equation into left side and right side at the equals sign

Example:
```python
equation = equation.replace('\n', ' ')
equation = ' '.join(equation.split())
left_side, right_side = equation.split('=')
```

### Step 2: Get the Constant (c)
The right side of the equation is our constant. We just need to:
1. Remove any spaces
2. Convert it to an integer

Example:
```python
c = int(right_side.strip())
```

### Step 3: Get Coefficients (a and b)
From the left side of each equation:
1. Split the terms at plus signs to handle each part separately
2. For each part:
   - If it has 'x', get its coefficient (a)
   - If it has 'y', get its coefficient (b)
   - If no number is written before the variable, the coefficient is 1

Example:
```python
parts = left_side.split('+')
for part in parts:
    part = part.strip()
    if 'x' in part:
        # Get coefficient of x
        number = part.replace('x', '').strip()
        if number == '':
            a = 1
        else:
            a = int(number)
```

### Step 4: Solve Using NumPy
Once we have the coefficients, we:
1. Create a 2x2 matrix A with coefficients from both equations
2. Create a vector B with the constants
3. Use NumPy's solve function to find x and y

Example:
```python
A = np.array([[a1, b1], [a2, b2]])
B = np.array([c1, c2])
solution = np.linalg.solve(A, B)
```

## Example

Given the equations:
- "2x + 3y = 8"
- "1x + 1y = 3"

1. After cleaning:
   - Left sides: "2x + 3y" and "1x + 1y"
   - Right sides: "8" and "3"

2. Get constants:
   - c1 = 8
   - c2 = 3

3. Get coefficients:
   - First equation: a1 = 2, b1 = 3
   - Second equation: a2 = 1, b2 = 1

4. Solve system:
```python
A = [[2, 3],
     [1, 1]]
B = [8, 3]
solution = np.linalg.solve(A, B)  # Returns [1.0, 2.0]
```

The solution (1.0, 2.0) means x = 1 and y = 2.

## Testing Your Solution
You can verify your answer by plugging the values back into the original equations:
- 2(1) + 3(2) = 2 + 6 = 8 ✓
- 1(1) + 1(2) = 1 + 2 = 3 ✓