"""CSC111 Project 1: Text Adventure Game

Instructions (READ THIS FIRST!)
===============================

This Python module contains the code for Project 1. Please consult
the project handout for instructions and details.

Copyright and Usage Information
===============================

This file is provided solely for the personal and private use of students
taking CSC111 at the University of Toronto St. George campus. All forms of
distribution of this code, whether as given or with any changes, are
expressly prohibited. For more information on copyright for CSC111 materials,
please consult our Course Syllabus.

This file is Copyright (c) 2024 CSC111 Teaching Team
"""

# Note: You may add in other import statements here as needed
from game_data import World, Item, Location, Player

# Note: You may add helper functions, classes, etc. here as needed
places = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0, 11: 0, 12: 0, 13: 0, 14: 0, 15: 0, 16: 0, 17: 0, 18: 0}

def do_action(w: World, p: Player, location: Location, choice: str) -> None:
    if choice in location.available_actions():
        if choice == 'north':
            p.y -= 1
        if choice == 'south':
            p.y += 1
        if choice == 'west':
            p.x -= 1
        if choice == 'east':
            p.x += 1
    else:
        print('This way is blocked.')


# COLORS
def black(skk):
    print("\033[30m {}\033[00m" .format(skk))

def darkRed(skk):
    print("\033[31m {}\033[00m" .format(skk))

def darkGreen(skk):
    print("\033[32m {}\033[00m" .format(skk))

def darkYellow(skk):
    print("\033[33m {}\033[00m" .format(skk))

def darkBlue(skk):
    print("\033[34m {}\033[00m" .format(skk))

def darkMagenta(skk):
    print("\033[35m {}\033[00m" .format(skk))

def darkCyan(skk):
    print("\033[36m {}\033[00m" .format(skk))

def lightGray(skk):
    print("\033[37m {}\033[00m" .format(skk))

def darkGray(skk):
    print("\033[90m {}\033[00m" .format(skk))

def red(skk):
    print("\033[91m {}\033[00m" .format(skk))
    # \u001b[38;2;180;180;180m

def green(skk):
    print("\033[92m {}\033[00m" .format(skk))

def yellow(skk):
    print("\033[93m {}\033[00m" .format(skk))

def blue(skk):
    print("\033[94m {}\033[00m" .format(skk))

def magenta(skk):
    print("\033[95m {}\033[00m" .format(skk))

def cyan(skk):
    print("\033[96m {}\033[00m" .format(skk))

def white(skk):
    print("\033[97m {}\033[00m" .format(skk))

black("This is black.")
darkRed("This is dark red.")
darkGreen("This is dark green.")
darkYellow("This is dark yellow.")
darkBlue("This is dark blue.")
darkMagenta("This is dark magenta.")
darkCyan("This is dark cyan.")
lightGray("This is light gray.")
darkGray("This is dark gray.")
red("This is red.")
green("This is green.")
yellow("This is yellow.")
blue("This is blue.")
magenta("This is magenta.")
cyan("This is cyan.")
white("This is white.")
print("\n")

# Note: You may modify the code below as needed; the following starter template are just suggestions
if __name__ == "__main__":
    w = World("map.txt", "locations.txt", "items.txt")
    p = Player(2, 7)  # set starting location of player; you may change the x, y coordinates here as appropriate

    menu = ["look", "inventory", "score", "quit", "grab", "drop"] # TODO: Implement BACK if we have time

    location = w.get_location(p.x, p.y)
    moves = 0

    while not p.victory and not p.quit and moves < 40: # decide the number of moves later
        location = w.get_location(p.x, p.y)
        loc = location.pos
        
        if places[loc] > 0:
            location.visited = True
        places[loc] += 1
        
        print(location.name)
        if location.visited == True:
            print(location.brief)
        else:
            print(location.long)

        print("What to do? \n")
        print("[menu]")
        print("north\nsouth\nwest\neast")
        choice = input("\nEnter action: ")

        if choice == "[menu]":
            print("Menu Options: \n")
            for option in menu:
                print(option)
            choice = input("\nChoose action: ")
        
        if choice == "north" or choice == "south" or choice == "east" or choice == "west":
            do_action(w, p, location, choice)
        
        if choice == "look":
            print(location.long + '\n') #TODO: don't print the brief
        
        if choice == "inventory":
            if p.inventory == []:
                print("You have nothing in your bag.\n")
            else:
                print("Inventory:")
                for item in p.inventory:
                    print("- " + str(item))

        if choice == "score":
            print("Score: " + str(p.score) + "\n")

        if choice == "quit":
            p.quit = True

        if choice == "grab":
            all_items = w.items
            curr_location = w.get_location(p.x, p.y)
            curr_items = []
            
            for item_info in all_items:
                if item_info.curr_position == curr_location.pos:
                    curr_items.append(item_info.name)

            if curr_items == [] or (w.items != [] and all([item.curr_position == -1 for item in w.items])):
                print("There are no items in this area!\n")
            else:
                print("Items:")
                for item in curr_items:
                    print("- " + item)
            
                print("Which item do you want to grab?")
                choice = input("\nChoose item: ")
                temp_items = []
                
                for item in curr_items:
                    temp_items.append(item.lower())

                if choice.lower() in temp_items:
                    chosen_item = choice.title()
                    p.inventory.append(chosen_item)
                    for item in w.items:
                        if chosen_item == item.name:
                            item.curr_position = -1
                else:
                    print("This item does not exist in this area.")
    
        if choice == "drop":
            all_items = p.inventory
            curr_location = w.get_location(p.x, p.y)
            curr_items = []

            for item_info in all_items:
                curr_items.append(item_info)

            if all_items == []:
                print("You have no items to drop!\n")
            else:
                print("Inventory:")
                for item in all_items:
                    print("- " + str(item))
            
                print("Which item do you want to drop?")
                choice = input("\nChoose item: ")
                temp_items = []
                
                for item in curr_items:
                    temp_items.append(item.lower())

                if choice.lower() in temp_items:
                    chosen_item = choice.title()
                    p.inventory.remove(chosen_item)
                    for item in w.items:
                        if chosen_item == item.name:
                            item.curr_position = curr_location.pos
                else:
                    print("You don't have this item.")
       
        if choice in ['north', 'south', 'east', 'west', 'grab', 'drop', 'look']:
            moves += 1

    if p.quit:
        print("You have successfully quit the game!")

    if p.victory:
        print("Congrats! You won!")

    if moves >= 25:
        print("You've reached the maximum number of moves. Game over.")

        # TODO: CALL A FUNCTION HERE TO HANDLE WHAT HAPPENS UPON THE PLAYER'S CHOICE
        #  REMEMBER: the location = w.get_location(p.x, p.y) at the top of this loop will update the location if
        #  the choice the player made was just a movement, so only updating player's position is enough to change the
        #  location to the next appropriate location
        #  Possibilities:
        #  A helper function such as do_action(w, p, location, choice)
        #  OR A method in World class w.do_action(p, location, choice)
        #  OR Check what type of action it is, then modify only player or location accordingly
        #  OR Method in Player class for move or updating inventory
        #  OR Method in Location class for updating location item info, or other location data etc....
