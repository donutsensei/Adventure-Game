class Location:

    def __init__(self,cct, studyroom, kaneff, lion, forest):
        '''Creates a new location.          
        ADD NEW ATTRIBUTES TO THIS CLASS HERE TO STORE DATA FOR EACH LOCATION.
        
        Data that could be associated with each Location object:
        a position in the world map,
        a brief description,
        a long description,
        a list of available commands/directions to move,
        items that are available in the location,
        and whether or not the location has been visited before.
        Store these as you see fit.

        This is just a suggested starter class for Location.
        You may change/add parameters and the data available for each Location class as you see fit.
  
        The only thing you must NOT change is the name of this class: Location.
        All locations in your game MUST be represented as an instance of this class.
        '''
        self.cct = cct
        self.studyroom = studyroom
        self.forest = forest
        self.kaneff = kaneff
        self.lion = lion

    def get_brief_description (self):
        '''Return str brief description of location.'''

        return get_brief_description



    def get_full_description (self):
        '''Return str long description of location.'''

        return None


class Item:

    def __init__ (self, name, start, target, target_points):
        '''Create item referred to by string name, with integer "start"
        being the integer identifying the item's starting location,
        the integer "target" being the item's target location, and
        integer target_points being the number of points player gets
        if item is deposited in target location.

        This is just a suggested starter class for Item.
        You may change these parameters and the data available for each Item class as you see fit.
        Consider every method in this Item class as a "suggested method":
                -- Suggested Method (You may remove/modify/rename these as you like) --

        The only thing you must NOT change is the name of this class: Item.
        All item objects in your game MUST be represented as an instance of this class.
        '''

        self.name = name
        self.start = start
        self.target = target
        self.target_points = target_points

    def get_starting_location (self):
        '''Return int location where item is first found.'''
        start=0
        for x in self.name:
            if self.name == ("T-card"):
                return (5)
            if self.name == ("Cheat sheet"):
                return (38)
            if self.name == ("Lucky pen"):
                return (24)

    def get_name(self):
        return (self.name)

    def get_target_location (self):
        '''Return item's int target location where it should be deposited.'''
        get_target_location = 21
        return (get_target_location)

    def get_target_points (self):
        '''Return int points awarded for depositing the item in its target location.'''
        target_points = 0
        for x in (0,4):
            if self.get_target_location == 21:
                target_points= target_points+5
        return target_points


class World:

    def __init__(self, mapdata, locdata, itemdata):
        '''
        Creates a new World object, with a map, and data about every location and item in this game world.

        You may ADD parameters/attributes/methods to this class as you see fit.
        BUT DO NOT RENAME OR REMOVE ANY EXISTING METHODS/ATTRIBUTES.

        :param mapdata: name of text file containing map data in grid format (integers represent each location, separated by space)
                        map text file MUST be in this format.
                        E.g.
                        1 -1 3
                        4 5 6
                        Where each number represents a different location, and -1 represents an invalid, inaccessible space.
        :param locdata: name of text file containing location data (format left up to you)
        :param itemdata: name of text file containing item data (format left up to you)
        :return:
        '''
        self.map = self.load_map(mapdata) # The map MUST be stored in a nested list as described in the docstring for load_map() below
        #self.locations ... You may choose how to store location and item data.
        self.load_locations(locdata) # This data must be stored somewhere. Up to you how you choose to do it...
        self.load_items(itemdata) # This data must be stored somewhere. Up to you how you choose to do it...



    def load_map(self, filename):
        '''
        Stores map from filename (map.txt) in the variable "self.map" as a nested list of strings OR integers like so:
            1 2 5
            3 -1 4
        becomes [['1','2','5'], ['3','-1','4']] OR [[1,2,5], [3,-1,4]]
        
        :param filename: map.txt
        :return: return nested list of strings/integers representing map of game world as specified above
        '''

        mapFile = open("map.txt", "r+")
        self.map = []
        for line in mapFile:

            splitLine = line.split("\n")
            splitLine2 = splitLine[0].split(" ")
            self.map.append(splitLine2)

        return (self.map)


    def load_locations(self, filename):
        '''
        Stores locations into a list/index.

        :param filename: location.txt
        :return: self.locations
        '''

        locationFile = open("location.txt", "r+")

        self.location = []
        for line in locationFile:

            splitLine = line.split("\n")
            splitLine2 = splitLine[0].split(":")
            self.location.append(splitLine2)

        return (self.location)


    def load_items(self, filename):
        '''
        Store all items from filename (items.txt) into ... whatever you think is best.
        Make sure the Item class is used to represent each item.
        Change this docstring accordingly.
        :param filename: items.txt
        :return: self.item
        '''
        filename = open ("items.txt","r")
        while True:
            line =filename.readline()
            if len (line)==0:
                break
            self.items=line
        filename.close()

    def get_location(self, x, y):
        '''corresponds map postion via arrays to location array, and prints description

        :param x: integer x representing x-coordinate of world map
        :param y: integer y representing y-coordinate of world map
        :return: Return Location object associated with this location if it does. Else, return None.
        '''

        if self.map[x][y] == '-1':
            return None

        else:
            position = self.map[x][y]
            for place in self.location:
                if place[0] == position:
                    return place[1]




