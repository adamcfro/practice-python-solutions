from random import choice

throws = ['rock', 'paper', 'scissors']

def gameplay():
    play_again = 'yes'
    while play_again == 'yes':
        player_input = ''
        while player_input not in throws:
            player_input = input("Rock, paper, or scissors? ").lower()
        comp_input = choice(throws)
        print(f"Computer chooses {comp_input}.")

        if player_input == comp_input:
            print("Draw!")
        elif player_input == 'rock' and comp_input == 'scissors':
            print("Player wins!")
        elif player_input == 'scissors' and comp_input == 'paper':
            print("Player wins!")
        elif player_input == 'paper' and comp_input == 'rock':
            print("Player wins!")
        else:
            print("computer wins!")
        play_again = input("Play again? (yes or no) ")

gameplay()