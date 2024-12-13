import random  # Imports the random module

#Creating the rules function to display the rules of the game
def rules():
    print('\n\nIn a game of 100 we start with a total of 0 \nand we take turns adding from 1-10 to that total.\nWhoever is able to add a number to the total to get 100 wins.\n\n')
    menu()

#Creating the playGame function to allow the user to play the game
def playGame():
    gameNum = 0
    turn = 0

    turn = input("Do you want to go first or second? ").lower().strip()
    if turn == "second":
        gameNum = random.randint(1, 10)
        print(f"Computer added {gameNum}, which means the total is {gameNum}")
    
    while gameNum < 100:
        turn = int(input("Enter a number from 1-10: "))
        gameNum += turn
        print(f"you entered {turn}, which means the total is {gameNum}")
        if gameNum >= 100:
            print("You win!")
            break
        if gameNum >= 90 and gameNum < 100:
            print(f"Computer added {100 - gameNum}, which means the total is 100")
            print("Computer wins!")
            break
        turn = random.randint(1, 10)
        gameNum += turn
        print(f"Computer added {turn}, which means the total is {gameNum}")
        if gameNum >= 100:
            print("Computer wins!")
            break

        
#Creating the menu function to allow the user to choose between the rules, playing the game, or exiting the game
def menu():
    print("1. Display rules")
    print("2. Play game")
    print("3. Exit")
    choice = int(input("Enter your choice: (1, 2, or 3) "))
    if choice == 1:
        rules()
    elif choice == 2:
        playGame()
    elif choice == 3:
        print("Goodbye")
        exit()
    else:
        print("Invalid choice. Please enter 1, 2, or 3")
        menu()

#actually running the program
menu()