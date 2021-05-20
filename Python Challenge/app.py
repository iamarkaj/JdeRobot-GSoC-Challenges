#!/usr/bin/env python3

"""
Wrapper
"""

from game import game
g = game()


patterns = {1:g.random, 2: g.beehive, 3: g.beacon, 4: g.glider, 5: g.LWSS, 6: g.glidergun}


print("\n\nEnter the maximum number of iterations (e.g. 200)")
max_iterations = int(input("Enter: "))


print("\n\nEnter a number corresponding to the required pattern (1-7)")
print("1. Random\n2. Bee-hive\n3. Beacon\n4. Glider\n5. Light-weight spaceship\n6. Glider gun")
choose = int(input("Enter: "))


print("\n\nEnter position x of the pattern (e.g. 0)")
pos_x = int(input("Enter: "))
print("\n\nEnter position y of the pattern (e.g. 0)")
pos_y = int(input("Enter: "))
print("\n\n")

g.add_pattern(patterns[choose], pos_x, pos_y)


for i in range(max_iterations):
	g.main()


g.move_cursor_down()
print("Thank you.")