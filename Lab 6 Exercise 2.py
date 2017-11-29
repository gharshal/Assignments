Continue = 'yes'
while Continue == 'yes':

    x = input('Enter Two Integers Seperated By A Space:')
    a,b = x.split(" ")

    print(int(a)+int(b))

    Continue = input("Enter 'yes' to continue:")
    
