# Remeber to always keep one extra line or add extra empty line at the end of your code

print("python journey begins")
# string manupulation
# printng a new line without using print statement
print("my name is paras\nI am programmer just like you")

# combine a string with another string also known as concatination
print("helo" + "friends")

# ways to add spaces while combining two strings
print("helo " + "friends")

print("helo" + " " + "friends")

# taking input from user
input("what is your name?\n")

# taking user input and also print a statement
print("helo " + input("what is your name?\n"))

print("helo " + input("what is your name?\n") + "!")

# variable
name = input("what is your name?\n")
print(name + " is the vlaue stored in the name variable")

# adding new data to same variable
myName = "paras"
myName = "andy"
print(myName + " is the new name stored as a new variable data")

# challange - 01
userName = input("what is your name?\n")
print("user name is : " + userName + " , the length of the user name characters is : " + str(len(userName)))

# challange - 02
name_of_user = input("enter user's name\n")
lenght_of_characters = len(name_of_user)
print(lenght_of_characters)

# challange - 03
glass1 = "milk"
glass2 = "juice"
glass1, glass2 = glass2, glass1
print(glass1)
print(glass2)

# remember to always keep an extra empty line at the end of your code
