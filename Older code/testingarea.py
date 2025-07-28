#AREAS
#use variables to show in what direction there is nothing
f = "n/a"
l = "n/a"
r = "n/a"
b = "n/a"
name_friend = "Allie"
area_no = 4
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

def choice_move(area_no, paths_dict, al, moving):

  for i in range(4):
    
    if (paths_dict[al[area_no][area_no]][i].endswith("b") == True):
      area_b = paths_dict[al[area_no][area_no]][i][:-2]
      if moving != True:
        print(f"blue streaks lead back to the {area_b}")
      
    elif (paths_dict[al[area_no][area_no]][i].endswith("f") == True):
      area_f = paths_dict[al[area_no][area_no]][i][:-2]
      if moving != True:
        print(f"following pink paint streaks theres a {area_f} ")
      else:
        area_no = al.index(area_f)
        print(area_no)

    elif (paths_dict[al[area_no][area_no]][i].endswith("l") == True):
      area_l = paths_dict[al[area_no][area_no]][i][:-2]
      if moving != True:
        print(f"mysterious green brushstrokes appear to lead to {area_l}")

    elif (paths_dict[al[area_no][area_no]][i].endswith("r") == True):
      area_r = paths_dict[al[area_no][area_no]][i][:-2]
      if moving != True:
        print(f"an odd yellow pattern has appears near the {area_r}")

    #placeholder to ensure doesn't do trapped text when a direction has nothing
    elif (paths_dict[al[area_no][area_no]][i].endswith("n/a") == False):
      print("You can't escape this room.... you stay there for hours..." \
      f"\n  eventually...\n the staff come looking and take you to {name_friend}")


  print(f"You're in the {al[area_no][area_no]}\nwhere go?")


  