import string
import random
#-----------------------------------------
#               Configurations
#-----------------------------------------

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

buildings = {"Residential":"R","Industry":"I","Commercial":"C","Park":"O","Road":"*"}

player = {"coins":16,
          "points":0}

upper = list(string.ascii_uppercase)

#-----------------------------------------
#               Field print
#-----------------------------------------

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


#-----------------------------------------
#               GAME MENU
#-----------------------------------------

def game_menu():
    valid = ["1","2","3"]
    while True:
        print_field(field)
        print("╔══════════════════════════════════════════╗")
        print(f"║  Coins: {player['coins']: <4} 💰    Points: {player['points']: <4} 🌟       ║")
        print("╚══════════════════════════════════════════╝")
        print()
        print("1. Build Buildings     ")
        print()
        print("2. Save game    3. Exit to Main Menu")
        option = input("\nYour choice? ") #Prompt user for choice
        if option not in valid:
            continue
        else:
            if option == "1":
                build_buildings()
            elif option == "2":
                print("Unincorporated Feature")
            elif option == "3":
                print("Unincorporated Feature")
    return

#-----------------------------------------
#               Display Main Menu
#-----------------------------------------

def show_main_menu():
    print("1. Start new game")
    print("2. Load saved game")
    print("3. Display high scores")
    print("4. Exit")

#-----------------------------------------
#              Option input
#-----------------------------------------

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
#               Initialize game
#-----------------------------------------

def initialize_game(save = None):
    if save == None:
        player["coins"] = 16
        player["points"] = 0

#-----------------------------------------
#                Build Buildings
#-----------------------------------------

def get_building_choice():
    keys = list(buildings.keys())
    
    First_Building = random.choice(keys)
    keys.remove(First_Building)
    
    Second_Building = random.choice(keys)
    
    temp = [First_Building, Second_Building]
    return temp

def build_buildings():
    
    temp = get_building_choice()

    print(f"Available Buildings: {temp[0]} , {temp[1]}")
    choice = input("Which building would you want? Press 1 or 2: ")
    while True:
        if choice == "1" or choice == "2":
            field_location = input("Where to place? ")
            if len(field_location) != 2 and len(field_location) != 3:
                print("Invalid Input!")
            else:
                try:
                    if (field_location[0].upper() not in upper or (int(field_location[1:]) < 1 or int(field_location[1:])>20) or field[int(field_location[1:])-1][ord(field_location[0].upper()) - ord('A')] != None):
                            print("Invalid Input!")
                    else:
                        row = int(field_location[1:])-1
                        column = ord(field_location[0].upper()) - ord('A')
                        field[row][column] = buildings[temp[int(choice)-1]]
                        player['coins'] -= 1
                        calculate_points(row, column, player)
                        return
                except:
                    print("Invalid Input!")
        else:
            print("Invalid Input!")
            choice = input("Which building would you want? Press 1 or 2: ")

            continue

#-----------------------------------------
#               Calculate points
#-----------------------------------------

def calculate_points(row, column, player):
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # right, down, left, up
    building = field[row][column]
    accumulated_points = 0
    if building is not None:
        # Residential
        if building == 'R':
            for dx, dy in directions:
                nx, ny = row + dx, column + dy
                if 0 <= nx < len(field) and 0 <= ny < len(field[nx]):
                    if field[nx][ny] != None:
                        if field[nx][ny] == 'I':
                            accumulated_points = 1
                            player['coins'] += 1
                            break
                        elif field[nx][ny] == 'R':
                            accumulated_points += 1
                        elif field[nx][ny] == 'C':
                            accumulated_points += 1
                            player['coins'] += 1
                        elif field[nx][ny] == 'O':
                            accumulated_points += 2

        # Industry
        elif building == 'I':
            accumulated_points += 1
            for dx, dy in directions:
                nx, ny = row + dx, column + dy
                if 0 <= nx < len(field) and 0 <= ny < len(field[nx]):
                    if field[nx][ny] != None:
                        if field[nx][ny] == 'R':
                            accumulated_points += 1
                            player['coins'] += 1

        # Commercial
        elif building == 'C':
            for dx, dy in directions:
                nx, ny = row + dx, column + dy
                if 0 <= nx < len(field) and 0 <= ny < len(field[nx]):
                    if field[nx][ny] != None:
                        if field[nx][ny] == 'C':
                            accumulated_points += 1
                        elif field[nx][ny] == 'R':
                            accumulated_points += 1
                            player['coins'] += 1
        # Park
        elif building == 'O':
            for dx, dy in directions:
                nx, ny = row + dx, column + dy
                if 0 <= nx < len(field) and 0 <= ny < len(field[nx]):
                    if field[nx][ny] != None:
                        if field[nx][ny] == 'O':
                            accumulated_points += 1

        # Road
        elif building == '*':
            road_directions = [(0, 1), (0, -1)]  # right, left
            for dx, dy in road_directions:
                nx, ny = row + dx, column + dy
                if 0 <= nx < len(field) and 0 <= ny < len(field[nx]):
                    if field[nx][ny] != None:
                        if field[nx][ny] == '*':
                            accumulated_points += 1
                        if field[nx][ny] == 'R':
                            accumulated_points += 2
        
        player['points'] += accumulated_points

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
        choice = game_menu()

        
elif choice == '2':
    initialize_game()
    # load_game(game_vars)
    # main_gameplay()
    print("2")        

elif choice == '3':
    print("\nHigh Scores")

        
