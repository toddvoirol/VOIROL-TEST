# Processing Log Files - How It Works

## What We're Doing
We're looking at website logs (records of who visited the website) to find errors. Think of it like looking through a big list of visitor information to find what went wrong.

## Understanding the Log Data
Each line in our log file has this information:
- Time: When someone visited the website
- Endpoint: Which page they tried to visit (like /login or /home)
- HTTPMethod: How they tried to access it (GET = view page, POST = submit form)
- Login: Username (empty if not logged in)
- IPAddr: Computer address of the visitor
- ResponseMS: How long the website took to respond
- ResponseCode: Whether it worked (200 = good, 500 = error)

## How We Fix It - Step by Step

### Step 1: Load the Data
```python
import pandas as pd
log_data = pd.read_csv('log.csv')
```
This is like opening a spreadsheet file in Python. Pandas helps us work with data easily.

### Step 2: Remove Empty Logins
```python
log_data = log_data[log_data['Login'] != '""']
```
We only want to look at visits from logged-in users, so we remove rows where Login is empty.

### Step 3: Find Error Pages
```python
log_data = log_data[log_data['ResponseCode'] == 500]
```
Keep only the rows where something went wrong (ResponseCode = 500).

### Step 4: Combine Method and Page
```python
log_data['HTTPCall'] = log_data['HTTPMethod'] + ' ' + log_data['Endpoint']
```
Make a new column that shows both how they tried to access (GET/POST) and what page they wanted.
Example: "GET /login" means someone tried to view the login page.

### Step 5: Sort by Time
```python
log_data = log_data.sort_values(by='Time', ascending=False)
```
Put the newest errors first, so we can see what's happening now.

### Step 6: Keep Important Information
```python
log_data = log_data[['Time', 'Login', 'ResponseCode', 'HTTPCall']]
```
Only keep the columns we need:
- When it happened (Time)
- Who it happened to (Login)
- What went wrong (ResponseCode)
- What they were trying to do (HTTPCall)

## Example
If our log file looked like this:
```
Time,Endpoint,HTTPMethod,Login,ResponseCode
1000,/login,GET,"",200
1001,/home,GET,"alice",500
1002,/profile,POST,"bob",500
```

After our code runs, we'd get:
```
Time,Login,ResponseCode,HTTPCall
1002,"bob",500,"POST /profile"
1001,"alice",500,"GET /home"
```

Notice:
- Empty login row is gone
- Only error (500) rows remain
- Newest time is first
- HTTPMethod and Endpoint are combined
- We only kept the columns we need

## What to Do Next
Look at the results to see:
1. Which pages have the most errors
2. Whether certain users see more errors
3. If errors happen more at certain times
4. If recent changes might have caused problems