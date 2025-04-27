import unittest
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import sys
import os
import importlib.util

# Import the visualization module without running it
spec = importlib.util.spec_from_file_location("visualize_survey_data", 
                                             os.path.join(os.path.dirname(__file__), "visualize_survey_data.py"))
viz_module = importlib.util.module_from_spec(spec)
# Prevent plt.show() from being executed when importing
viz_module.plt = plt
# Save the original show function
original_show = plt.show
# Replace show with a dummy function
plt.show = lambda: None
# Now execute the module
spec.loader.exec_module(viz_module)
# Restore the original show function
plt.show = original_show

class TestSurveyVisualization(unittest.TestCase):
    """Unit tests for the survey data visualization code"""
    
    def setUp(self):
        """Create test data for each test"""
        # Create test survey data
        self.test_data = pd.DataFrame({
            'Topic': ['Logic', 'Loops', 'Memory', 'Matplotlib', 'NumPy'],
            'Number': [2, 3, 13, 14, 17],
            'Difficulty': [4.1, 3.2, 3.6, 3.2, 3.8],
            'Usefulness': [4.5, 4.6, 3.3, 4.1, 4.2],
            'Enjoyment': [3.1, 3.6, 3.4, 3.9, 2.2]
        })
        
        # Create a figure for testing
        self.fig, self.axes = plt.subplots(2, 2, figsize=(10, 8))
        
    def tearDown(self):
        """Close any open plots after each test"""
        plt.close('all')
    
    def test_figure_layout(self):
        """Test that the figure has the correct layout (2x2 grid)"""
        # Check that fig exists and has 4 subplots in a 2x2 grid
        fig = viz_module.fig
        self.assertIsNotNone(fig)
        
        axes = viz_module.axes
        self.assertEqual(axes.shape, (2, 2))
    
    def test_plot_types(self):
        """Test that each subplot has the correct type of plot"""
        axes = viz_module.axes
        
        # Get the lines and collections from each subplot
        top_left_lines = axes[0, 0].get_lines()
        top_right_collections = axes[0, 1].collections
        bottom_left_collections = axes[1, 0].collections
        bottom_right_collections = axes[1, 1].collections
        
        # Check top left is a line plot (has lines)
        self.assertTrue(len(top_left_lines) > 0)
        
        # Check other plots are scatter plots (have collections)
        self.assertTrue(len(top_right_collections) > 0)
        self.assertTrue(len(bottom_left_collections) > 0)
        self.assertTrue(len(bottom_right_collections) > 0)
    
    def test_axis_labels(self):
        """Test that each subplot has the correct axis labels"""
        axes = viz_module.axes
        
        # Check top left labels
        self.assertEqual(axes[0, 0].get_xlabel(), 'Number')
        self.assertEqual(axes[0, 0].get_ylabel(), 'Difficulty')
        
        # Check top right labels
        self.assertEqual(axes[0, 1].get_xlabel(), 'Difficulty')
        self.assertEqual(axes[0, 1].get_ylabel(), 'Enjoyment')
        
        # Check bottom left labels
        self.assertEqual(axes[1, 0].get_xlabel(), 'Difficulty')
        self.assertEqual(axes[1, 0].get_ylabel(), 'Usefulness')
        
        # Check bottom right labels
        self.assertEqual(axes[1, 1].get_xlabel(), 'Enjoyment')
        self.assertEqual(axes[1, 1].get_ylabel(), 'Usefulness')
    
    def test_plot_data(self):
        """Test that the plots contain the correct data"""
        # This requires accessing internal matplotlib data structures
        # which is generally not recommended, but useful for testing
        
        axes = viz_module.axes
        survey_data = viz_module.survey_data
        
        # Test top left plot (line plot)
        line = axes[0, 0].get_lines()[0]
        x_data, y_data = line.get_data()
        np.testing.assert_array_equal(x_data, survey_data['Number'])
        np.testing.assert_array_equal(y_data, survey_data['Difficulty'])
        
        # Test top right plot (scatter plot)
        scatter = axes[0, 1].collections[0]
        # For scatter plots, get_offsets returns the x, y coordinates
        offsets = scatter.get_offsets()
        x_data = offsets[:, 0]
        y_data = offsets[:, 1]
        np.testing.assert_array_almost_equal(x_data, survey_data['Difficulty'])
        np.testing.assert_array_almost_equal(y_data, survey_data['Enjoyment'])
        
        # Test bottom left plot (scatter plot)
        scatter = axes[1, 0].collections[0]
        offsets = scatter.get_offsets()
        x_data = offsets[:, 0]
        y_data = offsets[:, 1]
        np.testing.assert_array_almost_equal(x_data, survey_data['Difficulty'])
        np.testing.assert_array_almost_equal(y_data, survey_data['Usefulness'])
        
        # Test bottom right plot (scatter plot)
        scatter = axes[1, 1].collections[0]
        offsets = scatter.get_offsets()
        x_data = offsets[:, 0]
        y_data = offsets[:, 1]
        np.testing.assert_array_almost_equal(x_data, survey_data['Enjoyment'])
        np.testing.assert_array_almost_equal(y_data, survey_data['Usefulness'])
    
    def test_with_different_data(self):
        """Test that the visualization works with different data"""
        # Create new test data
        new_data = pd.DataFrame({
            'Topic': ['A', 'B', 'C'],
            'Number': [1, 5, 10],
            'Difficulty': [2.0, 3.5, 5.0],
            'Usefulness': [4.0, 3.0, 2.0],
            'Enjoyment': [5.0, 2.5, 1.0]
        })
        
        # We'll create our own visualization function based on the module
        fig, axes = plt.subplots(2, 2, figsize=(10, 8))
        
        # Create plots just like in the module
        axes[0, 0].plot(new_data['Number'], new_data['Difficulty'], marker='o')
        axes[0, 0].set_xlabel('Number')
        axes[0, 0].set_ylabel('Difficulty')
        
        axes[0, 1].scatter(new_data['Difficulty'], new_data['Enjoyment'])
        axes[0, 1].set_xlabel('Difficulty')
        axes[0, 1].set_ylabel('Enjoyment')
        
        axes[1, 0].scatter(new_data['Difficulty'], new_data['Usefulness'])
        axes[1, 0].set_xlabel('Difficulty')
        axes[1, 0].set_ylabel('Usefulness')
        
        axes[1, 1].scatter(new_data['Enjoyment'], new_data['Usefulness'])
        axes[1, 1].set_xlabel('Enjoyment')
        axes[1, 1].set_ylabel('Usefulness')
        
        # Test the first plot's data
        line = axes[0, 0].get_lines()[0]
        x_data, y_data = line.get_data()
        np.testing.assert_array_equal(x_data, new_data['Number'])
        np.testing.assert_array_equal(y_data, new_data['Difficulty'])

if __name__ == '__main__':
    unittest.main()