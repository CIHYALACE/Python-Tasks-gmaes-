# 1. Write a Python program to read a file line by line
# and store it into a list.

# contentLines = []
# def FileReader(contentLines):
#     f1 = open("Test.txt",'r')
#     for line in f1:
#         contentLines.append(line)
#     print(contentLines)

# FileReader(contentLines)

# 2. Create a list of strings , Add to it yourname then
# Write the list to a new File .

# stringsList = ["The ", "Target ", "Name ", "Is: "]
# stringsList.append("Abdo")

# f1 = open("Test.txt",'w')
# for string in stringsList:
#     f1.write(string)

# 3. Create package directory called Calculator and add
# file called my_functions that have the following
# function
# a. Sum Function
# b. Subtract Function
# c. Divide Function
# d. Multiply Function

# from Calculator.my_functions import Sum , Subtract , Divide , Multiply

# num1 = int(input("Enter First Value: "))
# num2 = int(input("Enter Second Value: "))
# userInput = int(input("Coose The Number Of The Operation (1-Sum , 2-Subtract , 3-Divide , 4-Multiply): "))
# if (userInput == 1):
#     operator = Sum
# elif(userInput == 2):
#     operator = Subtract
# elif(userInput == 3):
#     operator = Divide
# elif(userInput == 4):
#     operator = Multiply
# else:
#     print("enter an invalid next time: ")

# result = operator(num1,num2)
# if(num1 == 0 or num2 == 0):
#     if(operator == Subtract):
#         print("subtracting zero from Number")
#     elif(operator == Divide):
#         print("can’t divide with zero")
#     elif(operator == Multiply):
#         print("Multiply with Zero")
# else:
#     print(result)

