#You can clear your Variables from Lesson 1 by:
#clicking "eraser" icon at the top of the Variable explorer window or
#clicking "eraser" icon at the top of Consolde window

#%% Section 5 - Dictionaries & Tuples

#%%% Dictionaries
#Slide 33
#Array using your own "names" for the "rows"
#storing information in key:value pairs

stocks = {'AAPL':'Apple Inc.', 
		  'CAT':'Caterpillar', 
		  'MSFT':'Microsoft',
          'NFLX':'Netflix'}

#To extract
stocks['CAT']

#To change values
stocks['AAPL'] = "Apple"

#To create a new entry
stocks['FB'] = 'Facebook'

#list of all row names
stocks.keys()
#list of all the values
stocks.values()

#%%% Tuples
#Slide 34
#Arrays that store constants
#tax rates, fx rates
taxes = (0.25, 0.35, 0.50)

taxes[1] #this pulls out the 2nd item, 35%

#This doesn't work:
#taxes[0] = 0.45

#%% Section 6 - If Statements - Boolean Logic
#Slides 36 - 40

#or |
#AND &
#not equal to: !=
#to compare if two things are equal use == not =
    #one "=" is used to change the value of a variable

x = 5
y = 10

# y = x #this changes b to be equal to x
# y == x #this checks if y and x are the same

#If Example
if x > y:
    print("x is greater than y")
    print("x is ", x)
    if x > 100:
        print("x is greater than 100")
elif y > x:
    print("y is greater than x")
else:
    print("x is equal to y")

print("this is outside the if statement")

#Be careful with "Truthy" statements, anything that is not 0 is True
if 10 - 2:
    print("This IF is True")


#%% Section 7 - Looping
#Two main types of loops: For loop, While loop
#For Loop - you know how many times to loop
#While Loop - you are checking a condition (loop with an IF stmt)
    #loop will run as long as condition is True

#%%% For Loop
#Slide 41    
numbers = [2, 5, 7, 9, 13, 25]

#Looping through a list
#Print the squares and cubes of these numbers really quickly
for num in numbers:
    print("-"*10)
    print(num)
    print("Square:",num ** 2) #square
    print("Cube:",num ** 3) #cube

#More efficient:
output = "X:{} Square:{} Cube:{}"
for num in numbers:
    print("-"*20)
    print(output.format(num, num**2, num**3))


#Looping "X" number of times
for i in range(5): #prints numbers 0, 1, 2, ... 4
    print(i)

for x in range(2,26,2): #range(start, end, skip)
    print(x) #prints 2, 4, 6, etc. stops at 24

#%%% List Comprehension
nums = [5, 7, 9, 12]
numsCube = [x**3 for x in nums]

#Faster than doing:
cubeList = []
for x in nums:
    cubeList.append(x**3)

#Can combine with IF Statements
nums = [3, 50, 29, 12, 100, 62]
squareList = [x**2 for x in nums if x > 50]

#%%% While Loops
#Slide 43
x = 5

#while x > 2:
#    print(x)
    #this is an infinite loop, it never stops
        # you can interrupt by hitting the Stop botton
        #OR hitting CTRL + C inside the console window
        
while x < 1000:
    print(x)        
    x += 1  #x = x + 1

#Careful with using floats in If statements or While loops
print(1.1 + 2.2 == 3.3) #Gives False
        #actually doing 3.30000001 or 3.29999999998...
print("{:.20f}".format(3.3))

round(1.1 + 2.2)  == round(3.3) #Gives True

#%% Exercises
#Try Exercises 3, 4, 5 from Assignment 1