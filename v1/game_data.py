"""CSC111 Project 1: Text Adventure Game Classes

Instructions (READ THIS FIRST!)
===============================

This Python module contains the main classes for Project 1, to be imported and used by
 the `adventure` module.
 Please consult the project handout for instructions and details.

Copyright and Usage Information
===============================

This file is provided solely for the personal and private use of students
taking CSC111 at the University of Toronto St. George campus. All forms of
distribution of this code, whether as given or with any changes, are
expressly prohibited. For more information on copyright for CSC111 materials,
please consult our Course Syllabus.

This file is Copyright (c) 2024 CSC111 Teaching Team
"""
from typing import Optional, TextIO


class Item:
    """An item in our text adventure game world.

    Instance Attributes:
        - self.name: the item's name
        - self.start_position: the position the item is initially at
        - self.target_position: the position the item should be deposited to
        - self.target_points: the points the item gives for obtaining and depositing it

    Representation Invariants:
        - self.name != ''
        - -1 <= self.curr_position <= 18
        - 0 <= self.start_position <= 18
        - 0 <= self.target_position <= 18
        - self.target_points > 0
    """
    name: str
    curr_position: int
    start_position: int
    target_position: int
    target_points: int

    def __init__(self, name: str, curr: int, start: int, target: int, target_points: int) -> None:
        """Initialize a new item.
        """
        self.name = name
        self.curr_position = curr
        self.start_position = start
        self.target_position = target
        self.target_points = target_points


class Location:
    """A location in our text adventure game world.

    Instance Attributes:
        - name: the name of the location
        - pos: represents the position of the player
        - brief: gives a brief description of the location if the player has already visited
        - long: gives a long description of the location if the player hasn't already visited
        - commands: gives a list of possible commands at the player's location
        - items: lists the item(s) located in the location
        - visited: states whether the player has already visited the location before

    Representation Invariants:
        - self.name != ''
        - self.pos > -1
        - self.brief != ''
        - self.long != ''
        - self.commands != []
    """
    name: str
    pos: int
    brief: str
    long: str
    commands: list[str]
    items: list[Item]
    visited: bool

    def __init__(self, name: str, pos: int, brief: str, long: str, items: list[Item],
                 visited: bool) -> None:
        """Initialize a new location.
        """
        self.name = name
        self.pos = pos
        self.brief = brief
        self.long = long
        # self.commands = self.available_actions()
        self.items = items
        self.visited = visited

    def available_actions(self) -> list[str]:
        """
        Return the available actions in this location.
        The actions should depend on the items available in the location
        and the x,y position of this location on the world map.
        """
        if self.pos == 0:
            return ['west', 'grab', 'drop']
        if self.pos == 1:
            return ['east', 'west', 'grab', 'drop']
        if self.pos == 2:
            return ['north', 'east', 'grab', 'drop']
        if self.pos == 3:
            return ['north', 'south', 'grab', 'drop']
        if self.pos == 4:
            return ['north', 'south', 'grab', 'drop']
        if self.pos == 5:
            return ['north', 'south', 'east', 'west', 'grab', 'drop']
        if self.pos == 6:
            return ['west', 'grab', 'drop']
        if self.pos == 7:
            return ['east', 'grab', 'drop']
        if self.pos == 8:
            return ['north', 'south', 'grab', 'drop']
        if self.pos == 9:
            return ['north', 'south', 'grab', 'drop']
        if self.pos == 10:
            return ['north', 'south', 'east', 'west', 'grab', 'drop']
        if self.pos == 11:
            return ['east', 'west', 'grab', 'drop']
        if self.pos == 12:
            return ['west', 'grab', 'drop']
        if self.pos == 13:
            return ['north', 'east', 'grab', 'drop']
        if self.pos == 14:
            return ['south', 'east', 'grab', 'drop']
        if self.pos == 15:
            return ['north', 'south', 'west', 'grab', 'drop']
        if self.pos == 16:
            return ['north', 'south', 'grab', 'drop']
        if self.pos == 17:
            return ['south', 'east', 'grab', 'drop']
        if self.pos == 18:
            return ['west', 'grab', 'drop']
        else:
            return []


class Player:
    """
    A Player in the text advanture game.

    Instance Attributes:
        - self.x: the player's position on the x-axis
        - self.y: the player's on the y-axis
        - self.inventory: items that the player is holding
        - self.victory: indicates if the player has won

    Representation Invariants:
        - 0 <= self.x <= 18
        - 0 <= self.y <= 18
    """
    x: int
    y: int
    inventory: list[str]
    victory: bool
    score: int
    quit: bool

    def __init__(self, x: int, y: int) -> None:
        """
        Initializes a new Player at position (x, y).
        """
        self.x = x
        self.y = y
        self.inventory = []
        self.victory = False
        self.score = 0
        self.quit = False


class World:
    """A text adventure game world storing all location, item and map data.

    Instance Attributes:
        - map: a nested list representation of this world's map using numbers from -1 to 18
        - location: the location data for the world, including the locations's name, descriptions, and points allotted
        - items: a list of items, the location they are found and deposited it, and the points they give

    Representation Invariants:
        - self.map != [[]]
        - self.location != [[]]
        - self.items != [[]]
    """
    map: TextIO
    location: TextIO
    items: TextIO

    def __init__(self, map_data: TextIO, location_data: TextIO, items_data: TextIO) -> None:
        """
        Initialize a new World for a text adventure game, based on the data in the given open files.

        - location_data: name of text file containing location data (format left up to you)
        - items_data: name of text file containing item data (format left up to you)
        """
        self.map = self.load_map(map_data)
        self.location = self.load_locations(location_data)
        self.items = self.load_items(items_data)

    def load_map(self, map_data: TextIO) -> list[list[int]]:
        """
        Store map from open file map_data as the map attribute of this object, as a nested list of integers like so:

        If map_data is a file containing the following text:
            1 2 5
            3 -1 4
        then load_map should assign this World object's map to be [[1, 2, 5], [3, -1, 4]].

        Return this list representation of the map.
        """
        temp = []
        with open(map_data) as file:
            for line in file:
                line = line.strip()
                temp.append(line.split(" "))
            map_list = [[int(i) for i in lst] for lst in temp]
            return map_list

    def load_locations(self, location_data: TextIO) -> list[list]:
        """
        Store locations from open file location_data as the location attribute of this object, as a nested list of:
        - Strings (location name and descriptions)
        - Integers (location number)
        - Lists of Strings (available commands in the location)
        - Booleans (if the location has been visited)

        Return this list representation of the locations.
        """
        ret_locations = []
        temp_one_list = []
        temp_two_list = []
        locations_list = []
        with open(location_data) as file:
            file_data = file.read()
            lines = file_data.split('END')
            for x in range(0, len(lines)):
                temp_one_list.append(lines[x].split('\n'))
                temp_two_list.append(list(filter(None, temp_one_list[x])))
            temp_two_list.pop()
            for i in temp_two_list:
                temp_three_list = []
                temp_str = ''
                for j in range(0, 3):
                    temp_three_list.append(i[j])
                for k in range(3, len(i)):
                    temp_str += i[k]
                temp_three_list.append(temp_str)
                locations_list.append(temp_three_list)
            for a in locations_list:
                a[1] = int(a[1])
            nums = len(locations_list) - 1
            for b in range(0, nums):
                ret_locations.append(
                    Location(locations_list[b][0], b, locations_list[b][2], locations_list[b][3], [], False))
            ret_locations.append(
                Location(locations_list[nums][0], -1, locations_list[nums][2], locations_list[nums][3], [], False))
            return ret_locations

    def load_items(self, items_data: TextIO) -> list[list[int]]:
        """
        Store items from open file items_data as the item attribute of this object, as a nested list of:
        - Strings (item name)
        - Integers (item grab location, item drop location, and points gained for dropping the item off)

        Return this list representation of the items.
        """
        ret_items = []
        items_list = []
        with open(items_data) as file:
            for line in file:
                temp_two_list = []
                temp_str = ''
                line = line.strip()
                temp_one_list = line.split(" ")
                for i in range(0, 3):
                    temp_two_list.append(int(temp_one_list[i]))
                for j in range(3, len(temp_one_list)):
                    temp_str += temp_one_list[j] + ' '
                temp_str = temp_str[0:len(temp_str) - 1]
                temp_two_list.append(temp_str)
                items_list.append(temp_two_list)
            for item_data in items_list:
                ret_items.append(Item(item_data[3], item_data[0], item_data[0], item_data[1], item_data[2]))
            return ret_items

    def get_location(self, x: int, y: int) -> Optional[Location]:
        """Return Location object associated with the coordinates (x, y) in the world map, if a valid location exists at
         that position. Otherwise, return None. (Remember, locations represented by the number -1 on the map should
         return None.)
        """
        map_data = self.map
        locations_data = self.location
        pos = map_data[y][x]

        if pos == -1:
            return None
        else:
            for location in locations_data:
                if pos == location.pos:
                    return location
            return None


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
    import python_ta

    python_ta.check_all(config={
        'max-line-length': 300,
        'extra-imports': ['hashlib']
    })
