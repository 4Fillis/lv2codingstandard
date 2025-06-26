#import random 
#INSULT GENERATOR
#insults1 = ["jam", "bird", "weak", "annoying", "underbaked", "peirced"]
#insults2 = ["brained", "filled", "bag of", "limbed"]
#insults3 = ["fool", "child", "elderich horror", "skin"]

#def generate_insults(insults1, insults2, insults3):
#  i1 = random.choice(insults1)
#  i2 = random.choice(insults2)
#  i3 = random.choice(insults3)
#  insult = i1 + " " + i2 + " "+ i3
#  return(insult)


#AREAS
#use variables to show in what direction there is nothing
f = "n/a f"
l = "n/a l"
r = "n/a r"
b = "n/a b"
name_friend = "Allie"
area_no = 0
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
  #area   forwards                 left                right          backwards
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

#to print dictionary line by line
#for key, value in paths_dict.items():
#  print(f"{key}: {value}")
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
#to print dictionary line by line
#for key, value in areas_cnts.items():
#  print(f"{key}: {value}")

def choice_move(area_no, paths_dict, al):
  #dedicating whats in what direction
  print(paths_dict[al[area_no][area_no]][0][-1])
  for i in range(4):
    print(i)
    if (paths_dict[al[area_no][area_no]][3].endswith("b") == True):
      area_b = paths_dict[al[area_no][area_no]][i]
    elif (paths_dict[al[area_no][area_no]][0].endswith("f") == True):
      area_f = paths_dict[al[area_no][area_no]][1]
    elif (paths_dict[al[area_no][area_no]][1].endswith("l") == True):
      area_l = paths_dict[al[area_no][area_no]][i]
    elif (paths_dict[al[area_no][area_no]][2].endswith("r") == True):
      area_r = paths_dict[al[area_no][area_no]][i]
    else:
      print("You can't go anywhere...")

  #if variable doesn't exist assign as "nothing"
  if area_f in locals():
    area_f = "nothing"
  if area_b in locals():
    area_b = "nothing"
  if area_l in locals():
    area_l = "nothing"
  if area_r in locals():
    area_r = "nothing"


  dir = input(f"You're in the {al[area_no][area_no]}\n"+
  f"forward is a {area_f[:-2]}\n"+
  f"left is the {area_l[:-2]}\n"+
  f"right is the {area_r[:-2]}\n"+
  f"theres a {area_b[-2]} back where you came\n"
  )

choice_move(area_no, paths_dict, al)
