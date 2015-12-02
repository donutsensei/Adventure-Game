from game_data import World, Item, Location
from player import Player

if __name__ == "__main__":
    WORLD = World("map.txt", "locations.txt", "items.txt")
    PLAYER = Player(1,1) # set starting location of player; you may change the x, y coordinates here as appropriate

    menu = ["look", "inventory", "score", "quit", "back"]

    World.load_map(WORLD, "map.txt")
    World.load_locations(WORLD, "locations.txt")
    World.load_items(WORLD, "items.txt")

    inventoryI = ["T-card", "Lucky Pen", "Cheat Sheet"]
    inventoryF = []
    counter = 0

    while not PLAYER.victory:
        location = WORLD.get_location(PLAYER.x, PLAYER.y)

        # ENTER CODE HERE TO PRINT LOCATION DESCRIPTION
        # depending on whether or not it's been visited before,
        #   print either full description (first time visit) or brief description (every subsequent visit)

        print("What to do? \n")
        '''
        print("[menu]")
        for action in Location.available_actions(Location):
            print(action)

        '''

        choice = input("\nEnter action: ")

        if (choice == "[menu]"):
            print("Menu Options: \n")
            for option in menu:
                print(option)
            choice = input("\nChoose action: ")



        if (choice == "go west" and not WORLD.map[PLAYER.x][PLAYER.y -1] == '-1'):
            PLAYER.move_north()
            counter = counter + 1
            print ("You have ", 50 - counter, " moves left.")
        elif (choice == "go west" and WORLD.map[PLAYER.x][PLAYER.y -1] == '-1'):
            print("This way is blocked!")


        elif (choice == "go east" and WORLD.map[PLAYER.x][PLAYER.y + 1] != '-1'):
            PLAYER.move_south()
            counter = counter + 1
            print ("You have ", 50 - counter, " moves left.")
        elif (choice == "go east" and WORLD.map[PLAYER.x][PLAYER.y + 1] == '-1'):
            print("This way is blocked!")

        elif (choice == "go north" and WORLD.map[PLAYER.x - 1][PLAYER.y] != '-1'):
            PLAYER.move_west()
            counter = counter + 1
            print ("You have ", 50 - counter, " moves left.")
        elif (choice == "go north" and WORLD.map[PLAYER.x - 1][PLAYER.y] == '-1'):
            print ("This way is blocked!")

        elif (choice == "go south" and WORLD.map[PLAYER.x + 1][PLAYER.y] != '-1'):
            PLAYER.move_east()
            counter = counter + 1
            print ("You have ", 50 - counter, " moves left.")
        elif (choice == "go south" and WORLD.map[PLAYER.x + 1][PLAYER.y] == '-1'):
            print("This way is blocked")


        elif (choice == "look"):
            Location.get_brief_description(Location)
            counter = counter + 1

        elif (choice == "look around"):
            Location.get_full_description(Location)
            counter = counter + 1

        elif (choice == "what can i do?"):
            Location.available_actions(Location)

        elif (choice == "view items"):
            print(PLAYER.get_inventory())

        elif (choice == "where am i?"):
            print ("You are at location", WORLD.map[PLAYER.x ][PLAYER.y], " on the map.")


        if counter == 50:
            print ("Sorry, you did not get all the objects in time. Game Over.")
            break

        if WORLD.map[PLAYER.x][PLAYER.y] == '5' and choice == "pick up":
            inventoryI.remove("T-card")
            PLAYER.add_item("T-card")
            print ("You found your TCard!")

        elif WORLD.map[PLAYER.x][PLAYER.y] == '10' and choice == "pick up":
            inventoryI.remove("Lucky Pen")
            PLAYER.add_item("Lucky Pen")
            print ("You found your lucky pen!")

        elif WORLD.map[PLAYER.x][PLAYER.y] == '38' and choice == "pick up":
            inventoryI.remove("Cheat Sheet")
            PLAYER.add_item ("Cheat Sheet")
            print ("You found your cheat sheet!")

        elif (WORLD.map[PLAYER.x][PLAYER.y] != '38' or '5' or '38') and (choice == "pick up"):
            print ("there is nothing to pick up!")

        elif (WORLD.map[PLAYER.x][PLAYER.y] != '20') and (choice == "drop"):
            print ("DROP your items in the exam hall!")

        elif WORLD.map[PLAYER.x][PLAYER.y]== '20' and choice == "drop":

            if len(PLAYER.inventory) == 0:
                print ("You have no items to drop")

            if len(PLAYER.inventory) == 1:
                inventoryF.append(PLAYER.inventory[0])
                PLAYER.remove_item(PLAYER, PLAYER.inventory[0])


            if len(PLAYER.inventory) == 2:
                inventoryF.append(PLAYER.inventory[1])
                PLAYER.remove_item(PLAYER, PLAYER.inventory[1])
                inventoryF.append(PLAYER.inventory[0])
                PLAYER.remove_item(PLAYER, PLAYER.inventory[0])

            if len(PLAYER.inventory) == 3:
                inventoryF.append(PLAYER.inventory[2])
                PLAYER.remove_item(PLAYER, PLAYER.inventory[2])
                inventoryF.append(PLAYER.inventory[1])
                PLAYER.remove_item(PLAYER, PLAYER.inventory[1])
                inventoryF.append(PLAYER.inventory[0])
                PLAYER.remove_item(PLAYER, PLAYER.inventory[0])

        if len(inventoryF) == 3:
            print("Congratulations, you collected all of your items before your exam!")
            print("Best of Luck! :)")
            break





        # CALL A FUNCTION HERE TO HANDLE WHAT HAPPENS UPON USER'S CHOICE
        #    REMEMBER: the location = w.get_location(p.x, p.y) at the top of this loop will update the location if the
        #               choice the user made was just a movement, so only updating player's position is enough to change
        #               the location to the next appropriate location
        # Possibilities: a helper function do_action(WORLD, PLAYER, location, choice)
        # OR A method in World class WORLD.do_action(PLAYER, location, choice)
        # OR Check what type of action it is, then modify only player or location accordingly
        # OR Method in Player class for move or updating inventory
        # OR Method in Location class for updating location item info, or other location data
        # etc....
