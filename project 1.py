#Getting all of the variables as inputs
from pickle import TRUE


payRate = float(input("Estimated earnings per view in cents: "))/100
dailyViews = float(input("Estimated daily views: "))
minEarnings = float(input("Minimum yearly revenue: $"))

#Calculating the estimated earnings and printing them
estimatedEarnings = payRate * (dailyViews * 365)
print(f"Estimated yearly earnings would he ${estimatedEarnings}")

#Getting if the user-defined goal was met and telling them if they did or didn't meet it
if estimatedEarnings >= minEarnings:
    print("You made your yearly goal!")
elif estimatedEarnings >= (minEarnings * 0.85) and estimatedEarnings < minEarnings:
    print(f"This is greater than 85% of your goal, but you were still ${minEarnings - estimatedEarnings} off from your goal")
else:
    print("You did not meet your yearly goal")