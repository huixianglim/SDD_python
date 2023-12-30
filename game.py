import string
import random
#-----------------------------------------
#               Configurations
#-----------------------------------------

field = [
    [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
]

buildings = {"Residential":"R","Industry":"I","Commercial":"C","Park":"O","Road":"*"}

class Players:
    def __init__(self, points: int, coins: int):
        self.points = points
        self.coins = coins

player = Players(points=0, coins=16)

class Records:
      def __init__(self, name: str, points: int):
        self.player = name
        self.points = points
    
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
        print(f"║  Coins: {player.coins: <4} 💰    Points: {player.points: <4} 🌟       ║")
        print("╚══════════════════════════════════════════╝")
        print()
        print("1. Build Buildings     ")
        print()
        print("2. Save game    3. Exit to Main Menu")
        option = input("\nYour choice? ") #Prompt user for choice
        if option not in valid:
            print('Invalid input! Please try again!')
            print()
            continue
        else:
            if option == "1":
                if not build_buildings():
                    break
            elif option == "2":
                save_game()
            elif option == "3":
                print("\nReturning to the main menu...")
                break
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
    if (choice != '1' and choice != '2' and choice != '3' and choice != '4'):
        is_invalid = True          #Validation of choice
        while is_invalid: 
            choice = input('Invalid input. Please select a proper choice ')
            if choice == '1' or choice == '2' or choice == '3' or choice == '4':
                is_invalid = False
                
    return choice

#-----------------------------------------
#               Initialize game
#-----------------------------------------

def initialize_game(save = None):
    if save == None:
        player.coins = 16
        player.points = 0
        for row in range(len(field)):
                for column in range(len(field[row])):
                    field[row][column] = None

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

    print(f"Available Buildings: [1] {temp[0]} , [2] {temp[1]}")
    choice = input("Which building would you want? Press 1 or 2: ")

    while True:
        if choice == "1" or choice == "2":
            field_location = input("Where to place? ")
            if len(field_location) != 2 and len(field_location) != 3:
                print("Invalid Input!")
            else:
                try:
                    if is_field_empty(field) or is_connected(field_location):
                        if (
                            field_location[0].upper() not in upper
                            or (int(field_location[1:]) < 1 or int(field_location[1:]) > 20)
                            or field[int(field_location[1:]) - 1][
                                ord(field_location[0].upper()) - ord("A")
                            ]
                            != None
                        ):
                            print("Invalid Input!")
                        else:
                            row = int(field_location[1:]) - 1
                            column = ord(field_location[0].upper()) - ord("A")
                            field[row][column] = buildings[temp[int(choice) - 1]]
                            player.coins -= 1
                            calculate_points(player)

                            if check_game_over(player, field):
                                return False
                            else:
                                return True
                    else:
                        print("Invalid Building Location!")
                except:
                    print("Invalid Input!")
        else:
            print("Invalid Input!")
            choice = input("Which building would you want? Press 1 or 2: ")
            continue

def is_field_empty(field):
    for row in field:
        for element in row:
            if element is not None:
                return False
    return True

# Function to check if the given location is connected to existing buildings
def is_connected(location):
    row = int(location[1:]) - 1
    column = ord(location[0].upper()) - ord("A")

    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # right, down, left, up

    for dx, dy in directions:
        nx, ny = row + dx, column + dy
        if 0 <= nx < len(field) and 0 <= ny < len(field[nx]):
            if field[nx][ny] is not None:
                return True

    return False

#-----------------------------------------
#               Calculate points
#-----------------------------------------

def calculate_points(player):
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # right, down, left, up
   # placed_building = field[row][column]
    accumulated_points = 0
    accumulated_coins = 0
    original_coins = player.coins
    for row in range(len(field)):
        for column in range(len(field[0])):
            accum2points = 0
            building = field[row][column]
            if building is not None:
                # Residential
                if building == 'R':
                    for dx, dy in directions:
                        nx, ny = row + dx, column + dy
                        if 0 <= nx < len(field) and 0 <= ny < len(field[nx]):
                            if field[nx][ny] != None:
                                if field[nx][ny] == 'I':
                                    accum2points = 1
                                    break
                                elif field[nx][ny] == 'R' or 'C':
                                    accum2points += 1
                                elif field[nx][ny] == 'O':
                                    accum2points += 2
                    accumulated_points += accum2points

                # Industry
                elif building == 'I':
                    accumulated_points += 1
                    for dx, dy in directions:
                        nx, ny = row + dx, column + dy
                        if 0 <= nx < len(field) and 0 <= ny < len(field[nx]):
                            if field[nx][ny] != None:
                                if field[nx][ny] == 'R':
                                    accumulated_coins += 1

                # Commercial
                elif building == 'C':
                    for dx, dy in directions:
                        nx, ny = row + dx, column + dy
                        if 0 <= nx < len(field) and 0 <= ny < len(field[nx]):
                            if field[nx][ny] != None:
                                if field[nx][ny] == 'C':
                                    accumulated_points += 1
                                elif field[nx][ny] == 'R':
                                    accumulated_coins += 1

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
        
              

    player.points = accumulated_points
    player.coins = accumulated_coins + original_coins

#-----------------------------------------
#               LEADERBOARD SAVE 
#-----------------------------------------
def update_leaderboard(player1:Players):
    f = open("player.txt",'r+')
    people_array = []
    for line in f:
       player,points = line.split('|')

       temp = Records(player,int(points))
       people_array.append(temp)
    people_array = sorted(people_array, key=lambda x: x.points, reverse=True)
    size = len(people_array)

    if size != 10:
        print("\n🎉 Congratulations! You are currently in the top 10 of the leaderboard! 🎉")
        print(f"\nYour current score: {player1.points} points\n")
        name = input('Please enter your name: ')
        while True:
            if len(name) > 10:
                print("Please try again!(Name length must be less than or equal to 10 characters)")
                name = input('Please enter your name: ')
            else:
                break
        temp_append = Records(name,player1.points)
        insert_index = 0
        while insert_index < len(people_array) and temp_append.points <= people_array[insert_index].points:
            insert_index += 1

        people_array.insert(insert_index, temp_append)

    else:
        for i, existing_player in enumerate(people_array):
            if player1.points > existing_player.points:
                print(f"\nYour current score: {player1.points} points\n")
                print("\n🎉 Congratulations! You are currently in the top 10 of the leaderboard! 🎉")
                name = input('Please enter your name: ')
                while True:
                    if len(name) > 10:
                        print("Please try again!(Name length must be less than or equal to 10 characters)")
                        name = input('Please enter your name: ')
                    else:
                        break
                temp_append = Records(name,player1.points)
                people_array.insert(i, temp_append)
                break

            elif player1.points == existing_player.points:
                if i < 9:
                    last_index = i
                    for x in range(i+1, len(people_array)):
                        if (player1.points == people_array[x].points):
                            last_index = x
                        else:
                            break
                    if last_index < 9:
                        print(f"\nYour current score: {player1.points} points\n")
                        print("\n🎉 Congratulations! You are currently in the top 10 of the leaderboard! 🎉")
                        name = input('Please enter your name: ')
                        while True:
                            if len(name) > 10:
                                print("Please try again!(Name length must be less than or equal to 10 characters)")
                                name = input('Please enter your name: ')
                            else:
                                break
                        temp_append = Records(name,player1.points)
                        people_array.insert(i+1, temp_append)
                        break
            
    

    people_array = people_array[:10]
    
    f.seek(0)
    for i in people_array:
        f.write(f"{i.player}|{i.points}")
        f.write('\n')
    
    f.close()

#-----------------------------------------
#               PRINT RECORDS
#-----------------------------------------
def print_leaderboard():
    f = open("player.txt",'r')
    print(f"Player       Points")

    for line in f:
         player,points = line.split('|')

         print("{:<13}{:<20}".format(player,int(points)))
    print()
    
    f.close()

#-----------------------------------------
#               Save game
#-----------------------------------------
        
def save_game():
    path = ""  # Can be modified if needed
    
    try:
        file = open(path + "Save_Data.txt", "w")

        for row in range(len(field)):  # Runs by the number of rows in the field
            for column in range(len(field[row])):  # Runs by the number of columns in the field
                tile_value = field[row][column]
                file.write(str(tile_value) if tile_value is not None else "None")  # Write tile value into file
                if column != len(field[row]) - 1:  # Checks if column is not the last index
                    file.write(",")  # Separates values by a comma
            file.write("\n")  
    
        file.write(f"{player.coins},{player.points}\n")

        print("\nGame saved successfully!\n")
    
    except Exception as e:
        print(f"Error saving game: {e}")

    file.close()

#-----------------------------------------
#               Load game
#-----------------------------------------
    
def load_game():
    path = ""  # Can be modified if needed
    try:
        with open(path + "Save_Data.txt", "r") as file:
            # Read the field data
            for row in range(len(field)):
                line = file.readline().strip().split(',')
                for column in range(len(field[row])):
                    field[row][column] = None if line[column] == 'None' else line[column]

            # Read player data
            player_data = file.readline().strip().split(',')
            player.coins = int(player_data[0])
            player.points = int(player_data[1])

            print("\nGame loaded successfully!\n")
            return True  # Return True to indicate successful loading
        
    except FileNotFoundError:
        print("\nNo saved game found.\n")
        return False  # Return False to indicate no saved game found

    except Exception as e:
        print(f"\nError loading game: {e}\n")
        return False  # Return False for other loading errors
    
#-----------------------------------------
#               End Game
#-----------------------------------------
def check_game_over(player, field):
    # Check if the game is over (no more coins or board filled)
    if player.coins <= 0 or is_field_filled(field):
        # Print multiple blank lines to "clear" the terminal
        print('\n' * 30)


        print("  /$$$$$$   /$$$$$$  /$$      /$$ /$$$$$$$$        /$$$$$$  /$$    /$$ /$$$$$$$$ /$$$$$$$ ")
        print(" /$$__  $$ /$$__  $$| $$$    /$$$| $$_____/       /$$__  $$| $$   | $$| $$_____/| $$__  $$")
        print("| $$  \\__/| $$  \\ $$| $$$$  /$$$$| $$            | $$  \\ $$| $$   | $$| $$      | $$  \\ $$")
        print("| $$ /$$$$| $$$$$$$$| $$ $$/$$ $$| $$$$$         | $$  | $$|  $$ / $$/| $$$$$   | $$$$$$$/")
        print("| $$|_  $$| $$__  $$| $$  $$$| $$| $$__/         | $$  | $$ \\  $$ $$/ | $$__/   | $$__  $$")
        print("| $$  \\ $$| $$  | $$| $$\\  $ | $$| $$            | $$  | $$  \\  $$$/  | $$      | $$  \\ $$")
        print("|  $$$$$$/| $$  | $$| $$ \\/  | $$| $$$$$$$$      |  $$$$$$/   \\  $/   | $$$$$$$$| $$  | $$")
        print(" \\______/ |__/  |__/|__/     |__/|________/       \\______/     \\_/    |________/|__/  |__/")

        update_leaderboard(player)
        
        print()
        print(f"Your Score is: {player.points}")

        print('\n'*2)
        print("---------------------------------------------------------------------------------------------------")
        return True
    else:
        return False

def is_field_filled(field):
    for row in field:
        for element in row:
            if element is None:
                return False
    return True


#-----------------------------------------
#          Return to main menu
#-----------------------------------------
# def return_to_main_menu():
#     print("\nReturning to the main menu...")
#     main_gameplay()


#-----------------------------------------
#               MAIN GAME
#-----------------------------------------
def main_gameplay():

    while True:
        print("\nNgee Ann City")
        print("-------------------")
        print("Build the happiest and most prosperous city!")
        print()
        show_main_menu()
        choice = get_main_choice()
        if choice == '1':
            initialize_game()
            game_menu()
                
        elif choice == '2':
            boolean_check = load_game()
            if boolean_check:
                game_menu()

        elif choice == '3':
            print_leaderboard()

        elif choice == '4':
            print("\nThank you for playing!")
            break

main_gameplay()

