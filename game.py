import random

# Game variables


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


#-----------------------------------------
#               MAIN GAME
#-----------------------------------------

print("\nNgee Ann City")
print("-------------------")
print("Build the happiest and most prosperous city!")
print()

show_main_menu()

while True:
    
    choice = get_main_choice()
    
    if choice == '1':
         
        # create_new_game()
        # main_gameplay()
        print("1")

            
    elif choice == '2':
        # initialize_game()
        # load_game(game_vars)
        # main_gameplay()
        print("2")        

    elif choice == '3':
        print("\nHigh Scores")

    elif choice == '4':
        break
    