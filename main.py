# Initial Print - Tradition

print("Hello, World!")

#Python Indentation

if 5 > 2:
  print("Five is greater than two!")

  """
  This is a comment
  written in
  more than just one line
  """

x = 4       # x is of type int
y = "Sally" # x is now of type str
print(x)
print(y)

# Casting - If you want to specify the data type of a variable, this can be done with casting.

x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0
print(x)
print(y)
print(z)

# You can get the data type of a variable with the type() function.

x = 5
y = "John"
print(type(x))
print(type(y))

"""
Variable Names
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"
"""

# Python allows you to assign values to multiple variables in one line:
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

#One Value to Multiple Variables
x = y = z = "Orange"
print(x)
print(y)
print(z)

#Unpack a Collection
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

#Output Variables
x = "awesome"
print("Python is " + x)

x = "Python is "
y = "awesome"
z =  x + y
print(z)

#Global Variables

#Create a variable outside of a function, and use it inside the function
x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc()

#Create a variable inside a function, with the same name as the global variable
x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)

#If you use the global keyword, the variable belongs to the global scope:
def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)

#To change the value of a global variable inside a function, refer to the variable by using the global keyword:
x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)

#Print the data type of the variable x:
x = 5
print(type(x))

#Convert from one data type to another:
x = 1    # int
y = 2.8  # float
z = 1j   # complex

#convert from int to float:
a = float(x)

#convert from float to int:
b = int(y)

#convert from int to complex:
c = complex(x)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))

#Import the random module, and display a random number between 1 and 9:
import random

print(random.randrange(1, 10))

#Get the character at position 1 (remember that the first character has the position 0):
a = "Hello, World!"
print(a[1])

#Loop through the letters in the word "banana":
for x in "banana":
  print(x)

#The len() function returns the length of a string:
a = "Hello, World!"
print(len(a))

#Check if "free" is present in the following text:
txt = "The best things in life are free!"
print("free" in txt)

#Print only if "free" is present:
txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")

#Check if "expensive" is NOT present in the following text:
txt = "The best things in life are free!"
print("expensive" not in txt)

#print only if "expensive" is NOT present:
txt = "The best things in life are free!"
if "expensive" not in txt:
  print("No, 'expensive' is NOT present.")

#Get the characters from position 2 to position 5 (not included):
b = "Hello, World!"
print(b[2:5])

#Get the characters from position 2, and all the way to the end:
b = "Hello, World!"
print(b[2:])

#Get the characters:
#From: "o" in "World!" (position -5)
#To, but not included: "d" in "World!" (position -2):

b = "Hello, World!"
print(b[-5:-2])

#The upper() method returns the string in upper case:
a = "Hello, World!"
print(a.upper())

#The lower() method returns the string in lower case:
a = "Hello, World!"
print(a.lower())

#The strip() method removes any whitespace from the beginning or the end:
a = " Hello, World! "
print(a.strip())

#The replace() method replaces a string with another string:
a = "Hello, World!"
print(a.replace("H", "J"))

#The split() method splits the string into substrings if it finds instances of the separator:
a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!']

#Python - String Concatenation
#Merge variable a with variable b into variable c:
a = "Hello"
b = "World"
c = a + b
print(c)

#Use the format() method to insert numbers into strings:

age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))

#The format() method takes unlimited number of arguments, and are placed into the respective placeholders:

quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))

#You can use index numbers {0} to be sure the arguments are placed in the correct placeholders:

quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))









