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
    print(f"Computer wins: {overall_wins[1]}")
    print(f"Player wins: {overall_wins[2]}")
    print(f"Computer wins: {overall_wins[0]}")
    print("\nThank you for playing with us! Have a great day!")


def win_results(player_choice, options):
    comp_choice = random.choice(options)

    if comp_choice == player_choice:
        return 0
    elif (comp_choice == "rock" and player_choice == 'paper' or
         comp_choice == 'paper' and player_choice == 'scissors' or
         comp_choice == 'scissors' and player_choice == 'rock'):
        return 1
    elif (comp_choice == "paper" and player_choice == 'rock' or 
         comp_choice == 'rock' and player_choice == 'scissors' or 
         comp_choice == 'scissors' and player_choice == 'paper'):
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