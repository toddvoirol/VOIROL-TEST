# Python Computer Science Test Preparation

This repository contains solutions for sample problems for an upcoming Computer Science test that uses Python. Each solution is organized in its own directory and includes both Python code files (`.py`) and corresponding explanation documents (`.md`) with the same base name as the solution's main function.

## Repository Structure

The repository is organized as follows:

- **Question1/**: First sample problem and solution
- **Question2/**: Log file processing solution with `process_log_files.py` and `PROCESS_LOG_FILES.md`
- **Question3/**: Survey data visualization solution with `visualize_survey_data.py` and `Survey_Data_Visualization_Explanation.md`
- **Question4/**: Matrix unscrambling solution with `matrix_unscramble.py` and `Matrix_Unscrambling_Explanation.md`
- **Question5/**: Linear equations solver with `solve_linear_eqns.py` and `SOLVE_LINEAR_EQNS.md`

## Running Unit Tests

Each problem folder contains unit tests to verify the correctness of the Python solutions. These tests are designed to be understandable for first-semester Python students.

### Prerequisites

- Python 3.x installed on your system
- Required packages: numpy, pandas, matplotlib (depending on the specific problem)

### Running Tests for Individual Problems

#### Question2: Log File Analysis
```bash
cd Question2
python -m unittest test_process_log_files.py
```
Tests verify log filtering, transformation, sorting, and column selection.

#### Question3: Survey Data Visualization
```bash
cd Question3
python -m unittest test_visualize_survey_data.py
```
Tests verify figure layout, plot types, axis labels, and data mapping.

#### Question4: Matrix Unscrambling
```bash
cd Question4
python -m unittest test_matrix_unscramble.py
```
Tests verify matrix extraction, handling different sizes, and error handling.

#### Question5: Linear Equation Solver
```bash
cd Question5
python -m unittest test_solve_linear_eqns.py
```
Tests verify equation solving with different formats, coefficients, and spacing patterns.

### Running All Tests at Once

To run all tests across all problem folders from the project root:

```bash
python -m unittest discover -p "test_*.py"
```

### Understanding Test Results

Successful tests show:
```
........
----------------------------------------------------------------------
Ran 8 tests in 0.123s

OK
```

Failed tests provide details to help identify issues:
```
F....
======================================================================
FAIL: test_example_from_description (test_module.TestClass)
----------------------------------------------------------------------
Traceback (most recent call last):
  ...
  AssertionError: ...
```

### Extending the Tests

To add a new test:
1. Create a new test method in the appropriate test class
2. Name it starting with `test_` followed by a descriptive name
3. Use assertions to verify expected behavior

Example:
```python
def test_new_feature(self):
    """Description of what this test verifies"""
    # Test code here
    self.assertEqual(actual_result, expected_result)
```

## Key Concepts Overview

### DataFrame
- A table-like structure in Python (from the pandas library) that stores data
- Think of it as an Excel spreadsheet in Python with rows and columns
- Can hold different types of data in each column (numbers, text, dates, etc.)
- Makes it easy to select, filter, and organize your data
- Great for working with structured data like survey results or experiment data

### pandas
- A Python library that makes working with data easier
- Gives us useful tools like DataFrames to organize and analyze data
- Helps with reading data from files (like CSV or Excel) into Python
- Lets us clean, transform, and summarize our data
- Named after "panel data" - a term for structured datasets

### matplotlib
- A Python library for making graphs and charts
- Creates visual representations of your data
- Can make many types of plots like line graphs, bar charts, and scatter plots
- Helps us see patterns in data that might be hard to spot in tables of numbers
- Customizable so you can adjust colors, labels, and styles

### Matrices
- Rectangular arrangements of numbers in rows and columns
- Used to organize data or represent mathematical relationships
- In Python, we often create matrices using lists of lists or NumPy arrays
- Allow us to solve multiple equations at once
- Used in many applications like graphics, games, and data analysis

### Pandas Data Filtering
- A way to select only the data you want from a larger dataset
- Like using a sieve to separate what you need from what you don't
- Uses simple conditions like "greater than," "equal to," or "contains"
- Example: `data[data['score'] > 70]` gets only rows where the score is above 70
- Helps focus your analysis on the most relevant information

### NumPy Array
- A special list-like object in Python designed for number crunching
- Much faster than regular Python lists for math operations
- Can hold lots of numbers and perform calculations on all of them at once
- Great for storing and working with rows and columns of numbers
- The building block for most data science and scientific computing in Python

### NumPy
- A Python library that adds support for working with large sets of numbers
- Makes mathematical operations on groups of numbers much faster
- Provides functions for common math operations without writing loops
- Handles arrays and matrices far more efficiently than standard Python
- Essential for any Python program that needs to do lots of calculations

Each problem in this repository demonstrates the application of one or more of these concepts to solve specific computational tasks.