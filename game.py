import string

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
                print(f'| {name}', end='')  # Print the name of the entity

        print(' |')  # End the row with the right border

    print('    +-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+')

print_field(field)






