from fileinput import filename
from platform import java_ver
import turtle
import random
import time
import csv


#Creating the turtle
t = turtle.Turtle()
t.speed(10000000000000)

s = turtle.Screen()
s.setup(650,650)

#Class to handle any settings that are implimented 
class settings():
    def __init__(self):
        filename = 'CSV files/settings.csv'
        try:
            with open(filename, 'r') as file:
                reader = csv.reader(file)

                for i, row in enumerate(reader):
                    if i == 0: #Add i==1 or i==2 for new settings to save
                        self.slowText = row[0]
        except:
            self.slowText = True
            filename = 'CSV files/settings.csv'
            with open(filename, 'w', newline='') as f:
                writer = csv.writer(f)
                writer.writerow([self.slowText])
              
    def getSlow(self):
        return self.slowText
    
    def toggleSlow(self):
        self.slowText = not self.slowText
        filename = 'CSV files/settings.csv'
        with open(filename, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([self.slowText])

#Fancy sleep function
def slp(num):
    for i in range(0, 3):
        print(".", end=" ", flush=True)
        time.sleep(num/3)
    print("\n")

#Fancy looking text that prints letter by letter
def printSlow(text):
    if st.getSlow():
        if len(list(text)) >= len(list("Welcome to Booty Bay Buccaneers!")):
            for x in list(text):
                print(x, end="", flush=True)
                time.sleep(random.uniform(.01, .05))
            print("\n")
        else:
            for x in list(text):
                print(x, end="", flush=True)
                time.sleep(random.uniform(.01, .08))
            print("\n")
    else:
        print(text)
        time.sleep(len(list(text)) * .02 if len(list(text)) >= len(list("Welcome to Booty Bay Buccaneers!")) else len(list(text)) * .05)

#Menu for the start of the game
def menu():
    print("\n")
    printSlow("Welcome to Booty Bay Buccaneers!")
    printSlow("Choose an option to start the game: ")
    print("\n")
    filename = 'CSV files/playerSave.csv'
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        for i, value in enumerate(reader):
            if i == 0:
                saveValue = value[0]
        if saveValue != "Empty":
            temp = input("1. Start Game\n2. Load saved game\n3. Instructions\n4. Settings\n5. Exit\n")
            if temp == "1":
                print("\n\nStarting Game...\n\n")
                for i in range(0, 30):
                    time.sleep(random.uniform(0, .5))

                    print("[" + '-' * (i + 1) + ' ' * (30 - i - 1) + f'  {' ' if int(((i + 1) / 30) * 100) < 10 else ''} {' ' if int(((i + 1) / 30) * 100) <100 else ''} {int(((i + 1) / 30) * 100)}%' + "]")
                time.sleep(2)
                roomMenu()
            elif temp == "2":
                print("\n\n")
                printSlow("Loading saved game...")
                p.load()
                #p.testLoad() #For testing purposes
                time.sleep(2)
                roomMenu()
            elif temp == "3":
                print("\n\n")
                printSlow("Instructions: ")
                printSlow("You are a pirate on a quest to find items on each the 5 islands of the map.")
                printSlow("Each island has items that you must find to complete the game.")
                printSlow("You can move between islands by selecting the direction you want to go.")
                printSlow("Your options when on the islands are look, pick, inventory, map, hint, save, and leave.")
                printSlow("Also, DO NOT CLOSE THE WINDOW FOR THE MAP.")
                printSlow("Good luck!")
                print("\n")

                time.sleep(2)
                menu()
            elif temp == "4":

                print("\n")
                printSlow("Settings: ")
                print("\n")
                cont = True
                while cont:
                    printSlow(f"1. Slow Text {"(Currently On) " if st.getSlow() else "(Currently Off) "}")
                    printSlow("2. Delete save file")
                    print("\n")
                    printSlow("Enter the number to toggle on and off, or 'exit' to return to the main menu. ")
                    inpt = input()
                    if inpt == "1":
                        st.toggleSlow()
                        printSlow(f"Slow Text is now {'on' if st.getSlow() else 'off'}")
                        print("\n")
                    elif inpt == "2":
                        temp = input("Are you sure you want to delete the save file? (yes/no) ")
                        if temp.lower() == "yes":
                            filename = 'CSV files/playerSave.csv'
                            with open(filename, 'w', newline='') as f:
                                writer = csv.writer(f)
                                writer.writerow(["Empty"])
                            printSlow("Save file deleted")
                        else:
                            printSlow("Save file not deleted")
                    elif inpt == "exit":
                        cont = False
                    else:
                        printSlow("Invalid input")
                
                print("\n")
                menu()
            elif temp == "5":
                printSlow("Exiting Game...")
                quit()
        else:
            temp = input("1. Start Game\n2. Instructions\n3. Settings\n4. Exit\n")
            if temp == "1":
                print("\n\nStarting Game...\n\n")
                for i in range(0, 30):
                    time.sleep(random.uniform(0, .5))

                    print("[" + '-' * (i + 1) + ' ' * (30 - i - 1) + f'  {' ' if int(((i + 1) / 30) * 100) < 10 else ''} {' ' if int(((i + 1) / 30) * 100) <100 else ''} {int(((i + 1) / 30) * 100)}%' + "]")
                time.sleep(2)
                roomMenu()
            elif temp == "2":
                print("\n\n")
                printSlow("Instructions: ")
                printSlow("You are a pirate on a quest to find items on each the 5 islands of the map.")
                printSlow("Each island has items that you must find to complete the game.")
                printSlow("You can move between islands by selecting the direction you want to go.")
                printSlow("Your options when on the islands are look, pick, inventory, map, hint, save, and leave.")
                printSlow("Also, DO NOT CLOSE THE WINDOW FOR THE MAP.")
                printSlow("Good luck!")
                print("\n")

                time.sleep(2)
                menu()
            elif temp == "3":

                print("\n")
                printSlow("Settings: ")
                print("\n")
                cont = True
                while cont:
                    printSlow(f"1. Slow Text {"(Currently On) " if st.getSlow() else "(Currently Off) "}")
                    print("\n")
                    printSlow("Enter the number to toggle on and off, or 'exit' to return to the main menu. ")
                    inpt = input()
                    if inpt == "1":
                        st.toggleSlow()
                        printSlow(f"Slow Text is now {'on' if st.getSlow() else 'off'}")
                        print("\n")
                    elif inpt == "exit":
                        cont = False
                    else:
                        printSlow("Invalid input")
                
                print("\n")
                menu()
            elif temp == "4":
                printSlow("Exiting Game...")
                quit()
            else:
                printSlow("Invalid input")
                menu()

#Looping function for all the main functions of the game
def roomMenu():
        #Sets place properly from the state saved in player class
        if p.north == True:
            place = "north"
        elif p.south == True:
            place = "south"
        elif p.east == True:
            place = "east"
        elif p.west == True:
            place = "west"
        
        #Instroduction to each island, plays before the player can do anything 
        if p.getIsland() == 1:
            print("\n")
            printSlow(f"You land on the {place} side of Blackwater Bay, a small beautiful island with paper white sand and palm trees that touch the sky.")
            printSlow("The middle of the island is a lush dense forest filled with all sorts of tropical animals.")
            printSlow("On the north shore, you see a dusty beer bottle lodged in the sand with a rolled up scroll inside.")
            print("\n")
        elif p.getIsland() == 2:
            print("\n")
            printSlow(f"You land on the {place} side of Skullhaven Isle, a volcano-y island with rugged terrain and sparse vegetation.")
            printSlow("The landscape is dominated by black volcanic rocks and ash, creating a desolate and eerie atmosphere.")
            printSlow("The air is filled with the smell of sulfur and the distant rumbling of the volcano can be heard. ")
            printSlow("Be cautious as you explore this treacherous island, as it is known for its unpredictable volcanic activity.")
            printSlow("Keep an eye out for any hidden treasures amidst the rocky terrain.")
            print("\n")
        elif p.getIsland() == 3:
            print("\n")
            printSlow(f"You arrive on the {place} side of Cursed Cove, an island filled with giant palm trees shoulder to shoulder that populate almost all the island. ")
            printSlow("The island is known for its lush vegetation and tropical climate, making it a popular destination for tourists and nature enthusiasts. ")
            printSlow("The island is also home to a variety of wildlife, including colorful birds, playful monkeys, and exotic fish. ")
            printSlow("As you explore the island, keep an eye out for any hidden treasures or mysterious artifacts that may be waiting to be discovered.")
        elif p.getIsland() == 4:
            print("\n")
            printSlow(f"You beach at the {place} side of Serpents Rest, an island almost completely covered in sand with small brush here and there. ")
            printSlow("The island is known for its sandy beaches, crystal clear waters, and abundant marine life. ")
            printSlow("Be cautious as you explore this treacherous island, as it is known for its unpredictable volcanic activity.")
            printSlow("Keep an eye out for any hidden treasures amidst the rocky terrain.")
            print("\n")
        elif p.getIsland() == 5:
            print("\n")
            printSlow("\nYou land at the southeast bay of Treasure Reef, a huge island with mountainous ranges that cover the south and west of the land. ")
            printSlow("The island is known for its rugged terrain, dense forests, and hidden caves. ")
            printSlow("As you explore the island, keep an eye out for any hidden treasures or mysterious artifacts that may be waiting to be discovered.")
            print("\n")
            slp(2)
            printSlow("On the island, you find a small compass. It initially seems normal, but you realize it isn't pointing north.")
            printSlow("You learn later that the compass has special properties, and points to that which you most desire.")
            slp(2)
            printSlow("You have completed the game! Congratulations!")
            quit()

        #Full game loop
        p.save()
        do = "Where Am I?"
        timeSinceChange = 0
        while place != "gone":
            if timeSinceChange == 4:
                p.hint()
                timeSinceChange = 0
            if "where" in do.lower() or "am" in do.lower() or "location" in do.lower():
                printSlow(f"You are on the {place} side of island {p.getIsland()}")
                timeSinceChange += 1
            elif "go" in do.lower() or "head" in do.lower() or "venture" in do.lower():
                if "north" in do.lower():
                    if place == "north":
                        printSlow("You are already here")
                        p.north = True
                        p.south = False
                        p.east = False
                        p.west = False
                    else:
                        printSlow("Going north")
                        place = "north"
                        p.north = True
                        p.south = False
                        p.east = False
                        p.west = False
                elif "south" in do.lower():
                    if place == "south":
                        printSlow("You are already here")
                        p.north = False
                        p.south = True
                        p.east = False
                        p.west = False
                    else:
                        printSlow("Going south")
                        place = "south"
                        p.north = False
                        p.south = True
                        p.east = False
                        p.west = False
                elif "east" in do.lower():
                    if place == "east":
                        printSlow("You are already here")
                        p.north = False
                        p.south = False
                        p.east = True
                        p.west = False
                    else:
                        printSlow("Going east")
                        place = "east"
                        p.north = False
                        p.south = False
                        p.east = True
                        p.west = False
                elif "west" in do.lower():
                    if place == "west":
                        printSlow("You are already here")
                        p.north = False
                        p.south = False
                        p.east = False
                        p.west = True
                    else:
                        printSlow("Going west")
                        place = "west"
                        p.north = False
                        p.south = False
                        p.east = False
                        p.west = True
                timeSinceChange = 0           
            elif "look" in do.lower() or "search" in do.lower():
                printSlow("Looking around")
                p.look()
                timeSinceChange += 1
            elif "pick" in do.lower() or "grab" in do.lower():
                p.item(place)
                timeSinceChange = 0
            elif "inventory" in do.lower():
                    printSlow("You have these items: ")
                    print("\n")
                    for i in p.inventory:
                        printSlow(i)
                    print("\n")
                    timeSinceChange += 1
            elif "what" in do.lower() or "describe" in do.lower():
                for j in p.inventory:
                    if j in do.lower():
                        p.itemDes(j)
                timeSinceChange += 1
            elif "map" in do.lower():
                if p.inInventory("map"):
                    if "full" in do.lower():
                        printSlow("Opening full map")
                        p.fullMap()
                        print("\n\n\n")
                    else:
                        printSlow("Opening map")
                        p.islandMap(p.isle)
                        print("\n\n\n")
                else:
                    printSlow("You don't have a map")
                timeSinceChange += 1
            elif "hint" in do.lower() or "help" in do.lower():
                p.hint()
            elif "save" in do.lower():
                p.save()
                printSlow("Game saved")
            elif "leave" in do.lower() or "next" in do.lower():
                    printSlow("Attempting to leave the island...")
                    slp(.5)
                    tempIn = 0
                    if p.getIsland() == 1:
                        for i in p.inventory:
                            if i == "map":
                                printSlow("You have all the items and can leave the island.")
                                place = "gone"
                            else:
                                printSlow("You have not found items yet.")
                    elif p.getIsland() == 2:    
                        for i in p.inventory:
                            if i == "gold":
                                if tempIn == 1:
                                    tempIn = 0
                                    printSlow("You have all the items and can leave the island.")
                                    place = "gone"
                                else:
                                    tempIn = 1
                            elif i == "cannonballs":
                                if tempIn == 1:
                                    tempIn = 0
                                    printSlow("You have all the items and can leave the island.")
                                    place = "gone"
                                else: tempIn = 1
                        if place != "gone":
                            printSlow("You have not found items yet.")
                    elif p.getIsland() == 3:
                        for i in p.inventory:
                            if i == "harpoon":
                                if tempIn == 1:
                                    tempIn = 0
                                    printSlow("You have all the items and can leave the island.")
                                    place = "gone"
                                else:
                                    tempIn = 1
                            elif i == "wood":
                                if tempIn == 1:
                                    tempIn = 0
                                    printSlow("You have all the items and can leave the island.")
                                    place = "gone"
                                else: tempIn = 1
                        if place != "gone":
                            printSlow("You have not found items yet.")
                    elif p.getIsland() == 4:
                        for i in p.inventory:
                            if i == "sword":
                                printSlow("You have all the items and can leave the island.")
                                place = "gone"
                        if place != "gone":
                            printSlow("You have not found items yet.")           
            elif "quit" in do.lower() or "exit" in do.lower():
                temp = input("Do you want to save before you quit? (Yes/No) ")
                if temp.lower() == "yes":
                    p.save()
                    printSlow("Game saved")
                    quit()
                else:
                    printSlow("Quitting game...")
                    quit() 
            do = input("What do you want to do? ")

        if p.isle == 1:
            p.isle += 1
            p.encounter(1)
        elif p.isle == 2:
            p.isle += 1
            p.encounter(2)
        elif p.isle == 3:
            p.isle += 1
            p.encounter(3)
        elif p.isle == 4:
            p.isle += 1
            p.encounter(4)
        
primColor = "Yellow"
secColor = "green"

#Class for all functions relating to the island and the map
class island():
    
    #Returns island num from player class
    def getIsland(self):
        return p.isle
    
    #Draws a rock on the island
    def rock(self, size, rockPosX, rockPosY):
        global primColor, secColor
        primColor = "gray"
        secColor = "dark gray"
        self.drawIsland(size, rockPosX, rockPosY, 0, False)

    #Draws tree on island
    def tree(self, size, treePosX, treePosY):
        t.goto(treePosX, treePosY)
        t.pencolor("brown")
        t.width(3*(size/50))
        t.pd()
        t.left(90)
        for i in range(0,10):
            t.forward(2)
            t.left(2)                   
        t.left(65)
        t.pencolor("lime green")
        for i in range(0,10):
            t.forward(1.25)
            t.left(3.5)
        t.pu()
        t.goto(treePosX, treePosY)
        t.right(122.5)
        for i in range(0,10):
            t.forward(2)
            t.left(2)     
        t.pd()
        t.right(70)
        for i in range(0,10):
            t.forward(1.25)
            t.right(3.5)
        t.pu()
    
    #Draws island with the given parameters
    def drawIsland(self, radius, islandPosX, islandPosY, islandNum, trees):
    
        global primColor, secColor, t
        if islandNum == 1:
            primColor = "white"
            secColor = "green"
        elif islandNum == 2:
            primColor = "red"
            secColor = "gray"
        elif islandNum == 3:
            primColor = "yellow"
            secColor = "green"
        elif islandNum == 4:
            primColor = "yellow"
            secColor = "#c29c64"
        elif islandNum == 5:
            primColor = "yellow"
            secColor = "green"


        innerRad = random.uniform(.1,.15)
        turtle.bgcolor("blue")
        t.pu()
        t.goto(islandPosX, islandPosY)
        t.begin_fill()
        t.pencolor(primColor)
        t.fillcolor(primColor)
        t.circle(radius)
        t.end_fill()
        t.goto(islandPosX + 0, islandPosY + (radius*innerRad))
        t.begin_fill()
        t.fillcolor(secColor)
        t.pencolor(secColor)
        t.circle(radius * (1 - innerRad))
        t.end_fill()


        #Sub "Islands"
        if islandNum == 1:
            self.rock(radius*.2, islandPosX - 7, islandPosY + 22)
        elif islandNum == 2:
            lkmcamcs = 0
        elif islandNum == 3:
            self.rock(radius*.25, islandPosX + -10, islandPosY + 27)
        elif islandNum == 4:
            primColor = "lime green"
            secColor = "green"
            self.drawIsland(radius*.22, islandPosX +14, islandPosY + 45, 0, False)
            self.drawIsland(radius*.15, islandPosX -8, islandPosY + 22, 0, False)
            self.drawIsland(radius*.20, islandPosX -14, islandPosY + 35, 0, False)
        elif islandNum == 5:
            primColor = "gray"
            secColor = "blue"
            self.drawIsland(40, islandPosX + 50, islandPosY, 0, False)
            primColor = "blue"
            self.drawIsland(42, islandPosX + 65, islandPosY -15, 0, False)
            self.rock(radius*.17, islandPosX - 8, islandPosY + 20)
            self.rock(radius*.2, islandPosX - 35, islandPosY + 45)
            self.rock(radius*.1, islandPosX + 45, islandPosY + 75)
            


        if trees == True:
            self.tree(radius, islandPosX + 0, islandPosY + 25)
            self.tree(radius, islandPosX + 25, islandPosY + 45)
            self.tree(radius, islandPosX - 15, islandPosY + 65)
    
    #Creating the full map
    def fullMap(self):
        t.clear()
    
        #Printing main islands
        self.drawIsland(35, -150, 100, 1, False)
        self.drawIsland(50, 25, 200, 2, False)
        self.drawIsland(55, 200, -27.5, 3, True)
        self.drawIsland(40, 210, -200, 4, False)
        self.drawIsland(85, -50, -200, 5, False)


        #Description for the main map
        text = "Welcome to the Island Map! \nThere are 5 islands on this map. \nEach island is unique"


        t.goto(-310, -400)
        t.pencolor("dark gray")
        t.hideturtle()

    #Creating the individual island maps
    def islandMap(self, islandNum):

        t.clear()

        #printing the island
        if islandNum == 3:
            self.drawIsland(100, 0, -75, islandNum, True)
        elif islandNum != 1 or islandNum != 2 or islandNum != 3 or islandNum != 4 or islandNum != 5:
            self.drawIsland(100, 0, -75, islandNum, False)


        t.goto(0, -100)
        t.pencolor("dark gray")
        t.hideturtle()
    

#Player class that contains all the functions that involve the player and their inventory
class player(island): 

    def __init__(self):
        self.isle = 1

        self.inventory = []
        self.north = False
        self.south = False
        self.east = False
        self.west = True
            
    #Funtion for looking in the current place on the island, prints a small summary of what is there
    def look(self):
        if self.getIsland() == 1:
            if self.north == True:
                printSlow("You see a dusty beer bottle lodged in the sand with a rolled up scroll inside.")
            elif self.south == True:
                printSlow("You see a small crab scuttling around in the sand. It scuttles away as you approach.")
            elif self.east == True:
                printSlow("You see a small pile of rocks, nothing special about them.")
            elif self.west == True:
                printSlow("You see an object lodged in the sand over on the north beach.")
        elif self.getIsland() == 2:
            if self.north == True:
                printSlow("You see a small bag of gold coins lodged in the rocks.")
            elif self.south == True:
                printSlow("You see a small pile of rocks, nothing special about them.")
            elif self.east == True:
                printSlow("You see a crate of cannonballs along with a lot of rocks, so nothing out of the ordinary.")
            elif self.west == True:
                printSlow("You see a small opening in the rocks that leads nowhere.")
        elif self.getIsland() == 3:
            if self.north == True:
                printSlow("You see a lot of large trees and a small pile of rocks along the beach.")
            elif self.south == True:
                printSlow("You seea large shipwreck on the beach, which seems to have some parts you can salvage. There seems to be a harpoon in good condition that you should be able to use on your ship.")
            elif self.east == True:
                printSlow("There are some fallen trees that you can harvest for some wood to repair your ship.")
            elif self.west == True:
                printSlow("You get jumped by a monkey. He takes a chunk out of your clothes, but doesn't do any physical harm to you.")
        elif self.getIsland() == 4:
            if self.north == True:
                printSlow("You see what appears to be remnants of a previous eruption from a geyser. You also see a small beam of light coming from the west coast.")
            elif self.south == True:
                printSlow("You see mostly sand, but catch a glint of light coming from the west coast if the island.")
            elif self.east == True:
                printSlow("You rummage through the sand and find a small pile of rocks and skip them across the water.")
            elif self.west == True:
                printSlow("You see a sword hilt emerging from the sand.")
    
    #Either adds item to inventory or prints that the item is already in the inventory
    def item(self, place):  
        #Island 1 ___________________________________________________________________________________________________________________________
        if self.getIsland() == 1:
            if place == "north":
                if not p.inInventory("map"):
                    printSlow("You grab the dusty beer bottle and open the scroll. It is a map of the nearby islands.")
                    self.inventory.append("map")
                else:
                    printSlow("You already found the item here")
            elif place == "south":
                printSlow("You try to catch the crab but it scuttles away too quickly.")
            elif place == "east":
                printSlow("You search the rocks but find nothing of interest.")
            elif place == "west":
                printSlow("You dig in the sand and find a small key, though there doesn't seem to be a door for it.")
        #Island 2 ___________________________________________________________________________________________________________________________
        elif self.getIsland() == 2:
            if place == "north":     
                if not self.inInventory("gold"):
                    printSlow("You find a small bag of gold coins lodged in the rocks.")
                    self.inventory.append("gold")
                else:
                    printSlow("You already found the item here")
                
            elif place == "south":
                printSlow("You search the rocks but find nothing of interest.")
            elif place == "west":
                printSlow("You see nothing but a few small rocks and what looks to be a tiny opening that leads nowhere")
            elif place == "east":        
                if not self.inInventory("cannonballs"):
                    printSlow("You find a crate of cannonballs that seem to be in pristine condition and take them with you.")
                    self.inventory.append("cannonballs")
                else:
                    printSlow("You already found the item here")
        #Island 3 ___________________________________________________________________________________________________________________________
        elif self.getIsland() == 3:
            if place == "north":
                printSlow("There is nothing to grab here.")       
            elif place == "south":
                if not self.inInventory("harpoon"):
                    printSlow("You grab the harpoon from the damaged shipwreck and take it back to your ship.")
                    self.inventory.append("harpoon")
                else:
                    printSlow("You already found the item here")
            elif place == "west":       
                printSlow("You can not grab the monkey.")
            elif place == "east":
                if not self.inInventory("wood"):
                    printSlow("You pry a few loose pieces of wood from the fallen trees and take them with you.")
                    self.inventory.append("wood")
                else:
                    printSlow("You already found the item here")

        #Island 4 ___________________________________________________________________________________________________________________________
        elif self.getIsland() == 4:
            if place == "north":
                printSlow("The sand is very rough and irritating.")
            elif place == "south":
                printSlow("You get annoyed by how coarse the sand is becoming.")
            elif place == "west":    
                if not self.inInventory("sword"):

                    printSlow("You find a sword hilt emerging from the sand. You dig it out and find a priceless relic.")
                    self.inventory.append("sword")
                else:
                    printSlow("You already found the item here")
            elif place == "east":
                printSlow("There is nothing but sand here.")
    
    #Gives a short description for every item
    def itemDes(self, item):
        if self.inInventory(item):
            if item == "map":
                printSlow("The map is a rolled up piece of paper with a drawing of the nearby islands.\nIt is not worth much but could be useful.")
            elif item == "gold":
                printSlow("The bag of gold coins is a small leather pouch filled with gold coins.\nThere are 25 gold coins in the pouch which can be useful if anyone demands something worth money.")
            elif item == "cannonballs":
                printSlow("The cannonballs are a crate of cannonballs that seem to be in pristine condition.\nThey could be worth a lot of gold, but they are more valuable to you as ammunition.")
            elif item == "loose wood":
                printSlow("A piece of driftwood that you found on the beach. Should be suitable to do repairs on your ship.")
            elif item == "harpoon":
                printSlow("A harpoon capable of taking down great sea monsters.")
            elif item == "sword":
                printSlow("A great weapon forged for a great warrior. It is a priceless relic.")
            else:
                printSlow("I don't recognize that item.")
        else:
            printSlow("That is not an item in your inventory.")
    
    #Returns True if item is in inventory, False if not
    def inInventory(self, item):
        if item in self.inventory:
            return True
        else:
            return False
    
    #Function for all encounters, along with the code for in between islands
    def encounter(self, num):
        slp(1.5)
        if num == 1:
            roomMenu()
        elif num == 2:
            enemyHP = 100
            youHP = 25
            printSlow("\nWhile sailing to the next island, you are ambushed by a group of pirates! They threaten you, saying 'Give us all ye gold, or face the consequences!'\n")
            inpt = input("Do you want to attack or surrender your gold to the pirates? ").lower().strip()
            if "attack" in inpt.lower().strip("") or "fight" in inpt.lower().strip("") or "kill" in inpt or "battle" in inpt.lower().strip(""):
                while True:
                        printSlow("\nYou attack the pirates")
                        action = random.randint(0, 10)
                        enemyHP -= action
                        if action == 0:
                            printSlow(f"\nYou completely missed and dealt no damage, the enemy pirates still have {enemyHP} health")
                            time.sleep(.5)
                        elif action != 0:
                            printSlow(f"\nyou deal {action} damage, which means the their health is now {enemyHP}")
                            time.sleep(.5)


                        if enemyHP <= 0:
                            printSlow("\nYou have beaten the pirates and move onwards, though your ship has been badly damaged.")
                            time.sleep(2.5)
                            roomMenu()
                            break
                        if enemyHP > 0:
                            dmg = random.randint(1,15)
                            youHP -= dmg
                            printSlow(f"\nThe pirates attack back and deal {dmg} damage")
                            time.sleep(1)
                        if youHP <= 0:
                            printSlow("\nYou have been defeated by the pirates and they take all of your gold.")
                            printSlow("Game Over.")
                            slp(2)
                            menu()
                            break
                        else:
                            printSlow(f"\nYou have {youHP} health left")
                        while True:
                            In = input("\nDo you want to attack again? (yes/no) ").lower().strip()
                            if "yes" in In:
                                time.sleep(.25)
                                break
                            else:
                                printSlow("Wrong answer")
                                time.sleep(.25)              
            
            elif "surrender" in inpt or "give" in inpt or "gold" in inpt:
                printSlow("\nYou surrender your gold and the pirates let you go. You have avoided a doomed fight and live to adventure another day.\n")
                for i in self.inventory:
                    if i == "gold":
                        self.inventory.remove("gold")
                        time.sleep(2)
                        roomMenu()
            else:
                printSlow("I'm sorry, I didn't understand that. Please try again.")
                self.encounter(2)
        elif num == 3:
            slp(2)
            printSlow("While traveling to the next island, you are caught up in a massive storm!")
            printSlow("The storm is causing heavy damage to your ship.")
            while True:
                inpt = input("Do you want to try and repair the ship or abandon it? (Repair/Abandon) ").lower().strip()
                if inpt == "repair":
                    if self.inInventory("wood"):
                        printSlow("You use the wood you found to repair the ship.")
                        self.inventory.remove("wood")
                        printSlow("The ship is repaired and you can continue on your journey.")
                        time.sleep(2)
                        roomMenu()
                    else:
                        printSlow("You don't have the materials to repair the ship.")
                        printSlow("Despite your best efforts, the ship is lost to the storm.")
                        slp(2)
                        printSlow("Game Over")
                        quit()
                elif inpt == "abandon":
                    printSlow("Despite your best efforts, the ship is lost to the storm.")
                    slp(2)
                    printSlow("Game Over")
                    quit()
                else:
                    printSlow("I'm sorry, I didn't understand that. Please try again.")
        elif num == 4:
            enemyHP = 15
            youHP = 25
            printSlow("\nWhile sailing to the final island, an enormous kraken appeared from the water! The only way to get past it is by defeating it!'\n")
            inpt = input("Are you ready to take it on? ").lower().strip()
            if "attack" in inpt.lower().strip("") or "fight" in inpt.lower().strip("") or "yes" in inpt.lower().strip("") or "kill" in inpt.lower().strip("") or "battle" in inpt.lower().strip(""):
                krakenhealth = random.randint(0, 10000)
                printSlow(f"Your harpoon sails into the kraken's eye, severely wounding it for {krakenhealth} health")
                printSlow("Because you have the cannonballs needed to fight, you are able to attack.")
                time.sleep(1.5)
                while True:
                    printSlow("\nYou attack the kraken")
                    action = random.randint(5, 10)
                    enemyHP -= action
                    if action == 0:
                        printSlow(f"\nYou completely missed and dealt no damage, the kraken still has {enemyHP} health")
                        time.sleep(.5)
                    elif action != 0:
                        printSlow(f"\nYou deal {action} damage, which means the krakens health is now {enemyHP}")
                        time.sleep(.5)


                    if enemyHP <= 0:
                        printSlow("\n You plunge your sword in to the kraken, landing the killing blow")
                        printSlow(
                            "\nYou have beaten the kraken and can now move to the next island, covered in the ink of your enemy.")
                        time.sleep(1.5)
                        roomMenu()
                        break
                    if enemyHP > 0:
                        dmg = random.randint(1, 10)
                        youHP -= dmg
                        printSlow(f"\nThe kraken fights back and deals {dmg} damage")
                        time.sleep(1)
                    if youHP <= 0:
                        printSlow("\nYou have been defeated by the kraken and were lost at sea.")
                        printSlow("Game Over")
                        time.sleep(2)
                        menu()
                        break
                    else:
                        printSlow(f"\nYou have {youHP} health left")
                        while True:
                            In = input("\nDo you want to attack again? (yes/no) ").lower().strip()
                            if "yes" in In:
                                time.sleep(.25)
                                break
                            else:
                                printSlow("Wrong answer")
                                time.sleep(.25)
            elif "no" in inpt:
                printSlow("\nYou turn your ship around and sail back to the previous island.")
                p.isle -= 1
                roomMenu()    
            else:
                printSlow("I'm sorry, I didn't understand that. Please try again.")
                self.encounter(4)
    
    #Function for saving the game
    def save(self, filename='CSV files/playerSave.csv'):
        with open(filename, 'w', newline='') as f:
            writer = csv.writer(f)
            islandNum = self.getIsland()
            inventory = self.inventory
                
            row = []
            row.append(islandNum)
            for j in range(len(inventory)):
                row.append(inventory[j])
                
            row.append(self.north)
            row.append(self.south)
            row.append(self.east)
            row.append(self.west)
                
            writer.writerow(row)
    
    #Function for loading the game
    def load(self, filename='CSV files/playerSave.csv'):
        try:
            with open(filename, 'r') as file:
                reader = csv.reader(file)
                for j, row in enumerate(reader):
                    self.isle = int(row[0])
                    self.inventory = row[1:len(row)-4]
                    if row[len(row)-4] == "True":
                        self.north = True
                    else:
                        self.north = False
                    
                    if row[len(row)-3] == "True":
                        self.south = True
                    else:
                        self.south = False
                    
                    if row[len(row)-2] == "True":
                        self.east = True
                    else:
                        self.east = False

                    if row[len(row)-1] == "True":
                        self.west = True
                    else:
                        self.west = False
                        
                        
        except:
            print("No save file found")
            time.sleep(2)
            menu()
    
    #Function for providing a hint to the player
    def hint(self):
        randInt = random.randint(0,2)
        if randInt == 0:
            printSlow("Have you looked in all 4 places for items yet?")
        elif randInt == 1:
            printSlow("What do you still need to acomplish?")
        elif randInt == 2:
            printSlow("What does it say when you try leaving the island?")


p = player()
st = settings()

menu()