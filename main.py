def wins(array):
    empty_array = []
    for arr in array:
        is_empty = " " in arr
        empty_array.append(is_empty)
    is_empty = any(empty_array)
    if (array[0][0]!= " ") and (array[0][0] == array[0][1]) and (array[0][1] == array[0][2]):
        print(array[0][0] + " " + "wins")
        return True
    elif (array[1][0] != " ") and (array[1][0] == array[1][1]) and (array[1][1] == array[1][2]):
        print(array[1][0] + " " + "wins")
        return True
    elif (array[2][0] != " ") and (array[2][0] == array[2][1]) and (array[2][1] == array[2][2]):
        print(array[2][0] + " " + "wins")
        return True
    elif (array[0][0] != " ") and (array[0][0] == array[1][0]) and (array[1][0] == array[2][0]):
        print(array[0][0] + " " + "wins")
        return True
    elif (array[0][1] != " ") and (array[0][1] == array[1][1]) and (array[1][1] == array[2][1]):
        print(array[0][1] + " " + "wins")
        return True
    elif (array[0][2] != " ") and (array[0][2] == array[1][2]) and (array[1][2] == array[2][2]):
        print(array[0][2] + " " + "wins")
        return True
    elif (array[0][0] != " ") and (array[0][0] == array[1][1]) and (array[1][1] == array[2][2]):
        print(array[0][0] + " " + "wins")
        return True
    elif (array[0][2] != " ") and (array[0][2] == array[1][1]) and (array[1][1] == array[2][0]):
        print(array[0][2] + " " + "wins")
        return True
    elif not is_empty:
        print("Draw")
        return True
    elif is_empty:
        # print("Game not finished")
        return False


def impossible(array):
    x_count = 0
    o_count = 0
    wins_count = 0
    for i in array:
        if i == "X":
            x_count += 1
        elif i == "O":
            o_count += 1
    if (array[0][0] != " ") and (array[0][0] == array[0][1]) and (array[0][1] == array[0][2]):
        wins_count += 1
    if (array[1][0] != " ") and (array[1][0] == array[1][1]) and (array[1][1] == array[1][2]):
        wins_count += 1
    if (array[2][0] != " ") and (array[2][0] == array[2][1]) and (array[2][1] == array[2][2]):
        wins_count += 1
    if (array[0][0] != " ") and (array[0][0] == array[1][0]) and (array[1][0] == array[2][0]):
        wins_count += 1
    if (array[0][1] != " ") and (array[0][1] == array[1][1]) and (array[1][1] == array[2][1]):
        wins_count += 1
    if (array[0][2] != " ") and (array[0][2] == array[1][2]) and (array[1][2] == array[2][2]):
        wins_count += 1
    if x_count - o_count >= 2 or o_count - x_count >= 2:
        print("Impossible")
        return True
    elif wins_count > 1:
        print("Impossible")
        return True
    else:
        return False


def printer(grid):
    print("---------")
    print("| " + grid[0][0] + " " + grid[0][1] + " " + grid[0][2] + " |")
    print("| " + grid[1][0] + " " + grid[1][1] + " " + grid[1][2] + " |")
    print("| " + grid[2][0] + " " + grid[2][1] + " " + grid[2][2] + " |")
    print("---------")


def user_coordinates(letter):
    user_input = input("Enter the coordinates: ").split(" ")
    if user_input[0].isnumeric() and user_input[1].isnumeric():
        temp_nums = [int(x) for x in user_input]
        if 1 <= temp_nums[0] <= 3 and 1 <= temp_nums[1] <= 3:
            coordinates = [int(x) - 1 for x in user_input]
            if grid[coordinates[0]][coordinates[1]] != " ":
                print("This cell is occupied! Choose another one!")
                user_coordinates(letter)
            else:
                grid[coordinates[0]][coordinates[1]] = letter
                printer(grid)
        elif (temp_nums[0] < 1 or temp_nums[0] > 3) or (temp_nums[1] < 1 or temp_nums[1] > 3):
            print("Coordinates should be from 1 to 3!")
            user_coordinates(letter)
    else:
        print("You should enter numbers!")
        user_coordinates(letter)


grid = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
printer(grid)

for i in range(1, 10):
    letter = ""
    if i % 2 != 0:
        letter = "X"
    else:
        letter = "O"
    user_coordinates(letter)
    isImpossible = impossible(grid)
    isVictory = wins(grid)
    if isVictory:
        break
    elif isImpossible:
        break
