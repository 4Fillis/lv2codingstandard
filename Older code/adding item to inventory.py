#function to add an item to the players inventory
#controlled variables so won't need invalid input tests

#how much and what the player has in inventory
inventory = ["socks"]

#item player is adding to inventory
addingitem = "museli bar"

def additem(addingitem):
    if addingitem in inventory:
        print(f"you add another {addingitem} to your knapsack")
    else:
        print(f"you place the {addingitem} in your knapsack")
    inventory.append(addingitem)
    
additem(addingitem)
print(inventory)
