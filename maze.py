import os
from maze_functions import ask_direction, draw_map, generate_objects

POS_X = 0
POS_Y = 1

MAP_WIDTH = 20 #columns
MAP_HEIGHT = 15 #rows


def main():

    my_position = [3, 3] #Cartesian coordinates (x, y)
    map_objects = []
    tail_length = [0]
    tail = []
    generate_objects(map_objects, my_position)
    draw_map(MAP_WIDTH, MAP_HEIGHT, my_position, map_objects, tail_length, tail)
    ask_direction(my_position, tail_length, tail)

    os.system("clear") #Clear screen

    while True:
        if(draw_map(MAP_WIDTH, MAP_HEIGHT, my_position, map_objects, tail_length, tail)): #End the game because we died
            print("HAS MUERTO")
            break
        if ask_direction(my_position, tail_length, tail) == "q": #End the game because we quit
            break
        
        os.system("clear")
        
    
    
if __name__ == "__main__":
    main()

