# Write a Python function to check whether a number falls in a given range. Range (-5, 5) -> return TRUE

# num = int(input ("inter a number to check if it between -5 and 5: "))
# def rangeChecker(num):
#     if(num >= -5 and num <= 5):
#         print("True")
#     else:
#         print("False")
# rangeChecker(num)

#_________________________________________________________________________________________________________

#  Write a Python program to convert two lists into a dictionary in a way that item from list1 is the key and item from list2 is the value.

# firstList = ["name", "age", "grade"]
# secondList = ["Abdo", 24, "B*"]

# def listsMerg(firstList, secondList):
#     dic = dict (zip(firstList, secondList))
#     print(dic)

# listsMerg(firstList, secondList)

#_________________________________________________________________________________________________________

# Write a Python function to create and print a list where the values are square of numbers between 1 and 30 (both included).

# def squareNum():
#     square = []
#     i = 1
#     while i < 31:
#         square.append({ i : i ** 2})
#         i +=1
#     print(square)
# squareNum()

#_________________________________________________________________________________________________________
#Write a Program that takes a list of 5 numbers [3,6,4,0,8] then
#a. Remove the last element in list .
#b. Add in the second place ‘R’.
#c. Ask the user to input specific number in list then delete it { by taking the list element not index}.

# def playInList():
#     num = [3, 6, 0, 4, 8]
#     num.pop()
#     num.insert(1,"R")
#     num.insert(-1,int(input("inter number to insert it into the list: ")))
#     num.pop()
#     print(num)
# playInList()

#_________________________________________________________________________________________________________
 # Create 2 dictionaries and append the two in one. {take into consideration unique keys }

firstDict = dict( name="Abdo", age=24, grade="B")
secondDict = dict( height = 176, weight = 66, name="mona" )

firstDict.update(secondDict)
print(firstDict)