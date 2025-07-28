#coding standard for lv2
#insert cool docs string
import random 
from random import randint
import time as tme
import sys
print("\n")
#variables
area_no = 1
interacting = "Coral"
addingitem = ""
insult = ""
name = ""
name_friend = "friends name"
#directional values
f = "n/a"
l = "n/a"
r = "n/a"
b = "n/a"


#AREAS
#use variables to show in what direction there is nothing
f = "n/a f"
l = "n/a l"
r = "n/a r"
b = "n/a b"
end_goal = "end goal"


#lists
npcs_met = []
inventory = ["socks"]

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


#areas list with key numbers
al = [{0:"starting room"}, {1:"candy cane bathroom"}, {2:"rainbow door"}, {3:"pastry hallway"},
{4:"cookie stairs"}, {5:"seaweed power farm"}, {6:"side door"}, {7:"fudge carpark"},
{8:"m&m hallway"}, {9:"toffee office"}, {10:"m&m themed door"}, {11:"small kids room"},
{12:"magic elevator"}, {13:"cookiehouse"}, {14:"gingerbread steps"}, {15:"candy carpark"}, {16:"n/a"},
{17:"candyfloss admin desk"}, {18:"Waiting area"}, {19:"outside"}, {20: name_friend}
]

#to edit paths in each al[a][a] a is the index number from the al list, add location and
#change where it connects
paths_dict = {
  #area    forwards                left                  right               backwards
  #room
  al[0][0]: [(f"{al[2][2]} f"),     (f"{al[1][1]} l"),     r,                  b],
  #bathroom
  al[1][1]: [f,                     l,                     r,                  (f"{al[0][0]} b")],
  #rainbow door
  al[2][2]: [f,                     (f"{al[3][3]} l"),    (f"{al[8][8]} r"),   (f"{al[0][0]} b")],
  #LEFT from room hallway
  al[3][3]: [(f"{al[4][4]} f"),     l,                     r,                  (f"{al[2][2]} b")],
  #RIGHT from room hallway
  al[8][8]: [(f"{al[10][10]} f"),   l,                    (f"{al[9][9]} r"),   (f"{al[2][2]} b")],
  #office
  al[9][9]: [f,                     l,                     r,                  (f"{al[8][8]} b")],
  #little kids room
  al[11][11]:[f,                    (f"{al[12][12]} l"),   r,                  (f"{al[10][10]} b")],
  #Elevator
  al[12][12]:[(f"{al[13][13]} f"),  (f"{al[17][17]} l"),   r,                  b],
  #Admin [facing admin desk/entering building perspective]
  al[17][17]:[f,                    (f"{al[12][12]} l"),   r,                  (f"{al[18][18]} b")],
  #Waitig area
  al[18][18]:[f,                    (f"{al[19][19]} l"),   r,                  (f"{al[17][17]} b")],
  #Outside
  al[19][19]:[(f"{al[20][20]} f"),  l,                     r,                  (f"{al[18][18]} b")],
  #Cookiehouse
  al[13][13]:[(f"{al[14][14]} f"),  l,                     r,                  (f"{al[12][12]} b")],
  #Gingerbread steps
  al[14][14]:[f,                    (f"{al[15][15]} l"),   r,                  (f"{al[13][13]} b")],
  #Candy Carpark
  al[2][2]: [(f"{al[20][20]} f"),   l,                     r,                  (f"{al[14][14]} b")],
  #left from rainbow door/room path
  #Cookie stairs
  al[4][4]: [(f"{al[5][5]} f"),     l,                     r,                  (f"{al[3][3]} b")],
  #seaweed power generator
  al[5][5]: [f,                     l,                    (f"{al[6][6]} r"),   (f"{al[4][4]} b")],
  #side door
  al[6][6]: [(f"{al[7][7]} f"),     l,                    r,                   (f"{al[5][5]} b")],
  #Fudge carpark
  al[7][7]: [f,                     l,                    (f"{al[20][20]} l"), (f"{al[6][6]} b")],
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
  "Kid":               ["Kid",                 "small child",        "pink lab coat",         "mixing chemicals",                       "on a table in the corner",                 "she", "her",  9]
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
objs = {
  #name         type    desc
  "candybag": ["item", "small red bag of M&M's"],
  "lilcreep": ["npc",  "small blue being apparently made of a blue sticky candy"],
  "Hanneman": ["npc",  f"2.8 tall man with a very diginified top hat flirting with himself whilst... standing in the mug of dark liquid"
               " you can't smell but vaugley assume its someones coffee and not something to be stood in"],
  "Penelope": ["npc",  "woman with star studded skin like a country night sky"],
  "coffee":   ["item", ""], 
  "Teddy":    ["item", "small, faded pink, stuffed bear.. it looks very cute"],
  "Files":    ["item", "small pile neat pile of unlabelled files on the desk"],
  "Kid":      ["npc", "small child with about 1.2m of height sitting on a very pink wooden bed "],
  "Cookiemaster": ["npc", "kinda average sized fuzzy blue muppetty being in a *very* rainbow apron"]
}
areas_cnts = {
  al[1][1]:   [objs["candybag"], objs["lilcreep"]], #bathroom
  al[9][9]:   [objs["Teddy"], objs["Files"]], #office
  al[5][5]:   [objs["Penelope"], objs["coffee"], objs["Hanneman"]], #seaweed power room
  al[11][11]: [objs["Kid"]], #kids room
  al[13][13]: [objs["Cookiemaster"]] #cookiehouse
}

#dictionaries


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
  print("ya lost")
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
        entity_types(f"ok you {insult.upper}, my GRAND PLANS... :( PLEASE LEAVE")
  else: 
    print("you need this somewhere else...")

#player moves areas
def new_area(area_no, npc_desc):
  newln()
  #if player is in the last area
  if area_no == 8:
    print("end of game")
  else:
    print(f"You move away from the {area_description[area_no]} {areas[area_no]} finding yourself in a "
          f"{area_description[(area_no + 1)]} {areas[(area_no + 1)]}")
    #update area index for dictionary use ease, and shows movement
    area_no += 1
    #describe npc in room is possible
    if npcs[area_no][1].lower() != "none":
      #get npc and describe them non repeditivley
      if randint(1, 2) == 2:
        npc_desc = f"theres a {npcs[area_no][1]} {npcs[area_no][3]} {npcs[area_no][4]}"
      else:
        npc_desc = f"a {npcs[area_no][1]} is {npcs[area_no][3]} {npcs[area_no][4]}"
      print(f"{npc_desc}")
      #npc does action based on friendliness level
      if npcs[area_no][7] > 7:
        print(f"{npcs[area_no][5]} waves at you ^-^")
      elif npcs[area_no][7] > 5:
        print(f"{npcs[area_no][5]} looks up questioningly..")
      else:
        print(f"...\n{npcs[area_no][5]} looks annoyed at the interruption")
    else:
      print("the place is void of any and all people")
  return(area_no)

#GOOD gets movement choices
def choice_move(area_no, paths_dict, al):
  #dedicating whats in what direction
  left = False
  right = False
  forward = False
  back = False

  for i in range(4):
    
    if (paths_dict[al[area_no][area_no]][i].endswith("b") == True):
      area_b = paths_dict[al[area_no][area_no]][i][:-2]
      print(f"blue streaks lead back to the {area_b}")
      back = True
      
    elif (paths_dict[al[area_no][area_no]][i].endswith("f") == True):
      area_f = paths_dict[al[area_no][area_no]][i][:-2]
      print(f"following pink paint streaks theres a {area_f} ")
      forward = True

    elif (paths_dict[al[area_no][area_no]][i].endswith("l") == True):
      area_l = paths_dict[al[area_no][area_no]][i][:-2]
      print(f"mysterious green brushstrokes appear to lead to {area_l}")
      left = True

    elif (paths_dict[al[area_no][area_no]][i].endswith("r") == True):
      area_r = paths_dict[al[area_no][area_no]][i][:-2]
      print(f"an odd yellow pattern has appears near the {area_r}")
      right = True

    #placeholder to ensure doesn't do trapped text when a direction has nothing
    elif (paths_dict[al[area_no][area_no]][i].endswith("n/a") == False):
      print("You can't escape this room.... you stay there for hours..." \
      f"\n  eventually...\n the staff come looking and take you to {name_friend}")

  print(f"You're in the {al[area_no][area_no]}\n")

#conflict sequence
def fight(interacting, list_npcs):
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

