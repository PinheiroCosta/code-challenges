#!/usr/bin/python

# width and height of the building
width, height = [int(i) for i in input().split()]
turns = int(input())  # maximum number of turns before game over.
batman_x, batman_y = [int(i) for i in input().split()]
lowest_x, lowest_y, highest_x, highest_y = [0, 0, width, height]

# game loop
while True:
    bomb_dir = input()  # the direction of the bombs from batman's current location (U, UR, R, DR, D, DL, L or UL)

    if "D" in bomb_dir:
        lowest_y = batman_y + 1

    elif "U" in bomb_dir:
        highest_y = batman_y - 1
    
    if "L" in bomb_dir:
        highest_x = batman_x - 1
    
    elif "R" in bomb_dir:
        lowest_x = batman_x + 1

    batman_y = (highest_y + lowest_y) // 2
    batman_x = (highest_x + lowest_x) // 2

    # the location of the next window Batman should jump to.
    print(batman_x, batman_y)
    
