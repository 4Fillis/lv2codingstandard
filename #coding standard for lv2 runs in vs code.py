#coding standard for lv2
#insert cool docs string
from random import *
import time as tme
import sys

#variables
areaindex = 1
interacting = "Coral"
addingitem = ""


#lists
npcs_met = []
dead_npcs = []
inventory = ["socks"]
noise_desc_neg = ["unholy", "shrieking", "peircing", "miserable", "pitiful", "low", "a high", "evidently pain-filled", "muffled"]
noises_neg = ["shriek", "moan", "sounds of pain", "cry", "rush"]
howdoes_neg = ["cut", "peirce", "hit", "scratch", "cry"]
#non key items in the game
other_items = ["seaweed", "rocks", "lipstick"]

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
  #        0 name     1 stature       2 wearing          3 action              4 where            5 6 pronouns   7 friendship interest / 10
  "Coral":["Coral", "small woman", "pink lab coat", "mixing chemicals", "on a table in the corner", "she", "her", 9],
  "Persephone":["Persephone", "tall dark woman", "black mechanics fit", "engineering something in the cogswork", "under a vicious looking copper machine", "she", "her",  4],
  "Credit card cookie":["Coral2", "small woman", "pink lab coat", "mixing chemicals", "on a table in the corner", "she", "her", 9],
  "digger man":["aname", "small woman", "pink lab coat", "mixing chemicals", "on a table in the corner", "she", "her", 9],
  "child":["bname", "small woman", "pink lab coat", "mixing chemicals", "on a table in the corner", "she", "her", 9],
  "name3":["cname", "small woman", "pink lab coat", "mixing chemicals", "on a table in the corner", "she", "her", 9],
}
npcs_id = {}
list_npcs = list(npcs.keys())

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
#add delay between each letter to make it look like something is typing
def entity_types(msg):
    for char in msg:
        delay = (randint(1, 10))/80
        #used to make sure chars dont print on a newline EVERY.SINGLE.TIME.
        sys.stdout.write(char)
        sys.stdout.flush()
        tme.sleep(delay)


def death():
  print("you have died.")
  quit()
#add an item to the players inventory
def additem(addingitem):
    if addingitem in inventory:
        print(f"you add another {addingitem} to your knapsack")
    else:
        print(f"you place the {addingitem} in your knapsack")
    inventory.append(addingitem)

def npc_item_response(interacting, item):
  if npcs[interacting][7] > 7:
    print(yay)

#when user has answer as 'give X'
def giveitem(interacting, item, npcs, keyitems, giveitems, other_items, item_origin):
  warnings = 0
  if item in other_items or giveitems[item]==interacting:
    print(f"you give {interacting} the {item} from {item_origin[item]}")
    print(npc_item_response[item][interacting])
  elif item in keyitems:
    print(f"you want to give {interacting} the {item}, yet you feel a force keeping you in place, telling you this item is too important to give away")
    warnings += 1
    if warnings > 3:
      entity_types(f"The Voice Of God enters your head and tells you to STOP TRYING TO GIVE THIS {npcs[1].upper()} A {item.upper()}")
      if warnings >= 5:
        entity_types("ok FLIP YOU you small BEING, you are MINISCULE and INSIGNIFICANT in my GRAND PLANS now FUDGENUGGETS the H E DOUBLE HOCKEY STICKS OUTTA HERE")
  else: 
    print("you need this somewhere else...")



#player moves areas
def new_area(areaindex, npc_desc):
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
        print(f"...\n{npcs[areaindex][5]} tells you to piss off")
    else:
      print("the place is void of any and all people")
  return(areaindex)

#conflict sequence
def fightsequence(interacting, npcs, npcs_parts, list_npcs, bodyparts, noise_desc_neg, noises_neg, dead_npcs, howdoes_neg):
  print(f"you decide to fight {interacting}")
  #if you try to fight an item
  if interacting not in list_npcs:
    entity_types(f"you... smash the {interacting} on the rocky ground in anger")
    return
  
  interacting_parts = npcs_parts[interacting]
  bodyparts_list = list(bodyparts.keys())

  
    #move decisions   0          1         2
  fight_options = ['paper', 'scissors', 'rock']
  fight_outcomes = {
    #     choice             win,             lose
    fight_options[0]: [fight_options[2], fight_options[1]],
    fight_options[1]: [fight_options[0], fight_options[2]],
    fight_options[2]: [fight_options[1], fight_options[0]]
  }
  parts_taken = []
  parts = ""
  
  while len(bodyparts_list) > 0 and len(interacting_parts) > 0:
    user = input(f"Would you like to: {fight_options[0]}, {fight_options[1]}, or {fight_options[2]}\n").lower()

    #checking minor misspellings e.g adding characters
    while user not in fight_options:
      print("soo thats not an option, please check spelling and have no puncuation, (e.g rock) now:\n")
      user = input(f"Would you like to: {fight_options[0]}, {fight_options[1]}, or {fight_options[2]}\n").lower()
    npc = fight_options[randint(0, 2)]

    #npc move
    print(f"{interacting} tries to {npc}")
    #who wins does what
    #both do same --> both take damage
    if npc == user:
      hits_what = interacting_parts[randint(0, (len(interacting_parts)-1))]
      interacting_parts.remove(hits_what)
      print(f"you both try to {user}. you dematerialise {interacting}'s {hits_what},")
      hits_what = bodyparts_list[randint(0, (len(bodyparts_list)-1))]
      hits_how = bodyparts[hits_what]
      bodyparts_list.remove(hits_what)
      parts_taken.append(hits_what)
      print(f"{npcs[interacting][5]} {hits_how} your {hits_what}")
      #if npc wins randomise hit message + body part taken
    elif fight_outcomes[user][1]:
      hits_what = bodyparts_list[randint(0, (len(bodyparts_list)-1))]
      hits_how = bodyparts[hits_what]
      bodyparts_list.remove(hits_what)
      parts_taken.append(hits_what)
      print(f"{interacting} {hits_how} {hits_what}, \n your {hits_what}'s {noise_desc_neg[randint(0, len(noise_desc_neg)-1)]}",
      f"{noises_neg[randint(0, len(noises_neg)-1)]}'s {howdoes_neg[randint(0, len(howdoes_neg)-1)]} the air as it is taken")
    #if user wins
    elif fight_outcomes[user][0]:
      hits_what = interacting[randint(0, (len(interacting_parts)-1))]
      interacting_parts.remove(hits_what)
      print(f"you swipe at {interacting} and feel {npcs[interacting][6]} {hits_what} disintegrate from the holy light shining from the tattoos covering your body")
  #if npc wins die
  if len(bodyparts_list) < 1:
    death()
    return("death")
  #if you win
  else:
    print(f"as you force the {hits_what} of the entity calling itself {interacting}'s to split apart a {noise_desc_neg[randint(0, len(noise_desc_neg)-1)]} {noises_neg[randint(0, len(noises_neg))]} is heard")
    dead_npcs.append(interacting)
    for i in range (len(parts_taken)-1):
      parts += parts_taken[i]
      parts += ", "
    print(f"left behind is your {parts}\n you pick them up, carrying them in your arms")
  return(dead_npcs, parts)

