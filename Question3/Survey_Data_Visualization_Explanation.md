# Creating Graphs from Survey Data - How It Works

## What We're Doing
We're taking survey answers from CS101 students about different programming topics and creating four graphs to show the results. This helps us see patterns in what students think about each topic.

## The Survey Data
We have information about different programming topics (like Loops, Logic, etc.):
- How hard students found it (Difficulty: 1-5)
- How useful they think it is (Usefulness: 1-5)
- How much they enjoyed it (Enjoyment: 1-5)
- A number for each topic (Topic Number)

## Making the Graphs - Step by Step

### Step 1: Get Ready
```python
import matplotlib.pyplot as plt
import pandas as pd
```
We need two helper tools:
- matplotlib: Helps us make graphs
- pandas: Helps us work with the survey data

### Step 2: Set Up the Graph Space
```python
fig, axes = plt.subplots(2, 2, figsize=(10, 8))
```
This creates a space for 4 graphs arranged in a 2×2 grid.
Think of it like dividing a piece of paper into four parts.

### Step 3: Make Each Graph

#### Graph 1 (Top Left): Line Plot
```python
axes[0, 0].plot(survey_data['Number'], survey_data['Difficulty'], marker='o')
axes[0, 0].set_xlabel('Number')
axes[0, 0].set_ylabel('Difficulty')
```
Shows how difficult each topic was:
- X-axis: Topic number
- Y-axis: How difficult it was
- The 'o' markers show each data point
- Lines connect the points to show trends

#### Graph 2 (Top Right): Scatter Plot
```python
axes[0, 1].scatter(survey_data['Difficulty'], survey_data['Enjoyment'])
axes[0, 1].set_xlabel('Difficulty')
axes[0, 1].set_ylabel('Enjoyment')
```
Shows if harder topics were less fun:
- X-axis: How difficult it was
- Y-axis: How enjoyable it was
- Each dot represents one topic

#### Graph 3 (Bottom Left): Scatter Plot
```python
axes[1, 0].scatter(survey_data['Difficulty'], survey_data['Usefulness'])
axes[1, 0].set_xlabel('Difficulty')
axes[1, 0].set_ylabel('Usefulness')
```
Shows if harder topics were seen as more useful:
- X-axis: How difficult it was
- Y-axis: How useful it was
- Each dot represents one topic

#### Graph 4 (Bottom Right): Scatter Plot
```python
axes[1, 1].scatter(survey_data['Enjoyment'], survey_data['Usefulness'])
axes[1, 1].set_xlabel('Enjoyment')
axes[1, 1].set_ylabel('Usefulness')
```
Shows if fun topics were also useful:
- X-axis: How enjoyable it was
- Y-axis: How useful it was
- Each dot represents one topic

### Step 4: Show the Graphs
```python
plt.tight_layout()
plt.show()
```
This displays all four graphs with proper spacing between them.

## What to Look For in the Graphs

1. Line Plot (Top Left):
   - Are later topics harder or easier?
   - Are there sudden jumps in difficulty?

2. Difficulty vs. Enjoyment (Top Right):
   - Do students enjoy harder topics less?
   - Are easier topics more fun?

3. Difficulty vs. Usefulness (Bottom Left):
   - Do students find harder topics more useful?
   - Are easier topics seen as less useful?

4. Enjoyment vs. Usefulness (Bottom Right):
   - Do students find fun topics more useful?
   - Are useful topics usually enjoyable?

## Example
If a dot in the top-right graph is at (4, 2), it means:
- That topic had difficulty = 4 (pretty hard)
- And enjoyment = 2 (not very fun)

If you see lots of dots going up and right, it means students enjoyed harder topics more!