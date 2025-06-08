
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
parts_taken = ["left arm", "golden eye", "false leg", "mass", "head", "yep", "a", "b", "c" ,"d"]
def newln():
  print("\n")
def death():
    print("you have died")
    quit()
#function to check players hp
def healthcheck(parts_taken, bodyparts, name):
    health_max = len(bodyparts)
    health = health_max - len(parts_taken)
    health_percent = (health/health_max)*100
    print(f"{name}, you have {health_percent}% health")
    
    if health_percent >= 100:
        print("you feel: spectacular, forge onwards!")
    #increments, messages based on health %
    elif health_percent >= 75:
        print(f"you are finee")
    elif health_percent >= 50:
        print(f"status = mehh, ok above average")
    elif health_percent >= 25:
        print(f"Advice: heal")
    elif health_percent > 0:
        print(f"you're wounds have taken a heavy toll\n"
            "Advice: do not to continue without sufficient healing")
    else:
        print("ERROR entity_living == false")
        print("you collapse on the ground as you're wounds prove too much to handle")
        death()

    #INSERT OPTION TO DRINK HEALTH POTION

healthcheck(parts_taken, bodyparts, name="maria")
