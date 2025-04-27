# Matrix Unscrambling - How It Works

## The Problem

We get a list of numbers and need to split it into two matrices:
1. Matrix A: Always a 2×2 matrix (4 numbers arranged in 2 rows and 2 columns)
2. Matrix B: A 2×N matrix (2 rows, but the number of columns depends on how many numbers are left)

For example, if we get this list: `[1, 2, 3, 4, 6, 5, 4, 3, 2, 1]`

We need to create:
```python
Matrix A:
[[1, 2],
 [3, 4]]

Matrix B:
[[6, 4, 2],
 [5, 3, 1]]
```

## How to Solve It

### Step 1: Get Matrix A
- Take the first 4 numbers from the list
- Arrange them into 2 rows and 2 columns
```python
first_four = [1, 2, 3, 4]
matrix_a = [[1, 2],
            [3, 4]]
```

### Step 2: Get Numbers for Matrix B
- Take all the remaining numbers
```python
remaining = [6, 5, 4, 3, 2, 1]
```

### Step 3: Calculate Matrix B Size
- We know Matrix B has 2 rows
- Count remaining numbers and divide by 2 to get number of columns
```python
number_of_columns = len(remaining) ÷ 2  # In this case: 6 ÷ 2 = 3 columns
```

### Step 4: Create Matrix B
- Take pairs of numbers to form each column
- First number in pair goes in first row
- Second number in pair goes in second row
```python
From [6, 5, 4, 3, 2, 1]:
Column 1: 6 on top, 5 on bottom
Column 2: 4 on top, 3 on bottom
Column 3: 2 on top, 1 on bottom

Result:
[[6, 4, 2],
 [5, 3, 1]]
```

## Important Things to Check

1. Make sure you have at least 4 numbers (needed for Matrix A)
2. Make sure the remaining numbers can be split evenly into pairs (for Matrix B)

## Using NumPy

We use NumPy to help us work with matrices. Here's what the main NumPy functions do:

### np.array()
Turns a Python list into a NumPy array that we can reshape:
```python
nums = [1, 2, 3, 4]
arr = np.array(nums)  # Now we can reshape it
```

### reshape()
Changes how numbers are arranged in rows and columns:
```python
arr = np.array([1, 2, 3, 4])
matrix = arr.reshape(2, 2)  # Makes a 2×2 matrix: [[1, 2], [3, 4]]
```

## Example with Code
```python
raw_data = [1, 2, 3, 4, 6, 5, 4, 3, 2, 1]

# Get Matrix A (first 4 numbers)
matrix_a = np.array(raw_data[:4]).reshape(2, 2)
print("Matrix A:")
print(matrix_a)
# Shows:
# [[1, 2],
#  [3, 4]]

# Get Matrix B (remaining numbers)
remaining = raw_data[4:]
matrix_b = np.array([
    remaining[::2],    # Take every other number starting at 0 (6,4,2)
    remaining[1::2]    # Take every other number starting at 1 (5,3,1)
])
print("Matrix B:")
print(matrix_b)
# Shows:
# [[6, 4, 2],
#  [5, 3, 1]]
```

## In Simple Terms

Think of it like dealing cards:
1. First deal out 4 cards to make Matrix A (2 rows × 2 columns)
2. Then deal out the rest of the cards in pairs to make Matrix B
3. Each pair forms one column in Matrix B