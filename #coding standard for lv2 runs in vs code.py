#coding standard for lv2
from random import randint

#dictionary of areas
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

#dictionary of descriptions of each area
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

#dictionary of all the NPCs in each area 
npcs = {
  #   name       stature         wearing            action                where                 pronouns   friendship interest / 10
  1:["Coral", "small woman", "pink lab coat", "mixing chemicals", "on a table in the corner", "she", "her", 9],
  2:["Persephone", "tall dark woman", "black mechanics fit", "engineering something in the cogswork", "under a vicious looking copper machine", 4],
  3:["Coral", "small woman", "pink lab coat", "kind"],
  4:["Coral", "small woman", "pink lab coat", "kind"],
  5:["Coral", "small woman", "pink lab coat", "kind"],
  6:["Coral", "small woman", "pink lab coat", "kind"],
  7:["Coral", "small woman", "pink lab coat", "kind"],
  8:["Coral", "small woman", "pink lab coat", "kind"],
}

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


#dictionary of things in areas
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

#variables
#what area you're on
areaindex = 1
#message to be displayed
message = ""

def desc_npc(areaindex):
  npc_desc = npcs[areaindex]
  #get npc and describe them non repeditivley
  if randint(1, 2) == 2:
    npc_desc = f"{npcs[areaindex][2]} {npcs[areaindex][4]} {npcs[areaindex][5]}"
  return(npc_desc)


#function for when player moves areas
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
      desc_npc(areaindex)
      print(f"there's a {npc_desc}")
      #npc does action based on friendliness level
      if npcs[areaindex][8] > 7:
        print(f"{npcs[areaindex][6]} waves at you")
      elif npcs[areaindex][8] > 5:
        print(f"{npcs[areaindex][6]} looks up questioningly")
      else:
        print(f"{npcs[areaindex][6]} tells you to piss off")
    else:
      print("the place is void of any and all people")      

    return(areaindex)

new_area(areaindex, npc_desc="")

#DICTIONARY INDEXING EXAMPLE
my_dict = {"a": [1, 2, 3]}

key = "c"
index = 3

if key in my_dict and index < len(my_dict[key]):
    item = my_dict[key][index]
    print(item)
else:
    print("Error: Key not found or index out of bounds.")
