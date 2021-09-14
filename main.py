from random import randint
from data import data
import art
from os import system
from time import sleep

a_dict = ""

b_dict = ""


def clear():
    system("cls")


def generate_values():
    global a_dict
    global b_dict
    a_int = randint(0, 49)
    a_dict = data[a_int]

    b_int = randint(0, 49)
    while b_int == a_int:
        b_int = randint(0, 49)
    b_dict = data[b_int]


def startup(is_start):
    clear()
    print(art.logo)
    if is_start:
        print("Welcome to Higher Lower!", end='')
    print("\n\n", end='')


def game():
    score = 0
    try_again = False

    fail = False
    while not fail:
        clear()
        if not try_again:
            generate_values()
        startup(False)
        vs(False)
        guess = input(f"Does {b_dict['name']} have a higher or lower number of followers than {a_dict['name']}? H for higher and L for lower: ").lower()
        if a_dict['follower_count'] > b_dict['follower_count']:
            is_higher = False
        else:
            is_higher = True

        clear()
        startup(False)
        vs(True)

        if is_higher and guess in ['higher', 'h'] or not is_higher and guess in ['lower', 'l']:
            input("Correct! Press [enter] on your keyboard when you are ready to move on.")
        elif is_higher and guess in ['l', 'lower'] or not is_higher and guess in ['h', 'higher']:
            print(f"That was incorrect. Game over. Your final score is {score}")
            return
        else:
            print("That was invalid. Try again")
            sleep(2)


def vs(show_follower_count_last):
    spaces = 63

    for index in range(0, spaces):
        print(" ", end='')
    print(art.vs_list[0])

    print(f"Name: {a_dict['name']}", end='')
    for index in range(0, spaces - len(a_dict['name']) - 6):
        print(" ", end='')
    print(art.vs_list[1], end='')
    for index in range(0, spaces - len(b_dict['name']) - 6):
        print(" ", end='')
    print(f"Name: {b_dict['name']}")

    print(f"Description: {a_dict['description']}", end='')
    for index in range(0, spaces - len(a_dict['description']) - 13):
        print(" ", end='')
    print(art.vs_list[2], end='')
    for index in range(0, spaces - len(b_dict['description']) - 13):
        print(" ", end='')
    print(f"Description: {b_dict['description']}")

    print(f"Country: {a_dict['country']}", end='')
    for index in range(0, spaces - len(a_dict['country']) - 9):
        print(" ", end='')
    print(art.vs_list[3], end='')
    for index in range(0, spaces - len(b_dict['country']) - 9):
        print(" ", end='')
    print(f"Country: {b_dict['country']}")

    print(f"Followers: {str(a_dict['follower_count'])},000,000", end='')
    for index in range(0, spaces - len(str(a_dict['follower_count'])) - 19):
        print(" ", end='')
    print(art.vs_list[4], end='')
    if not show_follower_count_last:
        for index in range(0, spaces - 14):
            print(" ", end='')
        print(f"Followers: ???")
    else:
        for index in range(0, spaces - len(str(a_dict['follower_count'])) - 19):
            print(" ", end='')
        print(f"Followers: {str(b_dict['follower_count'])},000,000")


generate_values()
startup(True)
game()
