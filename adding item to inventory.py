#function to add an item to the players inventory
#controlled variables so won't need invalid input tests

#how much and what the player has in inventory
#smallitem1 eg socks, med2 eg box, large8 eg basketball
stuffamount = 1
inventory = ["socks"]

#item player is adding to inventory
addingitem = "museli bar"

#INSERT DICTIONARY OF ALL ITEMS AND THEIR SPECIFICS

def additem(addingitem):
    if stuffamount > 25:
        print("you've got so much stuff you can't carry anymore")
        
        #INSERT OPTIONS TO DROP AN ITEM (non criticals only)
        
    if addingitem in inventory:
        print(f"you add another {addingitem} to your knapsack")
    else:
        print(f"you place the {addingitem} in your knapsack")
    inventory.append(addingitem)

    #INSERT FUNCTION TO ADD PTS PER ITEM SIZE
    
additem(addingitem)
print(inventory)
