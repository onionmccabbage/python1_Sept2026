## Python 1

September 2026 - Toby Dussek

* 9:00 start
* 10:45 morning break (20 mins)
* 12:30 lunch (1 hr)
* 3:15 afternoon break (20 mins)
* 5:00 done

### What we will do today
* Welcome, tech check and where to get help
* Comparing Excel and Python
* Overview: using Jupyter
* Writing Python code
* Data Types
* Data Collections
* Exercises 1 & 2
* Python 'dictionary' data type
* Conditional Logic and Loops
* Using range() and list comprehension
* Exercises 3, 4 & 5 (optionally 6)
    - code snippet: `grades = {'Bob':71, 'Alice':65, 'Jim':70, 'Jen':90, 'Tim':86, 'Trish':85, 'Tony':75}`
* Functions
* Random numbers, Normal Distribution and Standard Deviation
* Using Numpy Arrays
* Exercises 7 & 8 
* Using Pandas
* Importing and cleaning data
* DataFrames for statistical analysis
* Assignment 2 Exercises 1 & 2

#### Optional Content
* Merging and joining data sources
* Assignment 2 Exercises 3 & 4
* Moving Averages
* Data sampling frequency
* Assignment 2 Exercises 5, 6 & 7

### Things to watch for
#### Assignment 1
- When reading in the supplied .csv and .xlsx files you will often need to add `date_format='%m/%d/%y'` 
#### Assignment 2
- Exercise 1: use `format='%m/%d/%y'` (instead of format=r'%Y-%m-%d')
- Exercise 6: find `fundamentals.csv` in `ExData` folder
- Exercise 6 step 6: nay be better off using `ba_fin['ROA'] = ba_fin['ROA'].ffill()`
- Exercise 7: file `ff3.csv` is actually called `ff3_monthly.CSV` (in `ExData` folder)
- General: You may get this problem/solution: `ValueError: Invalid frequency: M. Failed to parse with error message: ValueError("'M' is no longer supported for offsets. Please use 'ME' instead.")`

