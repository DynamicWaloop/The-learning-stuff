import math

degrees = 45
radians = degrees /18 * math.pi
x = math.sin(degrees / 360.0 * math.pi)

## 3.4 Adding new functions ##

# def to declare a function
# Syntax
def function(num1, num2):
    return num1 + num2

# Defining a function creates a unction object, which has a type of function

# calling a function 
print(function(1,1))
# I'm calling a function inside a function 

## 3.5 Definitions and uses ##
# Function definitions must be created before the function call to avoide errors

## 3.6 Flow of execution ##
# Our code is always executed from top to bot
# Statements are executed one after another

## 3.7 parameters and arguments ##
# Some functions require arguments
# Inside a function, the argumets are assigned to variables called parameters. 

def printTwice(bruce):
    print(bruce)
    print(bruce)

printTwice("bruce")

# We can use any kind of expression as an argument 
# The argument is evaluted before the function is called
# A variable can be used as an argument
printTwice("Hank"*4)

newName = "Name"

printTwice(newName)

## 3.8 Variables and parameters are local ##
# When you create a variable inside a function, it is local, it can't be used out of the function

def catTwice(part1, part2):
    cat = part1 + part2 # cat can only exsit in the local scope of catTwice
    printTwice(cat) 

catTwice("row", "row")

## 3.9 Stack Diagrams ##
# To keep track of which variables can be used where, it is sometimes useful to draw a stack diagram
# Used to show the function each variable belongs to 


#          |------------------|
#          | x -> something   |
#  _main_  | num2 -> 45       |
#          |                  |
#          |__________________|

#          |------------------|
#          | cat -> p1 + p2   |
# catTwice | p1 -> "row"      |
#          | p2 -> "row"      |
#          |__________________|

# Each function is represented by a frame with the parameters and variables of the function inside
# Arranged in a stack that indicates which function caled which 

## 3.10 Fruitful functions and void functions ##
# Some functions return results while others don't return anything

# Take the result and assign it to x

x = math.cos(radians)
golden = (math.sqrt(5) + 1) / 2

# void functions might have some effects but they won't return anything

# Doesn't return anythig but does have an effect 
def returnNothing():
    print(x)

## 3.14 Exercises ##

### Ex 3.1 ###
# Write a function name rightJustify that takes a string named s as a parameter and prints the string 
# with enough leading spaces so that the last letter of the string is in column 70 of the display

def rightJustify(s):
    length = len(s)
    print(" " * (70 - length) + s)

rightJustify("Montey")
rightJustify("Harry")

print(len(range(5)))