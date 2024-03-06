from optparse import Option
import time
from unicodedata import name
seconds = 10
for i in range (0,10):
    time.sleep(10)
name = input ('enter your name :  ')
while True:
    total_questions=3
    correct = 0
    print('a) start quiz')
    print("b) exit")
    Option= input ("enter your option( press 'a' to start or press 'b' to exit) ")
    print()
    print()
    if Option==  "a":
        print('1 . What is the correct way to define a function in python?')
        print(" a) def function_name(parameters): b) function function_name(parameters): c) function function_name {parameters} d) function function_name(parameters) ")
        ans=input("Enter your answer : ")
        if ans == "a":
            correct+=1
            print()
            print()
        print('2. What is the correct way to call a function in python?')
        print(" a) function_name(arguments) b) function_name arguments c) function_name {arguments} d) function_name(arguments) ")
        ans=input("Enter your answer : ")
        if ans == "a":
            correct+=1
            print()
            print()
        print('3. What is the correct way to define a list in python?')
        print(" a) list_name = [1,2,3] b) list_name = (1,2,3) c) list_name = {1,2,3} d) list_name = [1,2,3] ")
        ans=input("Enter your answer : ")
        if ans == "a":
            correct+=1
            print()
            print()
    else:
        exit()
    print("total score : ", correct)
    percentage  = correct*100/3
    print ("your percentage :",percentage)

        
