# 1. Write a program that counts up the number of vowels [a, e, i, o, u] contained in the string.

# vowel = ["a","o","i","e","u"]
# message = "i am really tired"
# count = 0

# for i in message:
#     for l in vowel:
#         if(i == l):
#             count +=1
#             print(i)

# print ("the number of vowel letters is:",count)



#2. Write a function that accepts two arguments (length,start) to generate an array of a specific length filled with integer numbers increased by one from start.

# length =int( input ("gimme length for the array:") ) 
# start = int ( input("enter a number number:") )
# def arrayGenerator(length , start):
#     customArray = [start]
#     i = 1 
#     while i < length:
#         customArray.append(start +i)
#         i +=1

#     return customArray
    
# result = arrayGenerator(length , start)
# print(result)

#3. Fill an array of 5 elements from the user, Sort it in descending and ascending orders then display the output.

# numbersArray = []
# i = 0
# while i < 5 :
#     numbersArray.append(int(input(f"input the value number {i + 1}: ")))
#     i += 1

# numbersArray.sort()
# print(numbersArray)
# numbersArray.sort(reverse = True)
# print(numbersArray)


# 4. Write a function that takes a number as an argument and if the number divisible by 3 return "Fizz" and if it is divisible by 5 return "buzz" and if is divisible by both return "FizzBuzz"

# num = int(input("inter a number: "))
# def divisablity(num):
#     if(num%5 == 0 and num%3 == 0):
#         print("FIZZBUZZ")
#     elif(num%3 == 0):
#         print("FIZZ")
#     elif(num%5 == 0):
#         print("BUZZ")

# divisablity(num)

# 5. Write a Python function that checks whether a passed string is palindrome or not.Note: A palindrome is a word, phrase, or sequence that reads the same backward as forward, e.g., madam or nurses run {ignoring the spaces }.

# str = input("inter a word to check it: ")
# def palindromeFun(str):
#     if(str == str[::-1]):
#         print("The Word Is Palindrom")
#     else:
#         print("The Word Is Not Palindrom")

# palindromeFun(str)


#6. Write a function that takes a string and prints the longest alphabetical ordered substring occured. For example, if the string is 'abdulrahman' then the output is: Longest substring in alphabetical order is: abdu

# def longest_alphabetical_order(word):
#     word = input("Enter a word I can process: ")
#     max = "" 
#     curr = word[0]

#     i = 1 
#     while i < len(word):
#         if word[i] >= word[i - 1]:
#             curr += word[i]
#         else:
#             if len(curr) > len(max):
#                 max = curr
#             curr = word[i] 
#         i += 1  
   
#     if len(curr) > len(max):
#         max = curr

#     print("Longest alphabetical order is:", max)

# longest_alphabetical_order("")  
