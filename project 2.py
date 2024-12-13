#establishing a while loop to allow the user to make multiple orders
continueProgram = True
while continueProgram == True:
    #Establishing variables
    numOfInvites = int(input("How many people are you inviting to the party? "))
    color = input("Are the invitations in color? (y/n) ")
    mail = input("Are you mailing the invitations? (y/n) ")
    digital = input("Are you sending digital invitations? (y/n) ")

    #Working with variables to determine cost
    if numOfInvites >= 100:
        cost = .75 * numOfInvites
    elif numOfInvites >= 20 and numOfInvites < 100:
        cost = .50 * numOfInvites
    else:
        cost = .40 * numOfInvites

    #Color
    if color == "y":
        totalCost = cost + (.25 * numOfInvites)    
        costWoC = (.25 * numOfInvites)
    else:
        totalCost = cost

    #Mailing
    if mail == "y":
        totalCost = totalCost + (.40 * numOfInvites)
        costWoM = (.40 * numOfInvites)

    #digital
    if digital == "y":
        totalCost = totalCost + (.10 * numOfInvites) + 10
        costWoD = (.10 * numOfInvites) + 10

    #Printing the total cost
    print(f"\nTotal Bill: \n  Party Invitations Inc. \n__________________________ \n\nInvitations ordered: {numOfInvites} \nExtras chosed: \n")
    if color == "y":
        print("  Color \n")
    if mail == "y":
        print("  Mailed invitations \n")
    if digital == "y":
        print("  Digital invitations \n")
    if color != "y" and mail != "y" and digital != "y":
        print("  None \n")

    #Printing cost and extras
    print(f"\nCost of invitations: ${cost} ")
    if color == "y":
        print(f"Cost of color invites ($0.25 per invitation): ${costWoC} ")
    if mail == "y":
        print(f"Cost of mailed invites ($0.40 per invitation): ${costWoM} ")
    if digital == "y":
        print(f"Cost of digital invites ($0.10 per invitation plus additional $20): ${costWoD} \n")
    print(f"  Total cost: ${totalCost}")

    #Looping the program to create a new order (Extra credit portion)
    continueProgram = input("Would you like to make another order? (yes/no) ")
    if continueProgram == "no":
        continueProgram = False
    else:
        continueProgram = True
        print("\n\n\n")
