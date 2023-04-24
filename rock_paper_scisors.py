import random

def main():

    options = ['rock', 'paper', "scissors"]
    scoreboard = [0, 0, 0]

    user_flag = True
    print("Welcome to the exciting game of Rock, Paper Scisors!")
    user_choice = ''

    while user_flag:
        user_choice = input('Please pick a choice: rock, paper or scissors(or type "I quit" to end the fun): ').strip().lower()
        if user_choice == "i quit":
            final_results(scoreboard)
            user_flag = False
        while user_choice not in options and user_choice != 'i quit':
            user_choice = input('You did not enter a valid input! Please enter rock, paper or scissors: ')
            if user_choice == "i quit":
                final_results(scoreboard)
                user_flag = False
        print_results(win_results(user_choice, options), scoreboard)


def final_results(overall_wins):
    print("\nYou have decided to end the fun: So sorry to see you go!")
    print("But we have calculated your results and here they are:\n")
    print(f"Computer Wins: {overall_wins[1]}")
    print(f"Player Wins: {overall_wins[2]}")
    print(f"Games Tied: {overall_wins[0]}")
    print("\nThank you for playing with us! Have a great day!")


def win_results(player_choice, options):
    #rock = 0, paper = 1, scissors = 2
    comp_choice = random.randint(0,2)


    if  (comp_choice == 1 and player_choice == 'paper' or
         comp_choice == 2 and player_choice == 'scissors' or
         comp_choice == 0 and player_choice == 'rock'):
        return 0
    elif (comp_choice == 0 and player_choice == 'paper' or
         comp_choice == 1 and player_choice == 'scissors' or
         comp_choice == 2 and player_choice == 'rock'):
        return 1
    elif (comp_choice == 1 and player_choice == 'rock' or 
         comp_choice == 0 and player_choice == 'scissors' or 
         comp_choice == 2 and player_choice == 'paper'):
        return 2

def print_results(result, tally):
    if result == 0:
        print("Game Tied")
        tally[0] += 1
    elif result == 1:
        print("You Lose!")
        tally[1] += 1
    elif result == 2:
        print("You Win!!!!")
        tally[2] += 1


main()