#%% Section 10 - Intro to Pandas

#Slide 61
#Things you can do with pandas package:
"""
Data Manipulation
- Loading and cleaning data
- Filtering, sorting
- Access specific columns or rows
- Rolling metrics - moving average
- Calculate new columns --> formulas to do math
- Pivot table
"""

#%%% Importing pandas
import pandas as pd  
pd.__version__

#pd is the common "alias" used in Python community
#http://pandas.pydata.org/pandas-docs/stable/

#%%% Importing data
#Slide 64
sp500 = pd.read_csv("StockData/sp500.csv") #using relative path of project
dir(sp500) #lists out all properties and methods

#Can also use an absolute path:
# aapl = pd.read_csv(r"C:\Users\guido\Desktop\Python Class\Python 1\StockData\aapl.csv")
# note you have to use r at the beginning of the string if using backslashes (Windows)

#To see a summary of the data use .info
sp500.info() #summary of all columns
summaryStats = sp500.describe()

#To look at the first and last 5 rows:
sp500.head()
sp500.tail()

#Expand all columns in the output
pd.set_option("display.max_columns", 10)

#%%%Setting up the Data
#Change Dates to be numbers not text
sp500['Date'] = pd.to_datetime(sp500['Date'])
sp500.info() #Date column is now datetime not object

#changing the index to Dates column
sp500.set_index(['Date'], drop=True, inplace = True)
    #inplace = True is the same thing as sp500 = sp500.set_index....
    #most pandas functions/methods don't change the original table
    #you need to reassign to change the original DataFrame
    #or use inplace=True

#%% Section 11 - Accessing/Slicing Data
#Slides 72-76

#%%% Accessing rows
#Method 1 - iloc - integer location - index
	#starts with 0; row 1 in Excel = row 0 in Pandas

sp500.iloc[0] #first row
pd.options.display.float_format = '{:.2f}'.format #to change format of floats

sp500.iloc[:2]#start at beg, stop row[1]
	#still does open interval for iloc

#Method 2 - loc - new index, which is now Date
sp500.loc['20130930']
sp500.loc['20130930':'20131010'] #inclusive of the last date
sp500.loc['2013-10'] #prints all October of 2013
sp500.loc['2016'] #all 2016


#%%% Accessing columns
#Method 1 - Using df['name column'], similar to Dictionaries
sp500['Adj Close']

#Method 2 - Using df.colName, does not work for columns with spaces in name
sp500.Close

#%%% Slicing parts of DataFrame
#Method 1 - Using .loc['rowName','colName']
sp500.loc['2014-09', 'Low'] #column name inside []
sp500.loc['2015-09', ['Low','High']] #multiple columns can be given in a list

#Method 2 - Using .loc['rowName']['colName']
sp500.loc['2016-01']['Volume']#column name inside []
    #Careful when using this method to "Copy" data into another DataFrame
    #It could create a "view" instead of a copy, where tables are linked
    #Use df.loc['row']['col].copy() or Method 1
    #See Slide 72 for more details

sp500_OC = sp500[['Open','Close']]
sp500_HL = sp500.loc[:,['High','Low']] #another way of copying just values
        # .loc[:] grabs all rows

#%%% Output to Excel
sp500_OC.to_csv("Output/SP500 Open Close.csv")
sp500_HL.to_excel("Output/SP500 High Low.xlsx")

#%% Section 12 - Manipulating Data
#Sorting
#Filtering
#Creating new columns / calculated fields

#%%% Sorting Data
#Slide 70

#Descending by volume
sp500.sort_values(['Volume'], ascending=False, inplace=True)
#don't forget the inplace=True if you want to change the original
#OR: sp500 = sp500.sort_values....

#Sort multiple cols
sp500.sort_values(['Volume','Close','Open'],
                  ascending=[False,False,True],
                  inplace=True)

#Sort by Index
sp500.sort_index(inplace=True)

#%%% Filtering Data
#Slide 75

# posDays = sp500[ booleanMask  ]
#where a boolean mask is a column of True/False

#Filter the table for positive days
    #Today's close > Today's open
sp500[sp500['Open'] < sp500['Close']] #method 1 - use condition directly
sp500[sp500['isPositive']] #method 2 - give it a column of T/F

#More complex filtering:
    #Volume is bw x and y shares

sp500[ (sp500['Volume'] >= 1.30e+09) & (sp500['Volume'] <= 3.5e+09) ]
                        # 1,300,000,000
filteredTable = sp500[(sp500['Volume'] >= 1.30e+09) & (sp500['Volume'] <= 3.5e+09)]
    #Careful! filteredTable is linked to sp500
    #if you change the value of one of the rows
    #it changes the value in the bigger table

#If you don't want that, use .copy()
filteredDF = sp500[sp500['Close'] < sp500['Open']].copy()
    #See slide 76

sp500['isPositive_v2'] = sp500['Close'].shift(1) < sp500['Close']
            #today's close price is > row above close price (prev day)


sp500['priceScaled'] = sp500['Close'] * 100

#Index Price > 2,100 and <2,200
sp500[(sp500['Close'] > 2100) & (sp500['Close'] < 2200)]

#%%% Calculated Fields
import numpy as np
sp500['logClose'] = np.log(sp500['Close'])
sp500['logReturns'] = sp500['logClose'].diff() #default takes previous row

#Moving Averages
#1-Day moving average --> equal to yesterday
sp500['ma_1'] = sp500['Close'].shift(1)
sp500['ma_5'] = sp500['ma_1'].rolling(window = 5, min_periods = 5).mean()
sp500['ma_20'] = sp500['ma_1'].rolling(window = 20, min_periods = 20).mean()

#for more complex formulas use .apply()
#Slide 80


#%%% Resampling Data --> Daily to Monthly
#Slide 79
#Step 1 - Dictionary w Rules for each Column
rules = {'Open':'first', 'Close':'last','Volume':'sum'}
monthlySP500 = sp500.resample('M').agg(rules)

#%%% Merging Data Sets
#Slides 85 - 95

#Concat --> columns have to match up
aapl = pd.read_csv("StockData/aapl.csv")
sp500 = pd.read_csv("StockData/sp500.csv")

aapl['Ticker'] = "AAPL"
sp500['Ticker'] = 'SP500'

concatData = pd.concat([aapl,sp500])
    #header names were the same
    
#Merge --> you can pick one or more columns to merge on
mergedData = sp500.merge(aapl)
    #merge on all the columns that have the same name
    #getting no results
    
mergedData = sp500.merge(aapl, left_on=['Date'], right_on=['Date'])
                #left table: sp500
                #right table: aapl
                #put _x, _y as suffixed to header names
mergedData = sp500.merge(aapl, left_on=['Date'], right_on=['Date'],
                         suffixes=("_sp500","_aapl"))

        #default how="inner"
mergedData = sp500.merge(aapl, how="left", left_on=['Date'], right_on=['Date'],
                         suffixes=("_sp500","_aapl"))