from random import randint  # Imports
from data import data  # Imports data.py file
import art  # Imports art.py file
from os import system  # Allows for clear()

# Allows for viewage of these variables globaly (May clean up in future)
a_dict = ""
b_dict = ""


def clear():  # Uses os.system() to create clear() which clears the screen
    system("cls")


def generate_values():  # Generates comparison values used in-game
    global a_dict  # Allows for modifications of these variables
    global b_dict

    a_int = randint(0, 49)  # Generates comparison value for the first one
    a_dict = data[a_int]  # Finishes defining first comparison value

    b_int = randint(0, 49)  # Generates comparison value for second one
    while b_int == a_int:  # Sees if first value is the same as second value, if so, generates new value untill not same
        b_int = randint(0, 49)
    b_dict = data[b_int]  # Finishes defining second comparison value


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
        # Generates new values when answer is valid (see more later)
        if not try_again:
            generate_values()
        try_again = False
        startup(initial_startup)
        initial_startup = False

        # Shows the main comparison screen without follower count for second comparison value
        vs(False)

        guess = input(
            f"Does {b_dict['name']} have a higher or lower number of followers than {a_dict['name']}? H for higher and L for lower: ").lower()

        if a_dict['follower_count'] > b_dict['follower_count']:  # Compairs both values
            is_higher = False
        else:
            is_higher = True

        clear()  # Starts new screen that is same except that answer is shown for second value
        startup(False)
        vs(True)

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
                "That was invalid. Press [enter] on your keyboard to try again")  # Invalid input, does not generate new values
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

    print(f"Followers: {str(a_dict['follower_count'])},000,000", end='')  # Shows fourth row
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
game()
