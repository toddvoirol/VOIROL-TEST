# Log File Analysis

You have noticed some strange errors in the log files of a website that you are hosting. You want to investigate them more carefully and have to use Pandas to prepare them for further review.

The log files will look like the ones below right after loading them into a data frame. Note that the real data frame will not have the same data, but the same structure!

## Header Row
| Time | Endpoint | HTTPMethod | Login | IPAddr | ResponseMS | ResponseCode |
|------|----------|------------|-------|--------|------------|--------------|

## Sample Data Rows
| 17544 | /login | POST | "" | 115.91.249.13 | 928 | 200 |
| 17591 | /admin | GET | "user123" | 212.91.249.1 | 223 | 403 |

The log files are saved as a CSV file called log.csv. Your task is to:

1. Load the log file into a data frame `log_data`.
2. Remove any rows where Login is empty (""), as those are unlikely to cause the issues.
3. Remove any rows where ResponseCode is not 500, as this is where the issue seems to be happening.
4. Create a new column HTTPCall that contains the HTTPMethod column and the Endpoint column, separated by a single whitespace (" "). For example, if HTTPCall is GET and Endpoint is /login, then HTTPCall should be `GET /login`.
5. Sort the entire data frame by the Time column in descending order. You can add the parameter `ascending=False` when sorting to achieve that.
6. Remove all columns except for Time, Login, ResponseCode, and the new column HTTPCall you created previously. 

**Hint:** Remember that you can always print your data frame to see what your data looks like.

Your code snippet should define the following variables: `log_data` (DataFrame containing cleaned log data)
