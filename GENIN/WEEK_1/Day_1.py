#DAY 1
print("Hello World!")
print("Day 1 - String Manipulation")
print("string concatenation is done with the " '+' " sign")
print('e.g. print("Hello " "+" " World")')
print("New lines can be created with a backslash and n.")


#input() will get user input in console.Then print() will print the word "Hello" and then the user input

print("Hello " + input("what is your name? "))

#getting length ofa string
print(len(input("what is your name? ")))

# python variables
name = "Jack"
print(name)

name = "Angela"
print(name)

name = input("What is your name? ")
length = len(name)
print(length)

#interactive variable

a = input("a: ")
b = input("b: ")
c = a
a = b
b = c
print("a = " +  a)
print("b = " + b)

#band name project generator
print("Welcome to Band Name Generator")
city  = input("where did you grow up in?\n")
pet = input("what is the name of your pet?\n")
print("Your band name cold be " + city + "" + pet)
