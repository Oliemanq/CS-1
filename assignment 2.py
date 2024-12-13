#input data
from termios import CR0


numberOfScoops = int(input("How many scoops of vanilla ice cream would you like? (1,2,3) "))

#toppings
chocolateSyrup = input("Would you like chocolate syrup? (yes/no) ").strip().lower() == "yes"
whippedCream = input("Would you like whipped cream? (yes/no) ").strip().lower() == "yes"
reeses = input("Would you like Reeses cups? (yes/no) ").strip().lower() == "yes"
#.strip and .lower are used to make the input case insensitive and to get rid of any extra spaces in the input

#determine basic cost per scoop
if numberOfScoops == 2:
    costPerScoop = .75
elif numberOfScoops == 3:
    costPerScoop = .65
else:
    costPerScoop = 1.00

#calculate total cost
basicCost = numberOfScoops * costPerScoop
toppingCost = 0.00

if chocolateSyrup:
    toppingCost += .50
if whippedCream:
    toppingCost += .30
if reeses:
    toppingCost += 1.00

#total cost
totalCost = basicCost + toppingCost

#display results
print(f"Invoice:\n  You ordered {numberOfScoops} scoops of vanilla ice cream\n")
print(f"  Chocolate syrup: {'Yes' if chocolateSyrup else 'No'}")
print(f"  Whipped cream: {'Yes' if whippedCream else 'No'}")
print(f"  Reeses cups: {'Yes' if reeses else 'No'}")
#Embedded if statement to display yes or no based on whether the topping was selected or not
print(f"\nYour base cost is: ${basicCost:.2f}")
print(f"Your topping cost is: ${toppingCost:.2f}")
print(f"\nYour total cost is: ${totalCost:.2f}")