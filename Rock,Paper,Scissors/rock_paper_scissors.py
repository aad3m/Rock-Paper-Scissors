import random

# create list of moves
moves = ['Rock', 'Raper', 'Scissors']
# give computer_choice random move
computer_choice = random.choice(moves)

# set player to false
player_choice = False

while player_choice == False:
    # Change player to true
    player_choice = input("Rock, Paper, Scissors? ")
    # capitlize input to accept lowercase
    player_choice = player_choice.capitalize()
    # determines draw
    if player_choice == computer_choice:
        print("Draw!")
    # determines rock move
    elif player_choice == 'Rock':
        if computer_choice == 'Scissors':
            print("Player wins!")
        else:
            print("Computer wins!")
    # determines paper move
    elif player_choice == 'Paper':
        if computer_choice == 'Rock':
            print("Player wins!")
        else:
            print("Computer wins!")
    # determines scissors move
    elif player_choice == 'Scissors':
        if computer_choice == 'Paper':
            print("Player wins!")
        else:
            print("Computer wins!")
    # when user input if not valid
    else:
        print("Not a valid move")
    # option to end game
    end = input("Type 'N' to exit: ")
    end = end.lower()
    # end game
    if end == 'n':
        player_choice = True
    # continue game
    else:
        player_choice = False
        computer_choice = random.choice(moves)