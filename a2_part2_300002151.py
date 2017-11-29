# Family Name:Harshal Gautam
# Student Number: 300002151
# Course: ITI 1120[D]
# Assignment 2

##############################
#Question 2.1
##############################
def min_enclosing_rectangle(radius,x,y):
    '''(number,number,number)->None
    Preconditions: If side is a non-negative number, then the function prints None
    Prints None if side a non-negative number'''
    if radius >= 0:
        return(radius-x,radius-y)
    elif radius <= 0:
        return(None)

##############################
#Question 2.2
##############################
def series_sum():
    '''(int)->number
    If the user enters a negative integer the function should return None otherwise the function should return the sumer of the following series 1000 + 1/12 + 1/22 + 1/32 + 1/42 + ... + 1/n2 for the given integer n'''
    m= int(input("Please enter a non negative integer:"))
    if m== 0:
        return 1000
    elif m>0:
        add= 0
        while (m>0):
            add += 1/m**2
            m= m-1
        return 1000 +add
    else:
        return
    return

##############################
#Question 2.3
##############################
import math
def pell (n):
    '''(int)->number
    Precondition: the function takes one integer parameter n, of type int
    If n is negative, pell returns None. Else, pell returns the nth Pell number'''
    
    if n==0:
        return 0
    elif n==1:
        return 1
    elif n<0 :
        return
    else :
        m= (((1+ math.sqrt(2))**n)-((1-math.sqrt(2))**n))/(2* math.sqrt(2))
        return math.ceil(m)
    return

##############################
#Question 2.4
##############################
def countMembers(s):
    '''(str)->int
    Precondition: Not allowed to use Python's string methods
    Returns the number of characters in s, that are extraordinary''' 
    s= list(s)
    new1list= ['e','f','g','h','i','j','Q','R','S','T','U','V','W','X','2','3','4','5','6','!',',','"\"']
    count=0
    for i in s:
        if i in new1list:
            count=count+1
        return count

##############################
#Question 2.5
##############################
def casual_number(s):
    '''(str)->int
    Precondition: if a string in s looks like a number but with commas, you may assume that commas are in meaningful places i.e. you may assume that s will not be a string like ’1, 1, 345’.
    should return an integer representing a number in s. If s does not look like a number the function should return None.'''
    s= s.replace(',','')

    if((s[0]=='+' or s[0]=='-') and s[1:].isdigit()):
        return int(s)

    elif(s.isdigit()):
        return int(s)

    else:
        return None 

##############################
#Question 2.6
##############################
def alienNumbers(s):
    '''(str)->int
    Preconditions: try to make the whole body of this function only one line
    takes one string parameter s, and returns the integer value represented by s''' 
    s=list(s)
    new1list= ['T','y','!','a','N','U']
    a=0
    b=0
    c=0
    d=0
    e=0
    f=0
    for i in s:
        if i in new1list:
            if i == new1list[0]:
                a = a + 1024
            elif i in new1list[1]:
                b = b + 598
            elif i in new1list[2]:
                c = c + 121
            elif i in new1list[3]:
                d = d + 42
            elif i in new1list[4]:
                e = e + 6
            elif i in new1list[5]:
                f = f + 1
    return a+b+c+d+e+f

##############################
#Question 2.7
##############################
def alienNumbersAgain(s):
    '''(str)->number
    Precondition: Use accumulator variable
    takes a single string parameter s, and returns the numeric value of the number that s represents in the alien numbering system'''   
    s= list(s)
    new1list= ['T','y','!','a','N','U']
    a=0
    b=0
    c=0
    d=0
    e=0
    f=0
    for i in s:
        if i in new1list:
            if i == new1list[0]:
                a= a + 1024
            elif i in new1list[1]:
                b= b + 598
            elif i in new1list[2]:
                c= c + 121
            elif i in new1list[3]:
                d= d + 42
            elif i in new1list[4]:
                e= e + 6
            elif i in new1list[5]:
                f= f + 1
    return a+b+c+d+e+f

##############################
#Question 2.8
##############################
def encrypt(s):
    '''(str)->str
    has one parameter s where s is a string and encrypt returns a string which is the encrypted version of s''' 
    new0= ""
    new1= ""
    new2= ""

    if (len(s) > 3):
        for i in range(len(s)-1, (round(len(s)/2))-2,-1):
            new1 += s[i]

        for c in range(0, (round(len(s)/2))):
            new2 += s[c]

        for p in range (0, round(len(s)/2)):
            new0 += new1 [p]
            new0 += new2 [p]

        return (new0)

    elif (len(s) == 3):
        new0 += s[2]
        new0 += s[0]
        new0 += s[1]
        return new0

    else:
        s = s[::-1]
        return (s)

##############################
#Question 2.9
##############################
def oPify(s):
    '''(str)->str
    Preconditions: If at least one of the character is not a letter in the alphabet, it does not insert anything between that pair.
    takes a single string parameter (s) and returns a string. This function considers every pair of consecutive characters in s. It returns a string with the letters o and p inserted between every pair of consecutive characters of s, as follows.'''
    new= ""
    for i in range (len(s)-1):
        if (s[i].isalpha() and s[i+1].isalpha()):
            new += s[i]
            if (s[i] == s[i].upper()):
                new += "O"
            else:
                new += "o"
            if (s[i+1] == s[i+1].upper()):
                new += "p"
            else:
                new += "p"
        else:
            new += s[i]
    return(new +s[i+1])

##############################
#Question 2.10
##############################
def nonrepetitive(s):
    '''(str)->bool
    has one parameter, s, where s is a string. The function returns True if s is nonrepetitive and False otherwise.'''
    
    

    for i in range(1,int(len(s)/2) + 1):
      
        for j in range(len(s)):
  
            if(j+2*i <= len(s)):
                
                if(s[j:j+i] == s[j+i:j+2*i]):
                    return False
                
                return True
  

        
        

