class Location:

    def __init__(self,library,study_room,outside,visit):
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
        self.library = library
        self.study_room = study_room
        self.outside = outside
        self.visit=visit

    def get_brief_description (self):
        '''Return str brief description of location.'''

        if self.library == "LOCATION 1":
           return ("You are on the first floor of the UTM Library.")
        elif self.study_room == "LOCATION 2":
           return ("You are in the study room, which is completely empty.")
        elif self.outside == "LOCATION 3":
           return ("You are outside of the library. ")
        else:
           return ("That way is blocked.")
    def get_full_description (self):
        '''Return str long description of location.'''
        if self.visit == 0:
           if self.library == "LOCATION 1":
               return ("You are on the first floor of the UTM Library. There is an empty study room to the South, an exit from the library to the North.You are on the first floor of the UTM Library. It's usually crowded at this time of the day, but today it's eerily quiet.Only a few students are studying inside one of the study rooms. You better not disturb them. A librarian stands near the service desk, looking bored and sleepy. There is an empty study room to the South, an exit from the library to the North.")
           elif self.study_room == "LOCATION 2":
               return ("This study room is completely empty.You are in an empty study room. And by empty, we mean, absolutely empty. All the tables and chairs have been taken out,the whiteboards taken off the wall, not even the carpeting is left. Are they planning to do something else with this space?")
           elif self.outside == "LOCATION 3":
               return ("You are outside of the library. There is a Starbucks to the North. You are outside of the library in a crowded hallway. There is a smell of coffee in the air. There is a Starbucks to the North.")
           else:
               return ("That way is blocked.")

    def available_actions(self):
        '''
        -- Suggested Method (You may remove/modify/rename this as you like) --
        Return list of the available actions in this location.
        The list of actions should depend on the items available in the location
        and the x,y position of this location on the world map.'''
        pass

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
        THIS FUNCTION MUST NOT BE RENAMED OR REMOVED.
        Store map from filename (map.txt) in the variable "self.map" as a nested list of strings OR integers like so:
            1 2 5
            3 -1 4
        becomes [['1','2','5'], ['3','-1','4']] OR [[1,2,5], [3,-1,4]]
        RETURN THIS NEW NESTED LIST.
        :param filename: map.txt
        :return: return nested list of strings/integers representing map of game world as specified above
        '''

        mapFile = open("map.txt", "r+")
        self.map = []
        for line in mapFile:

            splitLine = line.split("\n")
            splitLine2 = splitLine[0].split(" ")
            self.map.append(splitLine2)

        return (map)


    def load_locations(self, filename):
        '''
        Store all locations from filename (locations.txt) into the variable "self.locations"
        however you think is best.
        Remember to keep track of the integer number representing each location.
        Make sure the Location class is used to represent each location.
        Change this docstring as needed.
        :param filename: location.txt
        :return: self.locations
        '''
        filename = open ("location.txt","r")

        while True:
            line = filename.readline()
            if len (line)==0:
                break
            self.location =line
            print (self.location,end="")
        filename.close()


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
            print (self.items,end="")
        filename.close()

    def get_location(self, x, y):
        '''Check if location exists at location (x,y) in world map.
        Return Location object associated with this location if it does. Else, return None.
        Remember, locations represented by the number -1 on the map should return None.
        :param x: integer x representing x-coordinate of world map
        :param y: integer y representing y-coordinate of world map
        :return: Return Location object associated with this location if it does. Else, return None.
        '''

