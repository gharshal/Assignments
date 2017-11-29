# Family Name: Harshal Gautam
# Student Number: 300002151
# Course: ITI 1120[D]
# Assignment 2

import math
import random

def primary_school_quiz(flag, n):

    '''(int, int) -> string
    The function gives a student an option of either an exponentiation or subtraction training quiz
    Preconditions: n is a non-negative integer
    '''
    
    if flag == 0:
        subtraction = True
        exponentiation = False
    elif flag == 1:
        subtraction = False
        exponentiation = True

    correct = 0

    for k in range (1, n + 1):
        num0 = random.randint(0, 9)
        num1 = random.randint(0, 9)

        if (subtraction == True):
            answer = 0
            print("Question " + str(k) + ": ")
            answer = int(input("What is the result of " + str(num0) + "-" + str(num1) + "? "))
            if (answer == (num0 - num1)):
                correct = correct + 1

        elif (exponentiation == True):
            answer = 0
            print("Question " + str(k) + ": ")
            answer = int(input("What is the result of " + str(num0) + "^" + str(num1) + "? "))
            if (answer == (num0**num1)):
                correct += 1
    if ((correct/n) * 100) >= 90:
        print("Congratulations " + name + "! You'll probably get an A tomorrow. Now go eat your dinner and go to sleep") 

    elif 70 >= ((correct/n) * 100) < 90:
        print("You did well " + name + ", but I know you can do better.")

    else:
        print("I think you need some more practice")
        
def high_school_eqsolver(a,b,c):
    
    if (a != 0):
    
        if (b**2 - (4*a*c)) < 0:
            print("The quadratic equation " + str(a) + "·x^2 + " + str(b) + "·x + " + str(c) + " = 0")
            print("has the following two complex roots:")
            print(str(-b/(2*a)) + str(" + i ") + str(((-(b**2 - 4*a*c))**0.5)/(2*a)))
            print("and")
            print(str(-b/(2*a)) + str(" - i ") + str(((-(b**2 - 4*a*c))**0.5)/(2*a)))

        elif (b**2 - (4*a*c)) == 0:
            print("The quadratic equation " + str(a) + "·x^2 + " + str(b) + "·x + " + str(c) + " = 0")
            print("has only one solution, a real root: ")
            print(str((-b + (b**2 - 4*a*c)**0.5)/(2*a)))
            
        elif (b**2 - (4*a*c)) > 0:
            print("The quadratic equation " + str(a) + "·x^2 + " + str(b) + "·x + " + str(c) + " = 0")
            print("has the following two real roots:")
            print(str(((-b + (b**2 - 4*a*c)**0.5)/(2*a))) + " and " + (str(((-b - (b**2 - 4*a*c)**0.5)/(2*a)))))

    elif (a == 0 and b!= 0):
        print("The linear equation " + str(b) + "·x + " + str(c) + " = 0")
        print("has the following root/solution: " + str((-c)/b))    

    elif (a == 0 and b == 0 and c != 0):
        print("The quadratic equation " + str(b) + " + " + str(c) + " = 0")
        print("is satisfied for no number x")
        
    elif (a == 0 and b == 0 and c == 0):
        print("The quadratic equation " + str(b) + " + " + str(c) + " = 0")
        print("is satisfied for all numbers x")
    
print((len("Welcome to my math quiz-generator / equation-solver")+8)*"*")
print("*" + (len("Welcome to my math quiz-generator / equation-solver")+6) * " " + "*")
print("*" + " __" + "Welcome to my math quiz-generator / equation-solver" + "__ " + "*")
print("*" + (len("Welcome to my math quiz-generator / equation-solver")+6) * " " + "*")
print((len("Welcome to my math quiz-generator / equation-solver")+8)*"*")

name=input("What is your name? ")

status=input("Hi "+name+". Are you in? Enter \n1 for primary school\n2 for high school or\n3 for none of the above?\n")

if status=='1':
    
    print((len((name + ", welcome to my quiz-generator for primary school students."))+8)*"*")
    print("*" + (len((name + ", welcome to my quiz-generator for primary school students."))+6) * " " + "*")
    print("*" + " __" + (name + ", welcome to my quiz-generator for primary school students.") + "__ " + "*")
    print("*" + (len((name + ", welcome to my quiz-generator for primary school students."))+6) * " " + "*")
    print((len((name + ", welcome to my quiz-generator for primary school students."))+8)*"*")

    flag = int(input("What would you like to practice? Enter \n0 for subtraction\n1 for exponentiation\n"))
    n = int(input("How many practice questions would you like to do? "))
    print(name + ", here are your " + str(n) + " questions: ")
    primary_school_quiz(flag, n)
    
elif status=='2':

    print((len("Welcome to my math quiz-generator / equation-solver")+8)*"*")
    print("*" + (len("Welcome to my math quiz-generator / equation-solver")+6) * " " + "*")
    print("*" + " __" + "Welcome to my math quiz-generator / equation-solver" + "__ " + "*")
    print("*" + (len("Welcome to my math quiz-generator / equation-solver")+6) * " " + "*")
    print((len("Welcome to my math quiz-generator / equation-solver")+8)*"*")
    
    flag=True
    while flag:
        question=input(name+", would you like a quadratic equation solved? ")
        question = question.lower().strip()

        if question!="yes":
            flag=False
        else:
            print("Good choice!")
            a = int(input("Enter a number for the coefficient a: "))
            b = int(input("Enter a number for the coefficient b: "))
            c = int(input("Enter a number for the coefficient c: "))
            high_school_eqsolver(a, b, c)
 
else:
    print(name + " you are not a target audience for this software.")

print("Good bye "+name+"!")

