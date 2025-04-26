# Survey Data Visualization

Solve the following example problem using Python code that a first semester computer science student could understand. It should consist of a single .py file and a .md document that explains the logic behind the solution and explains what each step is doing in detail.

## Problem Description

You have conducted a survey among other CS101 students which course topics they found the hardest, most useful, and most enjoyable to learn. You asked them to rate each of these categories on a scale from 1 to 5 and would now like to visualize your results.

The survey results are already cleaned and prepared, and look like the ones below. Note that the real data frame will not have the same data, but the same structure!

### Header Row
| Topic | Number | Difficulty | Usefulness | Enjoyment |
|-------|--------|------------|------------|-----------|

### Sample Data Rows
| Logic | 2 | 4.1 | 4.5 | 3.1 |
| Loops | 3 | 3.2 | 4.6 | 3.6 |
| Memory | 13 | 3.6 | 3.3 | 3.4 |
| Matplotlib | 14 | 3.2 | 4.1 | 3.9 |
| NumPy | 17 | 3.8 | 4.2 | 2.2 |

*5 rows x 5 columns*

## Task

To visualize the survey data, your task is to plot the data in a single figure with 4 sub-plots in a 2x2 grid:

* The top left sub-plot should be a line plot that plots the number vs. difficulty of each topic.
* The top right sub-plot should be a scatter plot that plots the difficulty vs. enjoyment of each topic.
* The bottom left sub-plot should be a scatter plot that plots the difficulty vs. usefulness of each topic.
* The bottom right sub-plot should be a scatter plot that plots the enjoyment vs. usefulness of each topic.

In all cases, the first column listed should always go on the x-axis and the second one on the y-axis. Both axes should be labeled exactly as the column they represent (e.g., "Difficulty").

You do not need to make any customizations to the plots other than the ones mentioned above.

## Available Variables
The setup code gives the following variables:
- `survey_data`: DataFrame containing survey data
