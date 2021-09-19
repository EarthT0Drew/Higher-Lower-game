from random import choice  # Imports
from data import data  # Imports data.py file
import art  # Imports art.py file
from os import system  # Allows for clear()

# Allows for viewage of these variables globaly (May clean up in future)
a_dict = ""
b_dict = ""
a_int = None
b_int = None


def clear():  # Uses os.system() to create clear() which clears the screen
    system("cls")


def generate_values(is_start):  # Chooses comparison accounts used in-game
    global a_dict  # Allows for modifications of these variables
    global b_dict

    if is_start:  # Finds if new game or if is new round
        a_dict = choice(data)  # Chooses first account

        b_dict = choice(data)  # Chooses second account
        while b_dict == a_dict:  # Sees if first value is the same as second value, if so, chooses new account untill not same
            b_dict = choice(data)
    else:
        a_dict = b_dict  # If new round, makes first account the second account, a and chooses a new account for second

        while b_dict == a_dict:
            b_dict = choice(data)


def startup(is_start):  # Shows the first few lines of the sceen
    clear()
    print(art.logo)
    if is_start:  # Shows 'Welcome to Higher Lower!' when done for first time
        print("Welcome to Higher Lower!", end='')
    print("\n\n", end='')


def game():
    score = 0  # Initial variables
    try_again = False
    initial_startup = True

    while True:
        clear()
        # Chooses new accounts when answer is valid (see more later) or if new game
        if not try_again:
            generate_values(initial_startup)
        startup(initial_startup)
        initial_startup = False

        # Shows the main comparison screen without follower count for second account
        vs(False)

        guess = input(
            f"Does {b_dict['name']} have a higher or lower number of followers than {a_dict['name']}? H for higher and L for lower: ").lower()

        if a_dict['follower_count'] > b_dict['follower_count']:  # Compairs both accounts
            is_higher = False
        else:
            is_higher = True

        clear()  # Starts new screen that is same except that answer is shown for second account
        startup(False)
        if not try_again:
            vs(True)
        else:
            vs(False)
        try_again = False

        # Compares guess to answer
        if is_higher and guess in ['higher', 'h'] or not is_higher and guess in ['lower', 'l']:
            score += 1
            input(
                "Correct! Press [enter] on your keyboard when you are ready to move on.")
        elif is_higher and guess in ['l', 'lower'] or not is_higher and guess in ['h', 'higher']:
            print(
                f"That was incorrect. Game over. Your final score is {score}")
            return
        else:
            input(
                "That was invalid. Press [enter] on your keyboard to try again")  # Invalid input, does not choose new account
            try_again = True


def vs(show_follower_count_last):
    spaces = 63  # Describes the number of characters that is between the begining of the sceen and the beginning of the 'vs', and the space between 'vs' and the end of screen

    for index in range(0, spaces):  # Shows first row
        print(" ", end='')
    print(art.vs_list[0])

    print(f"Name: {a_dict['name']}", end='')
    for index in range(0, spaces - len(a_dict['name']) - 6):
        print(" ", end='')
    print(art.vs_list[1], end='')
    for index in range(0, spaces - len(b_dict['name']) - 6):
        print(" ", end='')
    print(f"Name: {b_dict['name']}")

    print(f"Description: {a_dict['description']}", end='')  # Shows second row
    for index in range(0, spaces - len(a_dict['description']) - 13):
        print(" ", end='')
    print(art.vs_list[2], end='')
    for index in range(0, spaces - len(b_dict['description']) - 13):
        print(" ", end='')
    print(f"Description: {b_dict['description']}")

    print(f"Country: {a_dict['country']}", end='')  # Shows third row
    for index in range(0, spaces - len(a_dict['country']) - 9):
        print(" ", end='')
    print(art.vs_list[3], end='')
    for index in range(0, spaces - len(b_dict['country']) - 9):
        print(" ", end='')
    print(f"Country: {b_dict['country']}")

    # Shows fourth row
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


game()
