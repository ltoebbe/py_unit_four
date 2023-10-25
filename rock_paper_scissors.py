import random


def who_wins(user, computer):
    # 1 is rock, 2 is paper, 3 is scissors, 4 is lizard, 5 is spock
    rock_victory = rock + scissors
    rock_victory = rock + lizard

    paper_victory = paper + rock
    paper_victory = paper + spock

    scissors_victory = scissors + paper
    scissors_victory = scissors + lizard

    lizard_victory = lizard + paper
    lizard_victory = lizard + spock

    spock_victory = spock + rock
    spock_victory = spock + scissors



def main():
    comp_play = randint(1, 5)
    user_play = input("choose rock, paper, scissors, lizard, or spock:")



if __name__ == '__main__':
    main()
