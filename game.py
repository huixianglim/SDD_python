import string
import random


field = [ [None, None, None, None, None, None, None,None, None, None, None, None,None, None, None, None, None,None, None, None],
          [None, None, None, None, None, None, None,None, None, None, None, None,None, None, None, None, None,None, None, None],
          [None, None, None, None, None, None, None,None, None, None, None, None,None, None, None, None, None,None, None, None],
          [None, None, None, None, None, None, None,None, None, None, None, None,None, None, None, None, None,None, None, None],
       [None, None, None, None, None, None, None,None, None, None, None, None,None, None, None, None, None,None, None, None], 
       [None, None, None, None, None, None, None,None, None, None, None, None,None, None, None, None, None,None, None, None],
          [None, None, None, None, None, None, None,None, None, None, None, None,None, None, None, None, None,None, None, None],
          [None, None, None, None, None, None, None,None, None, None, None, None,None, None, None, None, None,None, None, None],
          [None, None, None, None, None, None, None,None, None, None, None, None,None, None, None, None, None,None, None, None],
       [None, None, None, None, None, None, None,None, None, None, None, None,None, None, None, None, None,None, None, None],
       [None, None, None, None, None, None, None,None, None, None, None, None,None, None, None, None, None,None, None, None],
          [None, None, None, None, None, None, None,None, None, None, None, None,None, None, None, None, None,None, None, None],
          [None, None, None, None, None, None, None,None, None, None, None, None,None, None, None, None, None,None, None, None],
          [None, None, None, None, None, None, None,None, None, None, None, None,None, None, None, None, None,None, None, None],
       [None, None, None, None, None, None, None,None, None, None, None, None,None, None, None, None, None,None, None, None],
       [None, None, None, None, None, None, None,None, None, None, None, None,None, None, None, None, None,None, None, None],
          [None, None, None, None, None, None, None,None, None, None, None, None,None, None, None, None, None,None, None, None],
          [None, None, None, None, None, None, None,None, None, None, None, None,None, None, None, None, None,None, None, None],
          [None, None, None, None, None, None, None,None, None, None, None, None,None, None, None, None, None,None, None, None],
       [None, None, None, None, None, None, None,None, None, None, None, None,None, None, None, None, None,None, None, None]]

buildings = ["Residential","Industry","Commercial","Park","Road"]

player = {"coins":16,
          "points":0}

upper = list(string.ascii_uppercase)
def print_field(field):
    print("   {:>5}".format(upper[0]),end="")

    for i in range(len(field)-1):
        print("{:>6}".format(upper[i+1]),end="")
    print()
    for i in range(len(field)):
        print('    +-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+')
        print('{:^3}'.format(i+1),end="")

        for j in range(len(field[i])):
            if field[i][j] is None:
                print(' |', end='    ')  # Print an empty cell
            else:
                name = field[i][j]
                print(' | {:^3}'.format(name[0].upper()), end='')  # Print the name of the entity

        print(' |')  # End the row with the right border

    print('    +-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+')


def game_menu():
    valid = ["1","2","3"]
    while True:
        print()
        print("1. Build Buildings     ")
        print()
        print("3. Save game    4. Exit to Main Menu")
        option = input("\nYour choice? ") #Prompt user for choice
        if option not in valid:
            continue
        else:
            if choice == "1":
                build_buildings()
            return


def show_main_menu():
    print("1. Start new game")
    print("2. Load saved game")
    print("3. Display high scores")
    print("4. Exit")

def get_main_choice():
    choice = input("\nYour choice? ") #Prompt user for choice
    if (choice != '1' and choice != '2' and choice != '3'):
        is_invalid = True          #Validation of choice
        while is_invalid: 
            choice = input('Invalid input. Please select a proper choice ')
            if choice == '1' or choice == '2' or choice == '3':
                is_invalid = False
                
    return choice

def initialize_game(save = None):
    if save == None:
        player["coins"] = 16
        player["points"] = 0

def build_buildings():
    temp = [buildings[random.randint(0,4)], buildings[random.randint(0,4)]]
    print(f"Available Buildings: {temp[0]} , {temp[1]}")
    choice = input("Which building would you want? Press 1 or 2: ")
    while True:
        if choice == "1" or choice == "2":
            field_location = input("Where to place?")
            if len(field_location) != 2:
                print("Invalid Input!")
                continue
            else:
                try:
                    if (field_location[0].upper() not in upper and (int(field_location[1]) < 1 or int(field_location[1])>20)):
                            print("Invalid Input!")
                    else:
                        field[upper.index(field_location[0].upper())][int(field_location[1])-1] = temp[int(choice)]
                        return
                except:
                    print("Invalid Input!")

#-----------------------------------------
#               MAIN GAME
#-----------------------------------------

print("\nNgee Ann City")
print("-------------------")
print("Build the happiest and most prosperous city!")
print()
show_main_menu()
choice = get_main_choice()

if choice == '1':
    while True:
        initialize_game()
        print_field(field)
        choice = game_menu()

        
elif choice == '2':
    initialize_game()
    # load_game(game_vars)
    # main_gameplay()
    print("2")        

elif choice == '3':
    print("\nHigh Scores")

        
