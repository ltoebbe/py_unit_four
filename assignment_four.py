# Liam T.
# oct. 26, 2023
# Unit four project, option 1

import random

# define get_card function
# define get_user_total and get_dealer_total
# define get_winner
#   if user_total > 21, display lose
#   if user_total < dealer_total and dealer_total <= 21, display lose

# ask user if they want to play 21
#   if yes, continue. if no, print 'see you later then! :)'
# ask user to pull a card
# generate a random number between 1 and 10 called user_card
# generate a second random number between 1 and 10 called dealer_card
# print results
# ask user if they want to draw again
#   if yes, continue. if no, run get_winner and display results
# generate a random number between 1 and 10 called user_card
# generate a second random number between 1 and 10 called dealer_card
# add user's cards and dealer's cards
# print results
# ask user if they want to draw again
#   if yes, continue. if no, run get_winner and display results


def get_card():
    return random.randint(1, 10)


def user_total():
    u_card1 = get_card()
    print("you drew a ", u_card1)
    print("your total is now ", u_current + u_card1)


def dealer_total():
    d_card1 = get_card()
    print("I drew a ", d_card1)
    print("my total is now ", d_current + d_card1)


def get_winner(user_total, dealer_total):
    if user_total > 21 and dealer_total > 21:
        print("both lose!")
    elif user_total > 21 and dealer_total <= 21:
        print("I win "
              "gg ez")
    elif user_total <= 21 and dealer_total > 21:
        print("you win!")
    elif user_total < 21 and dealer_total < 21:
        input("the scores are ", user_total, dealer_total, ", would you like to draw another card? type 'y' for yes, 'n' for no.")
            if input = y:
                get_card()
            if input = n:
                get_winner(user_total, dealer_total)

# i'm gonna have a freaking conniption
# i can't make it work
# (-̥̥̥̥̥̥̥̥̥̥̥̥̥̥̥̥̥̥̥̥̥̥̥̥̥᷄_-̥̥̥̥̥̥̥̥̥̥̥̥̥̥̥̥̥̥̥̥̥̥̥̥̥᷅ )
