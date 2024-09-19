# Data types

# String data type
brand = "yamaha"
print(brand)

# Subscripting
print(brand[0])

print("paras"[0])

print(brand[-1])

# concatinating
print("12342" + "655") 

# Intiger data type
num1 = 1234
num2 = 9324
print(num1 + num2)

# How to write large number values or large numbers :
sixty_thousand = 60_000
four_lakh = 4_00_000
print(sixty_thousand + four_lakh)

# Float Data type
print(12.45)

# Boolean Data type
print(True)

print(False)

# Excersise 01 
print("hello raghunath"[6] + "shivani"[2])

# How to check the data type
someNum = 12
someStr = "soiauhfvi"
someBool = False
someFloat = 12.56
print("Data type held by someNum variable is : " , type(someNum))

print("Data type held by someStr variable is : ", type(someStr))

print("Data type held by someBool variable is : ", type(someBool))

print("Data type held by someFloat variable is : ", type(someFloat))

# Typecasting
myStr = "1234"
convert_to_intiger = int(myStr)
print(convert_to_intiger)

convert_to_float = float(myStr)
print(convert_to_float)

convert_to_bool = bool(myStr)
print(convert_to_bool)
print(bool(convert_to_intiger))

myBool = False
print(type(str(myBool)))

# Print the lenght number of letters of your string entered by user
user_input_string = input("enter a string of your own like\n")
print(len(user_input_string))

# correct the code excersie
print("number of letters in your string : " + str(len(input("enter your desierd string\n"))))

# Methametical operations 

# Addition
print(12 + 12)

print(12 -10)

print(10*10)

print(12/ 3)

print(12 // 3)

print(10**5)

# Assignment operator
score = 0

score += 12
print(score)

score *= 4
print(score)

score /= 2
print(score)

score **= 3
print(score)

score %= 2 
print(score)

# f-string

burger = 1
price = 12.45
has_eaten = False

print(f"you have {burger} burger, your amount to be paid is {price} and have you eaten your burger {has_eaten}")

print(6 + 4 / 2 - (1 * 2))

a = int("5") / int(2.7)
print(type(a))
