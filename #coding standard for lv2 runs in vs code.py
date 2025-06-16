#coding standard for lv2
#insert cool docs string
import random 
from random import randint
import time as tme
import sys

#variables
areaindex = 1
interacting = "Coral"
addingitem = ""
insult = ""
name = ""


#lists
npcs_met = []
dead_npcs = []
inventory = ["socks"]
noise_desc_neg = ["unholy", "shrieking", "peircing", "miserable", "pitiful", "low", "a high", "evidently pain-filled", "muffled"]
noises_neg = ["shriek", "moan", "sounds of pain", "cry", "rush"]
howdoes_neg = ["cut", "peirce", "hit", "scratch", "stab"]
#non key items in the game
other_items = ["seaweed", "rocks", "lipstick"]

insults1 = ["jam", "bird", "weak", "annoying", "underbaked", "peirced"]
insults2 = ["brained", "filled", "bag of", "limbed"]
insults3 = ["fool", "child", "elderich horror", "skin"]

#dictionaries
#items given to a specific NPC
give_items = {
  'spade': 'digger man', 
  'earrings': 'child'
}
#items needed at a specific place
key_items = {
  'rusty key': 'door',
  'vial containing beetlejuice': 'ledge',
  'computer':'scrapyard'
}

#areas
areas = {
  1:"Hospital",
  2:"Seaweed farm",
  3:"Cogworks",
  4:"Dark tunnel",
  5:"Drain",
  6:"Nuclear reactor",
  7:"Pit of despair",
  8:"Scrapyard",
}

deft_dir = {
  "left"   : "blank wall", 
  "right"  : "blank wall",
  "forward": "blank wall", 
  "up"     : "ceiling", 
  "down"   : "floor"
}
paths_dict = {
  #area           0 forwards, 1 left, 2 right 3 backwards
  "your room": [0, "rainbow door", "bathroom", 0, 0],
  "rainbow door": [0, "sea themed hallway", "hallway with flower wallpaper" , 0],
  "sea themed hallway": [0, 0, "stairs", "rainbow door"],
  "stairs"     : ["hallway 1",     0,           "sink",              0,           0], 
  "bathroom"      : ["toilet",        0,           "sink",              0,           0], 
  "bathroom"      : ["toilet",        0,           "sink",              0,           0], 
  "bathroom"      : ["toilet",        0,           "sink",              0,           0], 
  "bathroom"      : ["toilet",        0,           "sink",              0,           0], 
}

#items & their location, incl ALL items
item_origin = {
  "spade": areas[1], 
  "earrings": areas[5]
}

#descriptions of each area
area_description = {
  1:"Goopy Worm",
  2:"wiggly",
  3:"iron and copper gears spin in place",
  4:"description",
  5:"description",
  6:"description",
  7:"description",
  8:"description",
}

#NPCs in each area 
npcs_area = {
  1: ["Coral"],
  2: ["Persephone"],
  3: [],
  4: [],
  5: ["child"],
  6: [],
  7: [],
  8: []
}
npcs = {
  #                      0 name                    1 stature              2 wearing                 3 action                                    4 where                                5 6 prns     7 friendship interest / 10
  "Coral":             ["Coral",                 "small woman",        "pink lab coat",         "mixing chemicals",                       "on a table in the corner",                 "she", "her",  9],
  "Persephone":        ["Persephone",            "tall dark woman",    "black mechanics fit",   "twisting a gear in the cogswork",        "under a vicious looking copper machine",   "she", "her",  4],
  "Cookiemaster":      ["Cookiemaster",          "small doughy being", "pink lab coat",         "mixing chemicals",                       "on a table in the corner",                 "she", "her",  9],
  "Hanneman":          ["Hanneman",              "man",                "top hat",               "flirting with himself",                  "in a mirror",                              "he",  "him",  0],
  "child":             ["child",                 "small child",        "pink lab coat",         "mixing chemicals",                       "on a table in the corner",                 "she", "her",  9]
}
npcs_id = {}
list_npcs = list(npcs.keys())

#items and ID
items_heal = {
  "healing liquid": 5,
  "cake": 2
}
items_heal_id = {}
list_items_heal = list(items_heal.keys())

#giving items an id number
for i in range (len(items_heal)):
  items_heal_id.update({i: list_items_heal[i]})
print(items_heal_id)

#giving all npcs an id number
for i in range (len(list_npcs)):
  npcs_id.update({i: list_npcs[i]})
print(npcs_id)

#list of items in each area
items = {
  1:"sedative",
  2:"example_item",
  3:"Cog",
  4:"Dark tunnel",
  5:"Meal",
  6:"Plasma radiation",
  7:"Tiny therapist",
  8:"Metal wheel hat",
}

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

npcs_parts = {
  "Coral": ["left arm", "right leg", "eye", "mass"],
  "Persephone": ["left arm", "golden eye", "false leg", "mass", "head"]
}

#functions
def newln():
  print("\n")

#add delay between each letter to make it look like something is typing
def entity_types(msg):
  newln()
  for char in msg:
      delay = (randint(1, 10))/80
      #used to make sure chars dont print on a newline EVERY.SINGLE.TIME.
      sys.stdout.write(char)
      sys.stdout.flush()
      tme.sleep(delay)

def death():
  newln()
  print("you have died.")
  quit()

#add an item to the players inventory
def additem(addingitem):
    newln()
    if addingitem in inventory:
        print(f"you add another {addingitem} to your knapsack")
    else:
        print(f"you place the {addingitem} in your knapsack")
    inventory.append(addingitem)

def npc_item_response(item, interacting):
  newln()
  print(interacting)
  newln()
  if npcs[interacting][7] > 7:
    print(f"Thank you! You are too kind, I shall treasure this {item}")
  elif npcs[interacting][7] > 4:
    print(f"Thanks for the {item}! :)")
  elif npcs[interacting][7] >= 2:
    print(f".... right ok uh a {item}... nice... thanks..?")
  else:
    print(f":(((( ok ill take it")
  return()

#when user has answer as 'give X'
def giveitem(item, interacting, npcs, keyitems, giveitems, other_items, item_origin, insult):
  warnings = 0
  if item in other_items or giveitems[item]==interacting:
    print(f"you give {interacting} the {item} from {item_origin[item]}")
    npc_item_response(item, interacting)
  elif item in keyitems:
    print(f"you want to give {interacting} the {item}, yet you feel a force keeping you in place, telling you this item is too important to give away")
    warnings += 1
    if warnings > 3:
      entity_types(f"A Voice enters your head and tells you to STOP TRYING TO GIVE THIS {npcs[1].upper()} A {item.upper()}")
      if warnings >= 5:
        entity_types(f"ok FLIP YOU you {insult.upper}, my GRAND PLANS... :( PLEASE LEAVE")
  else: 
    print("you need this somewhere else...")

#player moves areas
def new_area(areaindex, npc_desc):
  newln()
  #if player is in the last area
  if areaindex == 8:
    print("end of game")
  else:
    print(f"You move away from the {area_description[areaindex]} {areas[areaindex]} finding yourself in a "
          f"{area_description[(areaindex + 1)]} {areas[(areaindex + 1)]}")
    #update area index for dictionary use ease, and shows movement
    areaindex += 1
    #describe npc in room is possible
    if npcs[areaindex][1].lower() != "none":
      #get npc and describe them non repeditivley
      if randint(1, 2) == 2:
        npc_desc = f"theres a {npcs[areaindex][1]} {npcs[areaindex][3]} {npcs[areaindex][4]}"
      else:
        npc_desc = f"a {npcs[areaindex][1]} is {npcs[areaindex][3]} {npcs[areaindex][4]}"
      print(f"{npc_desc}")
      #npc does action based on friendliness level
      if npcs[areaindex][7] > 7:
        print(f"{npcs[areaindex][5]} waves at you ^-^")
      elif npcs[areaindex][7] > 5:
        print(f"{npcs[areaindex][5]} looks up questioningly..")
      else:
        print(f"...\n{npcs[areaindex][5]} looks annoyed at the interruption")
    else:
      print("the place is void of any and all people")
  return(areaindex)

#conflict sequence
def fightsequence(interacting, list_npcs):
  #variables
  user_pts = 0
  npc_pts = 0
  win_pts = 3

  print(f"you decide to engage {interacting} in a battle of paper scissors rock!")
  #you try to battle an item
  if interacting not in list_npcs:
    entity_types(f"you... win the battle with the {interacting} because it's a {interacting}")
    return
  
  #move decisions   0          1         2
  fight_options = ['paper', 'scissors', 'rock']
  fight_outcomes = {
    #     choice             win,             lose
    fight_options[0]: [fight_options[2], fight_options[1]],
    fight_options[1]: [fight_options[0], fight_options[2]],
    fight_options[2]: [fight_options[1], fight_options[0]]
  }
  
  #explanation
  print(f"Welcome to {fight_options[0]}, {fight_options[1]}, {fight_options[2]}")
  while user_pts < win_pts and npc_pts < win_pts:
    user_move = input(f"Would you like to: {fight_options[0]}, {fight_options[1]}, or {fight_options[2]}").lower()
    newln()

    #checking valid input
    while user_move not in fight_options:
      print("soo thats not an option, please check spelling and have no puncuation, (e.g rock) now:")
      newln()
      user_move = input(f"Would you like to: {fight_options[0]}, {fight_options[1]}, or {fight_options[2]}").lower()
      newln()
    npc_move = fight_options[randint(0, 2)]

    #npc move
    print(f"{interacting} tries to {npc_move}")
    #who wins does what
    #both do same --> both take damage
    if npc_move == user_move:
      print(f"You both try to {npc_move}! No points are won")
      print(f"You have {user_pts} pts, {interacting} has {npc_pts}")
      #npc wins 
    elif fight_outcomes[user_move][1]:
      print(f"{interacting} {npc_move}'s your {user_move} scoring a point")
    #user wins
    elif fight_outcomes[user_move][0]:
      print(f"You {user_move} {interacting}s {npc_move} scoring a point!")

    #Points
    print(f"You have {user_pts}/{win_pts} needed to win, {interacting} has {npc_pts}")
      
    #npc wins user loses
    if npc_pts > win_pts:
      death()
    #you win
    else:
      print(f"You win the battle!")

