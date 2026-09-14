#%% Section 8 - Functions
#Slide 45
#creating your own formulas that don't exist in Python
#also useful for creating "mini programs" that can be reused in your code
    #e.g. function that imports data from files, scrapes websites, etc.

def fnCube(x):
    cube = x ** 3
    return cube #outputting the result

def fnSquare(x):
    return x ** 2

#functions do not always have to return a value
def printGreeting(fName, lName):
    print("Hello " + fName + " " + lName)

#functions can return multiple outputs
def perimAreaRectangle(length, width):
    area = length * width
    perim = 2* (length + width)
    return perim, area 

#functions have to be written and loaded in memory before using them
    #typically declare functions at the top of our codes
x = 5
y = 10
print(fnSquare(x))

fnCube(y)
perim, area = perimAreaRectangle(x, y)

#%%% Lambda Functions
#Slide 47
#Advanced Topic
#Useful for writing simple "one-liner" functions

#lambda input(s): what to do with the input
lambdaSquare = lambda x: x**2

print(lambdaSquare(25))

hypLength = lambda x, y: (x**2 + y**2) ** 0.5 #could also use math.sqrt
print(hypLength(4,3))

#%% Section 9 - NumPy Library
#Slide 49
#Numpy package provides more advanced mathematical and statistical functions
#Also allows for more advanced calculations with arrays and matrices

#We will be primarily using it for random functions
#Slide 50

import numpy as np

#%%% Random Numbers
np.random.seed(42) #sets a seed for the random number generator. Set once per exectuion
print(np.random.rand(10))
print(np.random.rand(10)) #creates another list of 10 random numbers

# Notice setting seed again produces the same sequence as the first time
np.random.seed(42) 
print(np.random.rand(10))

#Random Integers
print(np.random.randint(1,7, size=100)) 
    #generates 100 random integer from 1 to 6 (exclusive of the 7)
    #similar to rolling dice
    #each number has equal chance of getting drawn

#Random Normal Distrubtion
#Now the probability of a number being generated will follow the normal (bell curve) distribution.
print(np.random.normal()) #draws a random number from the normal distribution
print(np.random.normal(5,2)) # can specify mean and standard dev
print(np.random.normal(5,2, 10)) # can specify mean and standard dev and size

#%%% Math and Statistical Functions
results = np.random.normal(5,2, 100)
    #notice how results variable is numpy array (not a list)

#Statistical functions
np.mean(results)
np.std(results)
np.cov(results)
np.sum(results)

#Other math functions
e = np.exp(1)
np.log(e) #natural log
np.sqrt(144)

#%% Exercises
#Try Exercises 6, 7, 8 from Assignment 1