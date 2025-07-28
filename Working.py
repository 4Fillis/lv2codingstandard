#import tkinter as tk
#from tkinter import messagebox, ttk
import tkinter as tk
from ttkbootstrap import Style

# Create the main window
root = tk.Tk()
root.geometry("600x500")
root.title("Moving")
style = Style(theme="flatly")

#Variables : AREAS
#use variables to show in what direction there is nothing
f = "n/a"
l = "n/a"
r = "n/a"
b = "n/a"
name_friend = "Allie"
area_no = 0

#areas list with key numbers #todo: make a even/odd counter for areas
al = [{0:"Caravan"}, {1:"hiding place"}, {2:"vanilla plateu"}, {3:"diamond staircase"},
{4:"suspended gold tiled walkway"}, {5:"seaweed power farm"}, {6:"secret door"}, {7:"fudge carpark"},
{8:"ice path"}, {9:"toffee office"}, {10:"m&m themed door"}, {11:"small kids room"},
{12:"magic elevator"}, {13:"cookiehouse"}, {14:"gingerbread steps"}, {15:"candy carpark"}, {16:"n/a"},
{17:"candyfloss admin desk"}, {18:"Waiting area"}, {19:"outside"}, {20: name_friend}
]
al_id = {}
#making dictionary with areas & their id number
for i in range(len(al)):
  al_id.update({al[i][i]:i})

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

#get where user moves to, triggered by check_button fnctn

def choice_move(area_no, paths_dict, al, al_id, dir, moving):
  nothing = "nope sorry! Can't go that way"
  area_f = nothing
  area_b = nothing
  area_l = nothing
  area_r = nothing

  if moving != True:
    for i in range(4):
      if (paths_dict[al[area_no][area_no]][i].endswith("b") == True):
        area_b = paths_dict[al[area_no][area_no]][i][:-2]
        print(f"blue streaks lead back to the {area_b}")
        
      elif (paths_dict[al[area_no][area_no]][i].endswith("f") == True):
        area_f = paths_dict[al[area_no][area_no]][i][:-2]
        print(f"following pink paint streaks theres a {area_f} ")

      elif (paths_dict[al[area_no][area_no]][i].endswith("l") == True):
        area_l = paths_dict[al[area_no][area_no]][i][:-2]
        print(f"mysterious green brushstrokes appear to lead to {area_l}")

      elif (paths_dict[al[area_no][area_no]][i].endswith("r") == True):
        area_r = paths_dict[al[area_no][area_no]][i][:-2] 
        print(f"an odd yellow pattern has appears near the {area_r}")

      #placeholder to ensure doesn't do trapped text when a direction has nothing
      elif (paths_dict[al[area_no][area_no]][i].endswith("n/a") == False):
        print("You can't escape this room.... you stay there for hours..." \
        f"\n  eventually...\n the staff come looking and take you to {name_friend}")

      print(f"NOT moving area_no {area_no}")
  else:
    print("moveing in wrong function")
  print(f"You're in the {al[area_no][area_no]}\nwhere go?")

#function for changing areas when user moves
def change_area(paths_dict, al_id, area_no, dir):
  go = {
      "pnk": paths_dict[al[area_no][area_no]][0][:-2],
      "blu": paths_dict[al[area_no][area_no]][3][:-2],
      "grn": paths_dict[al[area_no][area_no]][1][:-2],
      "ylw": paths_dict[al[area_no][area_no]][2][:-2]
    }
  where_go = go[dir]
  if "an't go that way" not in where_go:
    print(f"where go is: {where_go}")
    area_no = al_id[where_go]
    print(f"after move {area_no}")
  else:
    print("no u cant go that way theres a wall or smth")

#check what user wants to do
def check_button(btn_id):
    move = ["ylw", "grn", "blu", "pnk"]
    if btn_id in move:
        change_area(paths_dict, al_id, area_no, dir)


def move_btn_setup():
#make buttons which send id to check_button
    b1 = tk.Button(root, text="Pink", command=lambda: change_area(paths_dict, al_id, area_no, "pnk"))
    b1.pack(pady=10)

    b2 = tk.Button(root, text="Blue", command=lambda: change_area(paths_dict, al_id, area_no,"blu"))
    b2.pack(pady=10)

    b3 = tk.Button(root, text="Green", command=lambda: change_area(paths_dict, al_id, area_no,"grn"))
    b3.pack(pady=10)

    b4 = tk.Button(root, text="Yellow", command=lambda: change_area(paths_dict, al_id, area_no,"ylw"))
    b4.pack(pady=10)
    #add a nevermind button

move_btn_setup()
# Start the Tkinter event loop
root.mainloop()