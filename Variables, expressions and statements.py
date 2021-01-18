print("Hello World!")

# One of the mos powerful features of a programming language is the ability to manipulate variables.
# We can assign a value of a specific type i.e. strings, int, floats... to a variable for later use

## 2.1 Assignment statements ##
# Create a variable and assign it

x = 34
y = "string"
z = True

# The name of the variables can be names *almost* anything
# A common way to represent variables on paper is to write the name with an arrow pointing to its value, this is called a state diagram

## 2.2 variable names ##
# Choose meaningful variable names to keep the code clear

string = "String"
int = 34
decimal = 2.4
boolean = False

# *Variables names can't be the same as pythons built in key words 
# Python 3's key words
# False     class       finally     is          return
# None      continue    for         lambda      try
# True      def         from        nonlocal    while
# and       del         global      not         with
# as        elif        if          or          yield
# assert    else        import      pass
# break     except      in          raise

## 2.3 Expressions and statements ##
# an expression is a combination of value, variablesm and operators.
# A value all by its self is considere an exppression, and so is a variable

# When you type an expression at the prompt, the interpreter evaluates it, which means that it finds the value of the expression
# In this example, n has the value 15 and n + 25 has the value 42

# A unit of code that has an effect, like creating a variable or displaying a value is called a statement

n = 17 # A statement creating a variable called in assigning it 17
# n = n + 17
n += 17
print(n) # print out the the value stored in n 

## 2.4 Script mode ##
# Already scripting (this file is a script)
## 2.5 Order of operations ##
# Well aware of this

## 2.6 String operations ##
# Matheatical operations on strings can't be done, "2"+"2" would print out 22 instead
# The + operator would append two string together
# The * operator would repeat a string a certain amount

## 2.7 Comments ##
# The thing I've been doing with #

## 2.8 Debugging ##
# Three kinds of errors, Syntax, Runtime, Semantic error
# Syntax error: Errors in how the code was typed example: print("2)
# Runtime error: Errors that happend after the execution of the program
# Semantic error: An error that is hard to detect due to it not actcually cuase an error to crash the system

### Excercise 2.2 ###

r = 5
volumeSphere = (3/4) * 3.14 * (r**3)

print(volumeSphere)
#####################
price = 24.95
discount = .4
firstShipping = 3
restShipping = .75
totalCopies = 60

totalPrice = totalCopies * (((price * discount)+firstShipping)+restShipping*(totalCopies-1))
print(totalPrice)