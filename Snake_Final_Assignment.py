#Playing Snake as the old Nokias, also setting some characteristics of the grid


def draw_map_tuples(coordinates: list, sweets: list, x: int, y: int) -> None:
    """ Here we are printing the grid of dimensions "x" x "y", we add the sweets and then the instructions from coordinates to place the snake. """
    for i in range(x):
        for j in range(y):
            if (i , j) in sweets:
                print("o", end=" ")
            elif (i , j) in coordinates:
                print("x", end=" ")
            else:
                print(".", end=" ")
        print()

def normal_movement(coordinates:list, coordinate: tuple) -> None:
    """ Here we are defining the normal movement of the snake, when the snake does not eat. Will be called later in movement."""
    coordinates.append(coordinate)
    coordinates.pop(0)

def eat_movement(coordinates:list, coordinate: tuple) -> None:
    """ Here we are defining the movement of the snake when eating. Will be called later in movement."""
    coordinates.append(coordinate)

def movement(coordinates: list, direction: str, sweets: list) -> None: 
    """ Here we are changing the original list of coordinates with the new movement which can take 4 forms: e/w/n/s. If the snake eats the fruit it will grow, otherwise keep the size as original."""
    #Warning: side effects here because of changes we do to coordinates.
    result = coordinates[-1]
    coordinate_east = (result[0], result[1] + 1)
    coordinate_south = (result[0] + 1, result[1])
    coordinate_west = (result[0], result[1] - 1)
    coordinate_north = (result[0] - 1, result[1])

    if direction == "e" and (result[1] + 1 < 10 ) and (coordinate_east not in coordinates):
        if coordinate_east in sweets:
            eat_movement(coordinates, coordinate_east)
            sweets.remove(coordinate_east)
        else:
            normal_movement(coordinates, coordinate_east)
    elif direction == "s" and (result[0] + 1 < 10) and (coordinate_south not in coordinates):
        if coordinate_south in sweets:
            eat_movement(coordinates, coordinate_south)
            sweets.remove(coordinate_south)
        else:
            normal_movement(coordinates, coordinate_south)
    elif direction == "w" and (result[1] - 1  >= 0) and (coordinate_west  not in coordinates):
        if coordinate_west in sweets:
            eat_movement(coordinates, coordinate_west)
            sweets.remove(coordinate_west)
        else:
            normal_movement(coordinates, coordinate_west)
    elif direction == "n" and (result[0] - 1 >= 0) and (coordinate_north not in coordinates) :
        if coordinate_north in sweets:
            eat_movement(coordinates, coordinate_north)
            sweets.remove(coordinate_north)
        else:
            normal_movement(coordinates, coordinate_north)
    else:
        print("Something went wrong here, please check. Insert one of the 4 available options or just hit end. ")
 
def main() -> None:
    x = int(input("What is the width of the map that you would like to have for the game? Please insert a an integer."))
    y = int(input("What is the height of the map that you would like to have for the game? Please insert a an integer."))
    
    coordinates = [(0, 0), (0, 1), (0, 2)] # Original coordinates of the snake. 
    sweets = [(3, 5)] # Coordinates of the sweets.
    print( f"Please write into which direction the snake should go."
        f"e for east, w for west, n for north, s for south. If you want to stop enter end.") 

    while (movement_request := input()) != "end":
        movement(coordinates, movement_request, sweets)
        draw_map_tuples(coordinates, sweets, x, y)

if __name__ == "__main__": 
    main()
