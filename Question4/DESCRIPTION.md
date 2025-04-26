
ACME Scientific sent you some data for a 2x2 matrix and a 2xN matrix (with N being unknown), but got them all scrambled up. They sent you the data from both all appended into one long Python list.

You are given a single Python list of integers in a variable raw_data, and your task is to convert it into NumPy matrices a and b.

For example, if raw_data is [1,2,3,4,6,5,4,3,2,1], then:
a = np.array([[1, 2],
		[3, 4]])
and 
b = np.array([[6, 5],
	[4, 3],
	[2, 1]])


The setup code gives the following variables:
raw_data Type list Description List of scrambled matrix data

Your code snippet should define the following variables:
a numpy array Unscrambled matrix a
b numpy array Unscrambled matrix auser_code.py

