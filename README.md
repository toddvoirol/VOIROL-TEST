# Python Computer Science Test Preparation

This repository contains solutions for sample problems for an upcoming Computer Science test that uses Python. Each solution is organized in its own directory and includes both Python code files (`.py`) and corresponding explanation documents (`.md`) with the same base name as the solution's main function.

## Repository Structure

The repository is organized as follows:

- **Question1/**: First sample problem and solution
- **Question2/**: Log file processing solution with `process_log_files.py` and `PROCESS_LOG_FILES.md`
- **Question3/**: Survey data visualization solution with `visualize_survey_data.py` and `Survey_Data_Visualization_Explanation.md`
- **Question4/**: Matrix unscrambling solution with `matrix_unscramble.py` and `Matrix_Unscrambling_Explanation.md`
- **Question5/**: Linear equations solver with `solve_linear_eqns.py` and `SOLVE_LINEAR_EQNS.md`

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