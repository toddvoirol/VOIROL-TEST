import pandas as pd

# Step 1: Load the log file into a data frame
log_data = pd.read_csv('log.csv')

# Print original data to see what we're working with
print("Original log data:")
print(log_data.head())
print()

# Step 2: Remove any rows where Login is empty ("")
log_data = log_data[log_data['Login'] != '""']

# Print after removing empty logins
print("After removing empty logins:")
print(log_data.head())
print()

# Step 3: Remove any rows where ResponseCode is not 500
log_data = log_data[log_data['ResponseCode'] == 500]

# Print after filtering for 500 errors
print("After filtering for 500 errors:")
print(log_data.head())
print()

# Step 4: Create a new column HTTPCall that combines HTTPMethod and Endpoint
log_data['HTTPCall'] = log_data['HTTPMethod'] + ' ' + log_data['Endpoint']

# Print after creating HTTPCall column
print("After creating HTTPCall column:")
print(log_data.head())
print()

# Step 5: Sort the entire data frame by the Time column in descending order
log_data = log_data.sort_values(by='Time', ascending=False)

# Print after sorting
print("After sorting by Time in descending order:")
print(log_data.head())
print()

# Step 6: Remove all columns except Time, Login, ResponseCode, and HTTPCall
log_data = log_data[['Time', 'Login', 'ResponseCode', 'HTTPCall']]

# Print final result
print("Final cleaned log data:")
print(log_data.head())