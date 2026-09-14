#%% Section 1 - Intro to Spyder
#Creating a new project:
"""
- Projects menu --> New Project --> Existing Directory
- Enter location in the Location section (or select the folder by browsing to it)
- Click Creates
"""

#Useful Shortcuts
"""
- Slide 9 Has useful shortcuts used in Spyder
- Most commons ones we will use today:
    - F9 to run one line at a time (no highlight needed) or multiple lines (highlight them)
    - F5 to run the entire file (normally only use to run the entire Python file)
    - CTRL + Enter to run a section at a time
    - SHIFT + Enter to run a section and also advance forward to next section
    - These shortcuts are also listed on the Run menu
- For a list of all Spyder shortcuts: 
    Tools menu --> Preferences --> Keyboard shortucts
"""

#Other Tips:
"""
Use # to create single line "comments"
Use triple quotations for multi-line comments or notes
Use #%% for sections ("cells")
Use #%%% for a sub section (will still look like a cell)
The titles of these sections can also be see in the Outline window:
    View --> Panes --> Outline to enable
"""
#%% Section 2 - Data Types
#To run this section hit CTRL + Enter

x = 5 #integer
z = 2.5 #float

type(x)#This will work if you run single line with F9
print(type(x)) #if running entire file or section, you need to surround with print

x = "Hi" #string
    #note how variables can be re-assigned to be a different data type

greeting = "Hello World"
name = "Guido van Rossum"

print("Hello " + name)
    #use + to concatenate

#greeting + z 
    #this gives an erorr, cannot concat float to str

print(greeting + str(z))

#%% Section 3 - Strings and String Methods
y = '6' #this is a string
print(y * 100) #will print 6 repeated 100 times
print("-" * 50) #repeats the dash 50 times

#Cleaning up numbers
myNumber = "$123,456,789"
myNumber * 2


myNumber.strip('$') #did not change original
# myNumber = myNumber.strip('$')
# myNumber = myNumber.replace(',', '')
# myNumber = int(myNumber)

#All in one step
myNumber = "$123,456,789"
myNumber = int(myNumber.strip('$').replace(',', ''))

#variableName --> camel case
#variable_name --> snake case

#%%% String Format Method
#Slide 23

output = "Sales: {}, Gross Margin {:.2%}"
print(output.format(2000,0.3))

output2 = "Market Cap: {:>9,}"
mkCap1 = 1234
mkCap2 = 3456700
mkCap3 = 100234
print(output2.format(mkCap1))
print(output2.format(mkCap2))
print(output2.format(mkCap3))

#%% Section 4 - Lists and List Methods
#Arrays in other programming language
#Slides 26-32

ticker1 = 'AAPL'
ticker2 = 'SP500'
ticker3 = 'MSFT'

tickers = ['AAPL', 'SP500', 'MSFT', 'TSLA', 'NFLX']

#extract info from a list
tickers[3]

#change one of the itmes
#NFLX --> AMZN
tickers[4] = 'AMZN' #don't forget counting starts at 0
len(tickers) #size of the array --> 5

tickers[-1] = 'NFLX' #<-- this changes the last item

#pull out the first 3 items
tickers[0:3] #0 <= x < 3, 2nd number is open interval
tickers[4:6] #rows 4 and 5

#%%% List Methods
#Slide 29

listX = [1, 2, 3]
listY = [100, 200, 300]
listZ = ['a', 'b', 'c']

z = 10

listX.insert(1, z) #adds z as the new second item
listX.append(listY) #adds listY as one entry
listX[4][1] #extracts the "200"

listX.extend(listZ) #breaks appart listZ as multiple "rows"

#%%% Copying Lists

list1 = [1,2,3]
list2 = list1 #Creates a link
list2[0] = 100 #this will change first item of both list1 and list2

list3 = list1.copy() #copies the Values
list4 = list1[:] #copies the Values

list4[0] = 5000 #only changes first item in list4


#%% Exercises
#Try Exercises 1, 2 from Assignment 1