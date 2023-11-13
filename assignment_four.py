# Liam T.
# oct. 26, 2023
# Unit four project, option 1

import random


def random_card():
    """draws a random card"""
    return(random.randint(1,11))


def who_wins(user,computer):
    '''determines who wins

    :param user: user's current total
    :param computer: dealer's current total
    :return: who wins
    '''
    print("you have",user,", I have", computer)
    if user > 21:
        return "you lose!"
    elif computer > 21:
        return "I lose!"
    elif user > 21 and computer > 21:
        return "we both lose!"
    elif user > computer:
        return "you win!"
    elif computer> user:
        return "I win!"
    elif user == computer:
        return "its a tie!"



def dealers_cards(computer):
    """determines dealer's cards

    :param computer: the dealer
    :return: total cards
    """
    dtotal = random_card()
    #print("I drew a", dtotal)
    computer = computer + dtotal
    return computer

def third_card(user):
    """asks user if they want to draw another card

    :param user: user's total
    :return: The users total with new card if yes
    """
    choice = input("would you like to draw another card? Type 'yes' or 'no'")
    if choice == "yes":
        r = random_card()
        print("you drew a", r)
        print("Your current total is", r + user)
        return r
    else:
        print("Your current total is", user)
        return user



def main():
    """
    let's put it all together :D
    :return: Who wins, and the game
    """
    user = random_card()
    print("your first card is", user)
    second_card = random_card()
    print("your second card is", second_card)
    user = user + second_card
    print("your total is", user)


    computer = 0
    dealers_total = dealers_cards(computer)
    #print("my total is", dealers_total)

    dealers_total2 = dealers_cards(dealers_total)
    #print("my total is", dealers_total2)


    third_card(user)

    print(who_wins(user, dealers_total2))

main()