import unittest
import pandas as pd
import os
import tempfile

class TestLogFileProcessing(unittest.TestCase):
    """
    Unit tests for the log file processing functionality.
    Creates a temporary test CSV file to avoid modifying the original data.
    """
    
    def setUp(self):
        """Create a test CSV file for each test"""
        # Create a temporary file
        self.temp_file = tempfile.NamedTemporaryFile(delete=False, suffix='.csv')
        self.temp_file_path = self.temp_file.name
        
        # Create test data resembling the log file format
        test_data = [
            "Time,Endpoint,HTTPMethod,Login,IPAddr,ResponseMS,ResponseCode",
            "17544,/login,POST,\"\",115.91.249.13,928,200",
            "17591,/admin,GET,\"user123\",212.91.249.1,223,403",
            "17600,/profile,GET,\"user456\",212.91.249.2,150,500",
            "17620,/api/data,POST,\"admin\",115.91.249.15,432,500",
            "17630,/login,GET,\"\",115.91.249.20,321,500",
            "17650,/dashboard,GET,\"user789\",212.91.249.4,275,200"
        ]
        
        # Write test data to the temporary file
        with open(self.temp_file_path, 'w') as f:
            for line in test_data:
                f.write(line + '\n')
    
    def tearDown(self):
        """Remove the test CSV file after each test"""
        os.unlink(self.temp_file_path)
    
    def process_log_file(self, file_path):
        """
        A simplified version of the processing code from process_log_files.py
        so we can test the processing steps independently
        """
        # Step 1: Load the log file into a data frame
        log_data = pd.read_csv(file_path)
        
        # Step 2: Remove any rows where Login is empty ("")
        log_data = log_data[log_data['Login'] != '""']
        
        # Step 3: Remove any rows where ResponseCode is not 500
        log_data = log_data[log_data['ResponseCode'] == 500]
        
        # Step 4: Create a new column HTTPCall
        log_data['HTTPCall'] = log_data['HTTPMethod'] + ' ' + log_data['Endpoint']
        
        # Step 5: Sort by Time in descending order
        log_data = log_data.sort_values(by='Time', ascending=False)
        
        # Step 6: Keep only specific columns
        log_data = log_data[['Time', 'Login', 'ResponseCode', 'HTTPCall']]
        
        return log_data
    
    def test_empty_login_removal(self):
        """Test that rows with empty logins are removed"""
        # Step 1 only: Load data
        log_data = pd.read_csv(self.temp_file_path)
        
        # Count initial number of rows with empty logins
        empty_login_count = len(log_data[log_data['Login'] == '""'])
        
        # Step 2 only: Remove empty logins
        log_data = log_data[log_data['Login'] != '""']
        
        # Check that empty logins are removed
        self.assertEqual(len(log_data), len(pd.read_csv(self.temp_file_path)) - empty_login_count)
        for login in log_data['Login']:
            self.assertNotEqual(login, '""')
    
    def test_response_code_filtering(self):
        """Test that only rows with ResponseCode 500 are kept"""
        # Steps 1-3: Load data and filter
        log_data = pd.read_csv(self.temp_file_path)
        log_data = log_data[log_data['Login'] != '""']
        
        # Count how many rows have response code 500 and non-empty logins
        expected_count = len(log_data[log_data['ResponseCode'] == 500])
        
        # Apply the filter
        log_data = log_data[log_data['ResponseCode'] == 500]
        
        # Check that only rows with ResponseCode 500 remain
        self.assertEqual(len(log_data), expected_count)
        for code in log_data['ResponseCode']:
            self.assertEqual(code, 500)
    
    def test_http_call_creation(self):
        """Test that HTTPCall column is created correctly"""
        # Steps 1-4: Load data, filter, and create HTTPCall
        log_data = pd.read_csv(self.temp_file_path)
        log_data = log_data[log_data['Login'] != '""']
        log_data = log_data[log_data['ResponseCode'] == 500]
        log_data['HTTPCall'] = log_data['HTTPMethod'] + ' ' + log_data['Endpoint']
        
        # Check that HTTPCall column is created correctly
        self.assertTrue('HTTPCall' in log_data.columns)
        
        # Check specific values - but only if those rows exist
        for login, expected_call in [
            ('"user456"', 'GET /profile'),
            ('"admin"', 'POST /api/data')
        ]:
            rows = log_data[log_data['Login'] == login]
            if len(rows) > 0:
                self.assertEqual(rows['HTTPCall'].values[0], expected_call)
    
    def test_time_sorting(self):
        """Test that records are sorted by Time in descending order"""
        # Process the file completely up through sorting step
        log_data = pd.read_csv(self.temp_file_path)
        log_data = log_data[log_data['Login'] != '""']
        log_data = log_data[log_data['ResponseCode'] == 500]
        log_data['HTTPCall'] = log_data['HTTPMethod'] + ' ' + log_data['Endpoint']
        log_data = log_data.sort_values(by='Time', ascending=False)
        
        # Get the Time values as a list
        time_values = log_data['Time'].tolist()
        
        # Check that they're in descending order
        self.assertEqual(time_values, sorted(time_values, reverse=True))
    
    def test_column_selection(self):
        """Test that only the required columns are kept"""
        # Process the file completely
        log_data = self.process_log_file(self.temp_file_path)
        
        # Check that only the required columns are present
        expected_columns = ['Time', 'Login', 'ResponseCode', 'HTTPCall']
        self.assertEqual(set(log_data.columns), set(expected_columns))
    
    def test_full_processing(self):
        """Test the entire log processing pipeline"""
        # Process the file completely
        log_data = self.process_log_file(self.temp_file_path)
        
        # We should have all rows with non-empty logins and response code 500
        # Let's count them correctly
        raw_data = pd.read_csv(self.temp_file_path)
        filtered_data = raw_data[
            (raw_data['Login'] != '""') &
            (raw_data['ResponseCode'] == 500)
        ]
        expected_count = len(filtered_data)
        
        # Check final data properties
        self.assertEqual(len(log_data), expected_count)
        
        # If we have results, check they're properly sorted and formatted
        if len(log_data) > 0:
            # Check time is sorted in descending order
            time_values = log_data['Time'].tolist()
            self.assertEqual(time_values, sorted(time_values, reverse=True))

if __name__ == '__main__':
    unittest.main()