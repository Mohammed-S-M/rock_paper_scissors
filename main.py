# importing art file.
import art
# importing random file.
import random
# import the clear function.
from os import system, name


# clear function to clear the console.
def clear():
    # for windows.
    if name == 'nt':
        _ = system('cls')

    # for mac and linux(here, os.name is 'posix').
    else:
        _ = system('clear')
# end of clear function.


# main function.
def rock_paper_scissors():
    # printing the game logo and the welcome message.
    clear()
    print(art.logo)
    print("Welcome to Rock Paper Scissors game.")
    print("The rock will break the scissors, the paper will eat the rock, and the scissors will cut the paper.")
    print("You need to reach 5 points to win. You vs. PC")
    print("Start the game.....")
    print("-------------------------------------------------------------------")
    print()

    # exporting the arts of rock paper and scissors and assign them to a variable.
    rock = art.rock
    paper = art.paper
    scissors = art.scissors

    # creating a list that hold all the choices.
    choices = [rock, paper, scissors]
    player_score = 0
    computer_score = 0

    # the game will keep going until the user or the pc score reaches 5
    game_over = False
    while not game_over:
        # asking the user to select a choice.
        print("What do you choose?")
        print("Type R for Rock, P for paper, and S for scissors.")
        user_input = input("Rock, Paper, or Scissors: ").lower()
        clear()
        # Making sure the user enter a valid answer.
        correct_choice = False
        while not correct_choice:
            # If the user entered something outside the game rules.
            if user_input == "r" or user_input == "p" or user_input == "s":
                correct_choice = True
            else:
                clear()
                print("Invalid entry, please try again.")
                print("What do you choose?")
                print("Type 'R' for Rock, 'P' for paper, and 'S' for scissors.")
                user_input = input("Rock, Paper, or Scissors: ").lower()
        # end of while loop.

        user_choice = 0
        # converting the user input from letters to numbers to pick a choice from the choices list.
        if user_input == "r":
            user_choice = 0
        elif user_input == "p":
            user_choice = 1
        elif user_input == "s":
            user_choice = 2

        # getting the user and computer choices from the choices list.
        player_choice = choices[user_choice]
        computer_choice = random.choice(choices)

        # printing the user and PC choices for the user to see who won.
        print(f"Your choice: \n{player_choice}")
        print(f"PC choice: \n{computer_choice}")

        # determine the winner
        if player_choice == rock and computer_choice == paper:
            winner = "---- PC won! ----"
            computer_score += 1
        elif player_choice == rock and computer_choice == scissors:
            winner = "---- You won! ----"
            player_score += 1
        elif player_choice == paper and computer_choice == rock:
            winner = "---- You won! ----"
            player_score += 1
        elif player_choice == paper and computer_choice == scissors:
            winner = "---- PC won! ----"
            computer_score += 1
        elif player_choice == scissors and computer_choice == rock:
            winner = "---- PC won! ----"
            computer_score += 1
        elif player_choice == scissors and computer_choice == paper:
            winner = "---- You won! ----"
            player_score += 1
        else:
            winner = "---- a Tie ----"

        # printing the winner and the score
        print(winner)
        print(f"Score => PC {computer_score} vs You {player_score}")

        if player_score == 5 and player_score > computer_score:
            print(f"Final score: {player_score} YOU vs PC {computer_score}")
            print("CONGRATS! you won the game.")
            game_over = True
        elif computer_score == 5 and computer_score > player_score:
            print(f"Final score: {player_score} YOU vs PC {computer_score}")
            print("You lost! PC won the game.")
            game_over = True
    # while loop end

    # after the game ended, we ask the user if they want to play again.
    replay = input("You want to play again Y or N? ").lower()
    if replay == "y":
        rock_paper_scissors()
    else:
        print("Thanks for playing, GOODBYE!")

# end of main function.


# calling the main function to start the game.
rock_paper_scissors()
