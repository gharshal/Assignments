#Family Name: Harshal Gautam
#Student number: 300002151
#Course: ITI 1120[D]
#Assignment  3
####################
#Concentration Game
####################

import random

def shuffle_deck(deck):
    '''(list of str)->None
       Shuffles the given list of strings representing the playing deck
    '''
    print("\nShuffling the deck...\n")
    for i in range (len (deck)):
        random.shuffle(deck)


def create_board(size):
    '''int->list of str
       Precondition: size is even positive integer between 2 and 52
       Returns a rigorous deck (i.e. board) of a given size.
    '''
    board = [None]*size

    letter='A'
    for i in range(len(board)//2):
          board[i]=letter
          board[i+len(board)//2 ]=board[i]
          letter=chr(ord(letter)+1)
    return board

def print_board(a):
    '''(list of str)->None
       Prints the current board in a nicely formated way
    '''
    for i in range(len(a)):
        print('{0:4}'.format(a[i]), end=' ')
    print()
    for i in range(len(a)):
        print('{0:4}'.format(str(i+1)), end=' ')


def wait_for_player():
    '''()->None
    Pauses the program/game until the player presses enter
    '''
    input("\nPress enter to continue. ")
    print()

def print_revealed(discovered, p1, p2, original_board):
    '''(list of str, int, int, list of str)->None
    Prints the current board with the two new positions (p1 & p2) revealed from the original board
    Preconditions: p1 & p2 must be integers ranging from 1 to the length of the board
    '''
    discovered[p1-1]= original_board[p1-1]
    discovered[p2-1] = original_board[p2-1]
    return print_board(discovered)



#############################################################################
#   FUNCTIONS FOR OPTION 1 (with the board being read from a given file)    #
#############################################################################

def read_raw_board(file):
    '''str->list of str
    Returns a list of strings represeniting a deck of cards that was stored in a file.
    The deck may not necessarifly be playable
    '''
    raw_board = open(file).read().splitlines()
    for i in range(len(raw_board)):
        raw_board[i]=raw_board[i].strip()
    return raw_board


def clean_up_board(l):
    '''list of str->list of str

    The functions takes as input a list of strings representing a deck of cards.
    It returns a new list containing the same cards as l except that
    one of each cards that appears odd number of times in l is removed
    and all the cards with a * on their face sides are removed
    '''
    print("\nRemoving one of each cards that appears odd number of times and removing all stars ...\n")
    playable_board= []
    import copy

    playable_board = l

    for i in playable_board:
        if i == '*':
            playable_board.remove(i)
    for i in playable_board:
        if playable_board.count(i) == 1:
            playable_board.remove(i)
    for i in ((playable_board)):
        if ((playable_board.count(i)) %2) != 0:
            playable_board.remove(i)

    for i in ((playable_board)):
        if ((playable_board.count(i)) %2) != 0:
            playable_board.remove(i)

    return playable_board


def is_rigorous(l):
    '''list of str->True or None
    Returns True if every element in the list appears exactlly 2 times or the list is empty.
    Otherwise, it returns False.

    Precondition: Every element in the list appears even number of times
    '''

    for x in l:
        if ((l.count(x)) == 2):
            return True
        elif l==[]:
            return True
        else:
            return False




####################################################################3

def play_game(board):
    '''(list of str)->None
    Plays a concentration game using the given board
    Precondition: board a list representing a playable deck
    '''

    print("Ready to play ...\n")

    # this is the funciton that plays the game
    discovered= len(board)*['*']
    print_board(discovered)
    print()
    answer= False
    guess = 0
    pairs = 0
    while answer == False :

        print()
        print("Enter two distinct positions on the board that you want revelaed.\ni.e two integers in the range [1," +str(len(board))+"]")
        p1= int(input("Enter position 1: "))
        p2= int(input("Enter position 2: "))
        if p1 == p2 :
            print("You chose the same position")
            print("Please try agan. This guess did not count Your current number of guesses is " + str(guess))
        elif (discovered[p1-1]!= "*") or(discovered[p2-1]!="*"):
            print("One or both of the chosen portions has already been paired")
            print("Please try agan. This guess did not count Your current number of guesses is " + str(guess))

        else:
            print_revealed(discovered,p1,p2,board)
            guess +=1
            if discovered[p1-1]==discovered[p2-1]:
                pairs +=1
                wait_for_player()
                print(100*"\n")
                print_board(discovered)
            elif discovered[p1-1] != discovered[p2-1]:
                discovered[p1-1] = "*"
                discovered[p2-1] = "*"
                wait_for_player()
                print(100*"\n")
                print_board(discovered)
        if pairs == (len(board) // 2):
            answer = True
            print(1000*"\n")
            print("Congratulations you completed the game with "+str(guess)+ " guesses. Thats " + str(guess - (len(board) // 2)) + " more than the best possible")
#ascii plaque function
def ascii_name_plaque(name:str)->str:
    """Takes in an input of a string representing a person’s name and
    draws (using print function) a name plaque """
    y = len(name) + 8
    print ("*" * y)
    z= y-2
    print ("*" + " " *z + "*")
    print ("*" + " " +"__" + name + "__" +" " + "*")
    print ("*" + " " *z + "*")
    print ("*" * y)
    return

#main
ascii_name_plaque("Welcome to my Concentration game")
print()
print()
# YOUR CODE TO GET A CHOICE 1 or CHOCE 2 from a player GOES HERE
s = int(input("Would you like (enter 1 or 2 to indicate your choice )\n(1) me to generate arigorous deck of cards fr you \n(2) or, would you like me to read a deck from a file\n"))
option = False
while option == False:
    if s == 1:
        print ("You chose to have a rigorous deck of cards for you\n")
        option = True
    elif s==2:
        print("You chose to read a deck from a file\n")
        option = True
    else:
        s=int(input( str(s) + " is not an existing option. Please try again. Enter 1 or 2 to indicate your option\n"))




# YOUR CODE FOR OPTION 1 GOES HERE
if s == 1:
    option2= False
    while option2 == False:
        print()
        size= int(input("How many cards do you want to play with?\nEnter an even number between 0 and 52: "))
        if ((size % 2 == 0)and(0<size<= 52)):
            option2=True
            board=create_board(size)
            shuffle_deck(board)
            wait_for_player()
            print(1000*"\n")
            play_game(board)

# YOUR CODE FOR OPTION 2 GOES HERE
if s == 2:
    print("You chose to load a deck of cards from a file")
    file=input("Enter the name of the file: ")
    file=file.strip()
    board=read_raw_board(file)
    board=clean_up_board(board)
    ascii_name_plaque("This deck is now playable and rigorous and it has " +str(len(board))+ " cards.")
    print()
    print()
    wait_for_player()
    print(1000*"\n")
    shuffle_deck(board)
    wait_for_player()
    print(1000*"\n")
    if board == []:
        print("The resulting board is empty.\nPlaying the concentration game with an empty board is impossibe.\nGoodbye.")
    else:
        play_game(board)
