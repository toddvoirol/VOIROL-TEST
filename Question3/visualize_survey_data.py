#!/usr/bin/env python3
# Visualization of CS101 Survey Data
# This script creates a figure with 4 subplots to visualize different aspects of
# a survey about CS101 topics.

# Import necessary libraries
import matplotlib.pyplot as plt
import pandas as pd

# Sample data - in a real scenario, this would be loaded from a file or database
# You can replace this with the actual survey_data if it's provided elsewhere
survey_data = pd.DataFrame({
    'Topic': ['Logic', 'Loops', 'Memory', 'Matplotlib', 'NumPy'],
    'Number': [2, 3, 13, 14, 17],
    'Difficulty': [4.1, 3.2, 3.6, 3.2, 3.8],
    'Usefulness': [4.5, 4.6, 3.3, 4.1, 4.2],
    'Enjoyment': [3.1, 3.6, 3.4, 3.9, 2.2]
})

# Create a figure with 2x2 subplots
fig, axes = plt.subplots(2, 2, figsize=(10, 8))

# Top Left: Line plot of Number vs. Difficulty
axes[0, 0].plot(survey_data['Number'], survey_data['Difficulty'], marker='o')
axes[0, 0].set_xlabel('Number')
axes[0, 0].set_ylabel('Difficulty')
axes[0, 0].set_title('Topic Number vs. Difficulty')

# Top Right: Scatter plot of Difficulty vs. Enjoyment
axes[0, 1].scatter(survey_data['Difficulty'], survey_data['Enjoyment'])
axes[0, 1].set_xlabel('Difficulty')
axes[0, 1].set_ylabel('Enjoyment')
axes[0, 1].set_title('Topic Difficulty vs. Enjoyment')

# Bottom Left: Scatter plot of Difficulty vs. Usefulness
axes[1, 0].scatter(survey_data['Difficulty'], survey_data['Usefulness'])
axes[1, 0].set_xlabel('Difficulty')
axes[1, 0].set_ylabel('Usefulness')
axes[1, 0].set_title('Topic Difficulty vs. Usefulness')

# Bottom Right: Scatter plot of Enjoyment vs. Usefulness
axes[1, 1].scatter(survey_data['Enjoyment'], survey_data['Usefulness'])
axes[1, 1].set_xlabel('Enjoyment')
axes[1, 1].set_ylabel('Usefulness')
axes[1, 1].set_title('Topic Enjoyment vs. Usefulness')

# Adjust layout so plots don't overlap
plt.tight_layout()

# Show the plot
plt.show()