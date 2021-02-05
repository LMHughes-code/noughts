#--global veribles--

#game board, where the pices are placed in the list
board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-",]


#game playing
game_still_going = True


#winner starts as none, untill conditions meet
winner = None

#whos playing, starts as X
current_palyer = "X"

def display_key():
    print("Board Key - left to right")
    print("Row 1 = 1, 2, 3")
    print("Row 2 = 4, 5, 6")
    print("Row 3 = 7, 8, 9")



#turns the list into a board
def display_board():
    print("   |   |   |")
    print(" " + board[0] + " | " + board[1] + " | " + board[2] + " |")
    print("   |   |   |")
    print("---------------")
    print("   |   |   |")
    print(" " + board[3] + " | " + board[4] + " | " + board[5] + " |")
    print("   |   |   |")
    print("---------------")
    print("   |   |   |")
    print(" " + board[6] + " | " + board[7] + " | " + board[8] + " |")
    print("   |   |   |")


#this is the game 
def play_game():
    display_key()
    display_board() 
    #this while loop will run untill winner or tie
    while game_still_going:
        handle_turn(current_palyer)
        check_if_game_over()
        flip_player()

    #dysplays end of game
    if winner == "X" or winner == "O":
        print(winner + " won!")
    elif winner == None:
        print("Tie!")



#this switchs between X and O
def handle_turn(player):
    #makes it easier to see who is playing currently
    print(player + "'s turn!")
    position = input("Choose a position from 1-9")

    #this while loop stops invaild inputs that will crash the game
    #it stops positions being overwritten
    vaild = False
    while not vaild:
        while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            position = input("Invaild input. Choose a position from 1-9")

        position = int(position) - 1

        if board[position] == "-":
            vaild = True
        else:
            print("This is taken! Try again.")


    board[position]= player
    display_board()



def check_if_game_over():
    check_for_winner()
    check_if_tie()


#this includes the global winner, so it can be changed to true and show the winner
def check_for_winner():

    global winner


    #check rows
    row_winner = check_rows()
    #check colloms
    collom_winner = check_colloms()
    #check dignals
    dignal_winner = check_dignals()

    #if statement to check for winner
    if row_winner:
        winner = row_winner

    elif collom_winner:
        winner = collom_winner

    elif dignal_winner:
        winner = dignal_winner

    else:
        winner = None
    return



#checks for matchs, global game_still_running so it can change to false and end game
def check_rows():
    global game_still_going
    row_1 = board[0] == board[1] == board[2] != "-"
    row_2 = board[3] == board[4] == board[5] != "-"
    row_3 = board[6] == board[7] == board[8] != "-"
    if row_1 or row_2 or row_3:
        game_still_going = False

    if row_1:
        return board[0]
    elif row_2:
        return board[3]
    elif row_3:
        return board[6]
    
    return


#checks for matchs, global game_still_running so it can change to false and end game
def check_colloms():
    global game_still_going
    collom_1 = board[0] == board[3] == board[6] != "-"
    collom_2 = board[1] == board[4] == board[7] != "-"
    collom_3 = board[2] == board[5] == board[8] != "-"
    if collom_1 or collom_2 or collom_3:
        game_still_going = False

    if collom_1:
        return board[0]
    elif collom_2:
        return board[1]
    elif collom_3:
        return board[2]
    
    return


#checks for matchs, global game_still_running so it can change to false and end game
def check_dignals():
    global game_still_going
    dignals_1 = board[0] == board[4] == board[8] != "-"
    dignals_2 = board[6] == board[4] == board[2] != "-"

    if dignals_1 or dignals_2:
        game_still_going = False
    if dignals_1:
        return board[0]
    elif dignals_2:
        return board[6]


#checks if any moves can be made, if not it calls a tie
def check_if_tie():
    global game_still_going
    if "-" not in board:
        game_still_going = False
    return

#flips players
def flip_player():
    global current_palyer
    if current_palyer == "X":
        current_palyer = "O"
    elif current_palyer == "O":
        current_palyer = "X"
    return



play_game()