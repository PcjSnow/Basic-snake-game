import readchar
import random
from colors import styled_print, reset_colors, colors, styles

POS_X = 0
POS_Y = 1

MAP_WIDTH = 20 #columns
MAP_HEIGHT = 15 #rows



#Draw map

def draw_map(width: int, heigth: int, player_pos: list, map_objects: list, tail_length: list, tail: list):

    ded = False #This variable represents whether we have colisioned with our own tail (and therefore we lost the game) or not
    print("+" + "-" * (width * 3) + "+")

    for coordinate_y in range(heigth): # Move in Y coordinates

        print("|", end="")

        for coordinate_x in range(width): # For each Y coordinate, move in all X coordinates
            
            object_in_cell = None # Variable to store an object (food) found in map. Each iteration resets it to None

            char_to_draw = " " # In general, we draw each cell with a blank space unless there is something in the cell (player or objects)
            
            for map_object in map_objects: #Check every single object in the map

                if coordinate_x == map_object[POS_X] and coordinate_y == map_object[POS_Y]: #Draw object position with *

                    char_to_draw = "*"
                    styled_print(styles["bold"], colors["red"])
                    object_in_cell = map_object # If we happen to stumble upon an object, we store it in the object_in_cell variable

            # Tail management       
            tail = tail[:tail_length[0]] #We only want to draw <tail_length> tails.
            for tails in tail: #Draw tails
                if coordinate_x == tails[POS_X] and coordinate_y == tails[POS_Y]:

                    char_to_draw = "@"

                    styled_print(styles["bold"], colors["green"])
            
            if coordinate_x == player_pos[POS_X] and coordinate_y == player_pos[POS_Y]: #Draw player position with @

                char_to_draw = "@"

                styled_print(styles["bold"], colors["green"])

                for tails in tail: # Let's check if the player position is the same as one of the tails
                    if coordinate_x == tails[POS_X] and coordinate_y == tails[POS_Y]:
                        ded = True #If that's the case, then we lost the game

                if object_in_cell: #If we pass through a cell that also contains a map object, then delete the map object and increase tail length (eat snek food)

                    tail_length[0] += 1

                    map_objects.remove(object_in_cell)
                    new_object_position = [random.randint(0, MAP_WIDTH-1), random.randint(0, MAP_HEIGHT-1)] #Generate new food once we have eaten it
                    if new_object_position not in map_objects and new_object_position != object_in_cell:
                        map_objects.append(new_object_position)
            
            print(" {} ".format(char_to_draw), end="")
            reset_colors()
        print("|")

    print("+" + "-" * (width * 3) + "+")
    return ded # Return whether we are alive or not



# Ask player where he wants to move

def ask_direction(player_pos: list, tail_length: list, tail: list):
    #direction = input("¿Dónde te quieres mover? [WASD] ([Q] to exit): ") Clunky way of doing it: requires the player to press Return after each input
    direction = readchar.readchar()
    if direction == "w":
        tail.insert(0, player_pos.copy()) # In each movement we store our last position in the head of the tail (LIFO policy)
        tail = tail[:tail_length[0]]
        player_pos[POS_Y] = (player_pos[POS_Y] - 1) % MAP_HEIGHT # We use modulo to ensure that we are always inside the map

    elif direction == "a":
        tail.insert(0, player_pos.copy())
        tail = tail[:tail_length[0]]
        player_pos[POS_X] = (player_pos[POS_X] - 1) % MAP_WIDTH

    elif direction == "s":
        tail.insert(0, player_pos.copy())
        tail = tail[:tail_length[0]]
        player_pos[POS_Y] = (player_pos[POS_Y] + 1) % MAP_HEIGHT

    elif direction == "d":
        tail.insert(0, player_pos.copy())
        tail = tail[:tail_length[0]]
        player_pos[POS_X] = (player_pos[POS_X] + 1) % MAP_WIDTH

    else:
        styled_print(styles["bold"], colors["green"])
        print("Thanks for playing!")
        reset_colors()
    
    return direction



# Randomly generate map objects' coordinates (i.e. randomly generate snek food)

def generate_objects(map_objects: list, player_pos: list):
    amount = int(input("Cuántos objetos deseas generar?: "))

    while len(map_objects) < amount:
        new_object_position = [random.randint(0, MAP_WIDTH-1), random.randint(0, MAP_HEIGHT-1)]

        if new_object_position not in map_objects and new_object_position != player_pos:
            map_objects.append(new_object_position)