#working document
import tkinter as tk

#main colors for gui
txt_clr = "#e7f3ff"
bg_clr = "#b8860b"
font = "OpenDyslexic"

#Variables : AREAS
#use variables to show in what direction there is nothing
n = "north fall"
s = "south fall"
e = "east fall"
w = "west fall"
name_friend = "Allie"
area_no = 0
#level referrs to if pc has gone up or down (ex. stairs)
level = 0

#areas list with key numbers #todo: make a even/odd counter for areas
al = [{0:"Caravan"}, {1:"hiding place"}, {2:"vanilla plateu"}, {3:"diamond staircase"},
{4:"suspended gold tiled walkway"}, {5:"broken path to docks"}, {6:"secret exit"}, {7:"gondola"},
{8:"blue ice path"}, {9:"blue-white pavlivion"}, {10:"icy rails"}, {11:"station"},
{12:"woods ghost"}, {13:"gelantinous river"}, {14:"gelatinous pool"}, {15:"sunken steps"}, {16:"marshlands"},
{17:"docks"}, {18:"boat"}, {19:"forest path"}, {20: "wasteland"}, {21: "Decrepit tower"}
]
al_id = {}
#making dictionary with areas & their id number
for i in range(len(al)):
  al_id.update({al[i][i]:i})

#to edit paths in each al[a][a] a is the index number from the al list, add location and
#change where it connects
paths_dict = {
  #area       north                   south                  east                west,
  #caravan
  al[0][0]:   [(f"{al[2][2]} n"),     (f"{al[20][20]} s"),   e,                  (f"{al[1][1]} w")],
  #hiding place
  al[1][1]:   [n,                     s,                    (f"{al[0][0]} e"),   w],
  #vanilla plateu
  al[2][2]:   [n,                     s,                    (f"{al[3][3]} e"),   (f"{al[8][8]} w")],
  #LEFT diamond staircase
  al[3][3]:   [n,                     s,                    (f"{al[4][4]} e"),   (f"{al[2][2]} w")],
  #suspended gold tiled walkway
  al[4][4]:   [n,                     s,                    (f"{al[3][3]} e"),   (f"{al[5][5]} w")],
  #broken path to docks
  al[5][5]:   [(f"{al[6][6]} n"),     s,                    (f"{al[4][4]} e"),   (f"{al[17][17]} w")],
  #secret exit
  al[6][6]:   [(f"{al[7][7]} n"),    (f"{al[5][5]} s"),     e,                   w],
  #gondola
  al[7][7]:   [n,                    (f"{al[6][6]} s"),     (f"{al[12][12]} e"), w],
  #blue ice path
  al[8][8]:   [n,                    s,                     (f"{al[9][9]} e"),   (f"{al[2][2]} w")],
  #blue-white pavivion
  al[9][9]:   [n,                    s,                     (f"{al[10][10]} e"), (f"{al[8][8]} w")],
  #icy rails
  al[10][10]: [n,                    s,                     (f"{al[11][11]} e"), (f"{al[9][9]} w")],
  #station
  al[11][11]: [(f"{al[13][13]} n"),  s,                     (f"{al[16][16]} e"), (f"{al[10][10]} w")],
  #woods ghost
  al[12][12]: [(f"{al[21][21]} n"),  s,                     (f"{al[19][19]} e"), (f"{al[7][7]} w")],
  #gelationous liquid
  al[13][13]: [(f"{al[14][14]} n"),  (f"{al[11][11]} s"),   e,                   w],
  #gelatinous pool
  al[14][14]: [(f"{al[15][15]} n"),  (f"{al[13][13]} s"),   e,                   w],
  #sunken steps
  al[15][15]: [n,                    (f"{al[14][14]} s"),   (f"{al[16][16]} e"), (f"{al[19][19]} w")],
  #marshlands
  al[16][16]: [n,                    s,                     e,                   w],
  #docks
  al[17][17]: [n,                    s,                    (f"{al[20][20]} e"),  (f"{al[18][18]} w")],
  #boat escape
  al[18][18]: [n,                    s,                     e,                   w],
  #forest path
  al[19][19]: [n,                    s,                    (f"{al[15][15]} e"),  (f"{al[12][12]} w")],
  #caught
  al[20][20]: [n,                    s,                     e,                   w],
  #Decrepit tower
  al[21][21]: [n,                    s,                     e,                   w],
}


#sorts users actions
def action_sort(input):
  dirs = ["north", "south", "east", "west"]
  lndmrks = [al[17][17], al[21][21], al[16][16], al[20][20]]
  pair = {
    al[21][21]: "north",
    al[20][20]: "south",
    al[16][16]: "east",
    al[17][17]: "west",
  }
  if input in lndmrks:
    input = pair[input]
  if input in dirs:
    move(input, area_no, paths_dict, al_id)

def move(input, area_no, paths_dict, al_id):
  go = {
      "north": paths_dict[al[area_no][area_no]][0][:-2],
      "south": paths_dict[al[area_no][area_no]][1][:-2],
      "east": paths_dict[al[area_no][area_no]][2][:-2],
      "west": paths_dict[al[area_no][area_no]][3][:-2]
    }
  print(f"in: {al[area_no]},\narea number: {area_no}")
  where_go = go[input]
  area_no = al_id[where_go]
  print(f"changed to: {where_go}\narea number: {area_no}")
  return area_no

def update_gui():
  print("hi")
#Takes user input and clears input bar
def user_input():
    input = input_bar.get()
    print(f"User input:\n{input}")
    input_bar.delete(0, tk.END)
    action_sort(input)
    update_gui()

#creating window
root = tk.Tk()
root.geometry("300x180")
root.title("Game title")
root.configure(bg=txt_clr) #background color

label = tk.Label(
    root,
    text="What do you want to do?",
    bg=txt_clr, #gui background
    fg=bg_clr, #text color
    font=(font, 12, "bold")
)
#padding 20 above, 5 below
label.pack(pady=(35, 5))

#entry box frame, padx & pady are text input space
entry_frame = tk.Frame(root, bg=txt_clr, padx=15, pady=10)
entry_frame.pack()

input_bar = tk.Entry(
    entry_frame,
    width=30,
    relief="solid", #border style
    borderwidth=2,
    bg="#f0f8ff", #input box bg color
    fg="#000000", #text color
    font=(font, 10)
)
input_bar.pack()

input_button = tk.Button(
    root,
    text="Get Text",
    command=user_input,
    bg=bg_clr, #background color
    fg="white", #text color
    activebackground="#e6b438", #color change when pressed
    font=(font, 10, "bold"))
#button space 10 above, 20 below
input_button.pack(pady=(10, 20))

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
      "north": paths_dict[al[area_no][area_no]][0][:-2],
      "south": paths_dict[al[area_no][area_no]][3][:-2],
      "east": paths_dict[al[area_no][area_no]][1][:-2],
      "west": paths_dict[al[area_no][area_no]][2][:-2]
    }
  where_go = go[dir]
  if "can't go that way" not in where_go:
    print(f"where go is: {where_go}")
    area_no = al_id[where_go]
    print(f"after move {area_no}")
  else:
    print("no u cant go that way theres a wall or smth")

# Start the Tkinter event loop
root.mainloop()
