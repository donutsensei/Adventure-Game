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
    score = 0

    print("You studied ridiculously hard last night and lost your tcard, lucky pen and cheat sheet. GO FIND THEM")
    print ("Valid commands are : go north, go south, go east, go west, look, look around, pick up, drop, inventory, score, quit and where am i?")
    print ("You have 50 minutes to find everything and go to the exam hall. every step you take is one minute gone lol")
    print ("Each item successfully dropped at the exam hall is 20 points. The faster you get all three items to the hall, the more points you'll earn")
    print ("Good Luck Bro")

    while not PLAYER.victory:
        location = WORLD.get_location(PLAYER.x, PLAYER.y)

        # ENTER CODE HERE TO PRINT LOCATION DESCRIPTION
        # depending on whether or not it's been visited before,
        #   print either full description (first time visit) or brief description (every subsequent visit)


        print("What to do? \n")


        choice = input("\nEnter action: ")



        if (choice == "go west" and not WORLD.map[PLAYER.x][PLAYER.y -1] == '-1'):
            PLAYER.move_north()
            counter = counter + 1
            print(WORLD.get_location(PLAYER.x,PLAYER.y))
            print ("You have ", 40 - counter, " moves left.")
        elif (choice == "go west" and WORLD.map[PLAYER.x][PLAYER.y -1] == '-1'):
            print("This way is blocked!")


        elif (choice == "go east" and WORLD.map[PLAYER.x][PLAYER.y + 1] != '-1'):
            PLAYER.move_south()
            counter = counter + 1
            print(WORLD.get_location(PLAYER.x,PLAYER.y))
            print ("You have ", 40 - counter, " moves left.")
        elif (choice == "go east" and WORLD.map[PLAYER.x][PLAYER.y + 1] == '-1'):
            print("This way is blocked!")

        elif (choice == "go north" and WORLD.map[PLAYER.x - 1][PLAYER.y] != '-1'):
            PLAYER.move_west()
            counter = counter + 1
            print(WORLD.get_location(PLAYER.x,PLAYER.y))
            print ("You have ", 40 - counter, " moves left.")
        elif (choice == "go north" and WORLD.map[PLAYER.x - 1][PLAYER.y] == '-1'):
            print ("This way is blocked!")

        elif (choice == "go south" and WORLD.map[PLAYER.x + 1][PLAYER.y] != '-1'):
            PLAYER.move_east()
            counter = counter + 1
            print(WORLD.get_location(PLAYER.x,PLAYER.y))
            print ("You have ", 40 - counter, " moves left.")
        elif (choice == "go south" and WORLD.map[PLAYER.x + 1][PLAYER.y] == '-1'):
            print("This way is blocked")


        elif (choice == "look"):
            print(WORLD.get_location(PLAYER.x,PLAYER.y))

        elif (choice == "look around"):
            print(WORLD.get_location(PLAYER.x,PLAYER.y))

        elif (choice == "inventory"):
            print(PLAYER.get_inventory())

        elif (choice == "where am i?"):
            print ("You are at location", WORLD.map[PLAYER.x ][PLAYER.y], " on the map.")

        elif (choice == "score"):
            print("Your score is currently", score)

        elif (choice == "quit"):
            print ("You have quit the game. You failed your exam")
            break


        if counter == 40:
            print ("Sorry, you did not get all of your objects in time. Game Over.")
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
            else:
                for item in PLAYER.inventory:
                    inventoryF.append(item)
                    score = score + 20
                    PLAYER.remove_item(item)
                print("You now have ", score, "points")



        if len(inventoryF) == 3:
            print("Congratulations, you collected all of your items before your exam!")
            print("You finished with", score + (40 - counter), "points!")
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
