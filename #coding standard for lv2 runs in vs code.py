#coding standard for lv2
#insert cool docs string
from random import *

#variables
areaindex = 1
interacting = "Coral"
#message to be displayed
message = ""

#areas
areas = {
  1:"Hospital",
  2:"Seaweed farm",
  3:"Cogworks",
  4:"Dark tunnel",
  5:"Canteen",
  6:"Nuclear reactor",
  7:"Pit of despair",
  8:"Scrapyard",
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
npcs = {
  #  0 name     1 stature       2 wearing          3 action              4 where            5 6 pronouns   7 friendship interest / 10
  1:["Coral", "small woman", "pink lab coat", "mixing chemicals", "on a table in the corner", "she", "her", 9],
  2:["Persephone", "tall dark woman", "black mechanics fit", "engineering something in the cogswork", "under a vicious looking copper machine", "she", "her",  4],
  3:["Coral", "small woman", "pink lab coat", "kind"],
  4:["Coral", "small woman", "pink lab coat", "kind"],
  5:["Coral", "small woman", "pink lab coat", "kind"],
  6:["Coral", "small woman", "pink lab coat", "kind"],
  7:["Coral", "small woman", "pink lab coat", "kind"],
  8:["Coral", "small woman", "pink lab coat", "kind"],
}

#npcs in a list for checking if x is npc in fight
list_npcs = []
for i in range(len(npcs)):
  list_npcs.append(str(npcs[i+1][0]))

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
#things in areas
area_attribute = {
  areas[1]: [npcs[1], items[1], area_description[1]],
  areas[2]: [npcs[2], items[2], area_description[2]],
  areas[3]: [npcs[3], items[3], area_description[3]],
  areas[4]: [npcs[4], items[4], area_description[4]],
  areas[5]: [npcs[5], items[5], area_description[5]],
  areas[6]: [npcs[6], items[6], area_description[6]],
  areas[7]: [npcs[7], items[7], area_description[7]],
  areas[8]: [npcs[8], items[8], area_description[8]],
}
#health
health = {
  "bread":1,
  "Coral":5,
  "Player":3,
  "clam":2
  }
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
  "you": "pushes", 
  "shin": "bruises"
}

npcs_parts = {
  "Coral": ["left arm", "right leg", "eye", "mass"],
  "Persephone": ["left arm", "golden eye", "false leg", "mass", "head"]
}

#functions
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

new_area(areaindex, npc_desc="")


#conflict sequence
def fightsequence(interacting, npcs, list_npcs, health, bodyparts, areaindex):
  print("fight sequence begin")
  #if you try to fight an item
  if interacting not in list_npcs:
    print(f"you... smash the {interacting} on the rocky ground in anger")
    return
  
  interacting_parts = npcs_parts[interacting]

  while health[interacting] > 0 and health["Player"] > 0:
    #move decisions   0          1         2
    fight_cando = ['paper', 'scissors', 'rock']
    fightchoices = {
      #choice              win,           lose
      fight_cando[0]: [fight_cando[2], fight_cando[1]],
      fight_cando[1]: [fight_cando[0], fight_cando[2]],
      fight_cando[2]: [fight_cando[1], fight_cando[0]]
    }
    user = input(f"Would you like to: {fightchoices[0]}, {fightchoices[1]}, or {fightchoices[2]}\n")
    npc = fightchoices[randint(0, 2)]

    #npc move
    print(f"{interacting} tries to {npc}")
    parts_taken = []
    #who wins does what
    if npc == user:
      print(f"you both try to {user}. Nothing happens.")
      #if npc wins randomise hit message + body part taken
    elif fightchoices.index(npc) == (fightchoices.index(user) -1):
      print("npc wins")
      bodyparts_list = list(bodyparts.keys())
      print(bodyparts_list)
      print(type(bodyparts_list))
      hits_what = bodyparts_list[randint(0, (len(bodyparts_list)-1))]
      hits_how = bodyparts[hits_what]
      del bodyparts[hits_what]
      parts_taken.append(hits_what)
      damage = randint(1, 2)
      health['Player'] -= damage 
      print(f"{interacting} {hits_how} your {hits_what}\n you feel your health decrease by {damage} as the {npcs[areaindex][1]} wins a hit")
    #if user wins
    elif fightchoices.index(user) == (fightchoices.index(npc) -1):
      print("user wins")
      hits_what = interacting[randint(0, (len(interacting_parts)-1))]
      interacting_parts.remove(hits_what)
      damage = randint(1, 2)
      health[interacting] -= damage
      print(f"you swipe at {interacting} and feel {npcs[interacting][6]} {hits_what} disintegrate from the holy light")
    else:
      print("did not work")


fightsequence(interacting, npcs, list_npcs, health, bodyparts, areaindex)
