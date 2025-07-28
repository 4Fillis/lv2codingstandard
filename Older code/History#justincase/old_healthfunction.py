name = "maria"

#dictionaries
bodyparts = {
  "left arm": "pulls out", 
  "right arm": "scratches", 
  "shirt": "grabs",
  "left leg": "pulls", 
  "right leg": "yoinks", 
  "foot": "stamps on",
  "mass": "grabs at",
  "head": "yanks", 
  "eye": "pokes",
  "shin": "bruises"
}
inventory = ["sock", "healing liquid", "healing liquid"]
parts_taken = ["left arm", "golden eye", "false leg", "mass", "head", "yep", "a", "b", "c" ,"d"]
items_healing = {
    "healing liquid": 5,
    "cake": 2
}
def newln():
  print("\n")
def death():
    print("you have died")
    quit()

def heal(inventory, items_healing):
    answer = ""
    items_heal = inventory.count("healing liquid")
    while answer != "yes" and answer != "no":
        print("please answer 'yes' or 'no'")
        answer = input(f"Would you like to heal? you have {items_heal} vials of healing liquid").lower
    if answer == 'yes':
        #item user wants to use to heal
        key = "healing liquid"
        inventory.remove(key)
        for i in range(items_healing[key]):
            parts_taken



#function to check players hp
def healthcheck(parts_taken, bodyparts, name):
    health_max = len(bodyparts)
    health = health_max - len(parts_taken)
    health_percent = (health/health_max)*100
    print(f"{name}, you have {health_percent}% health")
    
    if health_percent >= 100:
        print("you feel: spectacular, forge onwards!")
    else:
    #increments, messages based on health %
        if health_percent >= 75:
            print(f"you are finee")
        elif health_percent >= 50:
            print(f"status = mehh, ok above average")
        elif health_percent >= 25:
            print(f"Advice: heal")
        elif health_percent > 0:
            print(f"your wounds have taken a heavy toll\n"
            "Advice: do not to continue without sufficient healing")
        else:
            print("ERROR entity_living == false")
            print("you collapse on the ground as you're wounds prove too much to handle")
            death()
        heal(inventory, items_healing)
    return()
        

healthcheck(parts_taken, bodyparts, name, inventory, items_healing)
