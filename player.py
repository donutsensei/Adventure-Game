class Player:

    def __init__(self, x, y):
        '''
        Creates a new Player.
        :param x: x-coordinate of position on map
        :param y: y-coordinate of position on map
        :return:

        This is a suggested starter class for Player.
        You may add new parameters / attributes / methods to this class as you see fit.
        Consider every method in this Player class as a "suggested method":
                -- Suggested Method (You may remove/modify/rename these as you like) --
        '''
        self.x = x
        self.y = y
        self.inventory = []
        self.victory = False

    def move(self, dx, dy):
        '''
        Given integers dx and dy, move player to new location (self.x + dx, self.y + dy)
        :param dx:
        :param dy:
        :return:
        '''
        self.x = self.x + dx
        self.y = self.y + dy
        pass

    def move_north(self):
        '''These integer directions are based on how the map must be stored
        in our nested list World.map'''
        self.move(0,-1)

    def move_south(self):
        self.move(0,1)

    def move_east(self):
        self.move(1,0)

    def move_west(self):
        self.move(-1,0)

    def add_item(self, item):
        '''
        Add item to inventory.
        :param item:
        :return:
        '''

        self.inventory.append(item)



    def remove_item(self, item):
        '''
        Remove item from inventory.
        :param item:
        :return:
        '''

        self.inventory.remove(item)



    def get_inventory(self):
        '''
        Return inventory.
        :return:
        '''

        return self.inventory

'''
def test():
    player = Player(0, 0)
    print(player.x == 0) # prints True
    print(player.y == 0) # prints True
    player.move(3, -4)
    print(player.x == 3) # prints True
    print(player.y == -4) # prints True
    player.move(-1, 2)
    print(player.x == 2) # prints True
    print(player.y == -2) # prints True
    print(player.y == 3)
    print (player.x)
    player.move_east()
    print(player.x)
    player.move_west()
    player.move_west()
    player.move_west()
    print (player.x)
    player.move_west()
    print (player.x)

    Player.add_item(player, "hi")
    print (player.inventory)

test()
'''