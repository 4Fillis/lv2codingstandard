#working document
import tkinter as tk
from functools import partial
import random

#main colors for gui
txt_clr = "#e7f3ff"
bg_clr = "#b8860b"
font = "OpenDyslexic"

drop_desc = ["blank space  ", "a long drop...  ", 
           "wispy mist winds in the air  ", "the edge of the platform  "]

#Variables : AREAS
#use variables to show in what direction there is no path

def drop(drop_desc):
   desc = random.choice(drop_desc)
   return desc
area_no = {"num": 2}
#level referrs to if pc has gone up or down (ex. stairs)
level = 1

#messages for key game points
txts = {
   "start":"You're travelling away from your homeland Plasnamesrehard,\n"
   "the journey has been hard... \nyet you persist.. taking a different "
   "route \nthan that of your fellow refugees to better your odds \nof "
   "remaining invisible to the dark wizards who hunt \nyour people out "
   "of an old grudge your forefathers held.\n They posses magicks honed "
   "to find most beings, \nyet solo, scruffy travellers \nare too far, "
   "below their notice."
}

#dict of buttons for each area
#ALL areas have direction buttons
area_btns = {
   1:1
}

#areas list with key numbers + description & elevation (level)
al = {
    0: {"area": "Your old camp", "desc": "your old campsite", "level": 1,
         "btns":["north", "south", "hide"]},
    1: {"area": "Hiding Place", "desc": "beneth the roots of an old tree near your camp", "level": 1,
         "btns":["come out"]},
    2: {"area": "Vanilla Plateau", "desc": "a grand open yellow-gold tiled balcony, stairases descend either side", "level": 1,
         "btns":["south", "east", "west"]},
    3: {"area": "Diamond Staircase", "desc": "gleaming blue stairs spiralling down from yellow-gold tiles", "level": 1,
         "btns":["east", "west"]},
     #FOUR
    5: {"area": "Broken Path to Docks", "desc": "an old worn splintered path", "level": 1,
         "btns":["north", "east", "west", "talk", "pick up item"]},
    6: {"area": "Secret Exit", "desc": "a break in the wood behind a canvas railing, a gap, just small enough to sneak through", "level": 1,
         "btns":["north", "south"]},
     #SEVEN
     #EIGHT
    9: {"area": "Blue-White Pavilion", "desc": "an old vine-covered light blue pavlivion still standing resolutley", "level": 1,
         "btns":["east", "west"]},
     #TEN
    11: {"area": "Station", "desc": "a terminal with some benches, very old and worn, breaking apart", "level": 1,
         "btns":["north [jump]", "east", "west", "talk"]},
    12: {"area": "Woods Ghost", "desc": "a standing circle of stones surrounding the half-corporal form of a being", "level": 1,
         "btns":["east", "west", "talk"]},
    13: {"area": "Gelatinous River", "desc": "a thick gooey river made of some substance", "level": -1,
         "btns":["north", "south"]},
     #FOURTEEN
    14: {"area": "Gelatinous Pool", "desc": "a circular pool of this gooey semi transparent substance", "level": 1,
         "btns":["north", "south", "pick up item"]},
     #FIFTEEN
    16: {"area": "Marshlands", "desc": "feilds of marshy wetland caked in a thick fog", "level": 1,
         "btns":["west"]},
    17: {"area": "Docks", "desc": "decrept wooden planks stretching into the mist", "level": 1,
         "btns":[ "east [jump]", "west"]},
    18: {"area": "Boat", "desc": "a small wooden boat apparently abandoned an age ago", "level": 1,
         "btns":["west"]},
     #NINTEEN
    20: {"area": "Wasteland", "desc": "bleak scorched earth covered in ash and burnt gravel", "level": 1,
         "btns":["north"]},
    21: {"area": "Decrepit Tower", "desc": "an old yet proud building spiralling into the sky", "level": 1,
         "btns":["north", "south", "east", "west"]},
    22: {"area": "Stay", "desc": "you stay in place just....watching the shifting mist for a moment", "level": 1,
         "btns":"n/a"}
}

#to edit paths in each al[a]['thingtoget'] a is the index number from the al dict
a = 'area'
paths_dict = {
  #area      north                 south                east                west,
  #caravan
  al[0][a]:  [(f"{al[2][a]} n"),  drop(drop_desc),  drop(drop_desc),     (f"{al[1][a]} w")],
  #hiding place
  al[1][a]:  [drop(drop_desc),    drop(drop_desc),     (f"{al[0][a]} e"),   drop(drop_desc)],
  #vanilla plateu
  al[2][a]:  [drop(drop_desc),    (f"{al[0][a]} s"),   (f"{al[9][a]} e"),   (f"{al[3][a]} w")],
  #LEFT diamond staircase
  al[3][a]:  [drop(drop_desc),    drop(drop_desc),     (f"{al[2][a]} e"),   (f"{al[2][a]} w")],
  #broken path to docks
  al[5][a]:  [(f"{al[6][a]} n"),  drop(drop_desc),     (f"{al[3][a]} e"),   (f"{al[17][a]} w")],
  #secret exit
  al[6][a]:  [(f"{al[12][a]} n"),  (f"{al[5][a]} s"),   drop(drop_desc),     drop(drop_desc)],
  #blue-white pavivion
  al[9][a]:  [drop(drop_desc),    drop(drop_desc),     (f"{al[11][a]} e"),  (f"{al[2][a]} w")],
  #station
  al[11][a]: [(f"{al[13][a]} n"), drop(drop_desc),     (f"{al[16][a]} e"),  (f"{al[9][a]} w")],
  #gelationous liquid
  al[13][a]: [(f"{al[12][a]} n"), (f"{al[11][a]} s"),  drop(drop_desc),      drop(drop_desc)],
  #marshlands
  al[16][a]: [drop(drop_desc),    drop(drop_desc),     drop(drop_desc),      drop(drop_desc)],
  #docks
  al[17][a]: [drop(drop_desc),    drop(drop_desc),     (f"{al[5][a]} e"),    (f"{al[18][a]} w")],
  #boat escape
  al[18][a]: [drop(drop_desc),    drop(drop_desc),     drop(drop_desc),      drop(drop_desc)],
  #staying in same location
  al[22][a]: [(f"{al[22][a]} n"),  (f"{al[22][a]} s"), 
               (f"{al[22][a]} e"), (f"{al[22][a]} w")]
}

#creating window
root = tk.Tk()
root.geometry("1200x750")
root.title("Game title")
root.configure(bg=txt_clr) #background color

#doing background
bg_img = tk.PhotoImage(file="resources/floral_parchment.png")
bg_label = tk.Label(root, image=bg_img)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)


#game text
game_txt = tk.Label(
    root,
    text="Hello, Welcome to the game.",
    bg=txt_clr, #gui background
    fg=bg_clr, #text color
    font=(font, 12, "bold")
)
#padding above, below
game_txt.pack(pady=(20, 5))

txt_done = [None] #list so changeable in function
#ending typing 
#note: parts of tpg_end and tpg_skip were ai made
def tpg_end(root, txt_done):
  if txt_done[0] is not None:
     root.after_cancel(txt_done[0])
     txt_done[0] = None

#skip
def tpg_skip(event=None, txt=None):
    if txt_done[0] is not None and txt is not None:
        update_gui(txt, index=0, txt_done=txt_done, skip=True)

#update gui, end/remove text when start
def update_gui(txt, index=0, txt_done=txt_done, skip=False):
  if index == 0:
      game_txt.bind("<Button-1>", partial(tpg_skip, txt=txt))
      tpg_end(root, txt_done=txt_done)
      game_txt.config(text="")

  #skips typing effect
  if skip:
     game_txt.config(text=txt)
     tpg_end(root, txt_done)
     return
  #wait after printing character for typing effect
  if index < len(txt):
        game_txt.config(text=game_txt.cget("text") + txt[index])
        txt_done[0] = root.after(50, update_gui, txt, index + 1)


#start sequence 
def start_screen():
  #ca=current area
   ca = al[area_no['num']][a]
   start_moves = f"\nYou're in the {ca}\n"f"To your North {paths_dict[ca][0][:-2]}\n"f"South is {paths_dict[ca][1][:-2]}\n"f"To your East is {paths_dict[ca][2][:-2]}\n"f"To the west {paths_dict[ca][3][:-2]}"
   update_gui(txt=txts["start"] + f"\n{start_moves}" +"aaah", index=0)
   

#sorts users actions
def action_sort(input):
  input = input.lower()
  dirs = ["north", "south", "east", "west"]
  lndmrks = [al[17][a], al[21][a], al[16][a], al[20][a]]
  pair = {
    al[21][a]: "north",
    al[20][a]: "south",
    al[16][a]: "east",
    al[18][a]: "west",
  }
  if input in lndmrks:
    input = pair[input]
  elif input in dirs or input == "stay":
    move(input, area_no, paths_dict)
  elif input == "pick up":
    print("pick up item")

def move(input, area_no, paths_dict):
  go = {
      "north": paths_dict[al[area_no['num']][a]][0][:-2],
      "south": paths_dict[al[area_no['num']][a]][1][:-2],
      "east": paths_dict[al[area_no['num']][a]][2][:-2],
      "west": paths_dict[al[area_no['num']][a]][3][:-2],
      "stay": al[area_no['num']]
    }
  dspld_txt = game_txt.cget("text")
  where_go = go[input]
  if not where_go or where_go.strip() in ("", "None"):
        update_gui(txt="Can't get your input... please try again\n"
                  "use simple *valid* inputs like 'north'\n" + dspld_txt, index=0)
        return

    # Try to find the matching area index
  try:
    area_index = next(i for i, v in al.items() if v["area"] == where_go)
    area_no["num"] = area_index
  except StopIteration:
    update_gui(txt="Can't get what you're trying... please try again\n"
              "use simple valid inputs like 'south'\n" + dspld_txt, index=0)
    return
  
  #i=id v=sub dict, comp 'area' w/ where_go to find right math in al
  area_no["num"] = next((i for i, v in al.items() if v["area"] == where_go), None)
  update_gui(txt=f"Currently in: {al[area_no['num']][a]}\n"
            f"Facing North {go['north']}\n"
            f"Immediatley to the South {go['south']}\n"
            f"East there's {go['east']}\n"
            f"and West there's {go['west']}", index=0)

#Takes user input and clears input bar
def user_input(event=None):
    input = input_bar.get()
    input = input.lower()
    print(f"User input: {input}")
    input_bar.delete(0, tk.END)
    action_sort(input)

#input message
input_msg = tk.Label(
    root,
    text="What do you want to do?",
    bg=txt_clr, #gui background
    fg=bg_clr, #text color
    font=(font, 12, "italic")
)
#padding above, below
input_msg.pack(pady=(50, 5))

#entry box frame, padx & pady are text input space
entry_frame = tk.Frame(root, bg=txt_clr, padx=0, pady=0)
entry_frame.pack()

#input bar + button
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
input_bar.bind("<Return>", user_input)
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

#function for changing areas when user moves
def change_area(paths_dict, al_id, area_no, dir):
  go = {
      "north": paths_dict[al[area_no['num']][a]][0][:-2],
      "south": paths_dict[al[area_no['num']][a]][3][:-2],
      "east": paths_dict[al[area_no['num']][a]][1][:-2],
      "west": paths_dict[al[area_no['num']][a]][2][:-2]
    }
  where_go = go[dir]
  if "can't go that way" not in where_go:
    print(f"where go is: {where_go}")
    area_no['num'] = al_id[where_go]
    print(f"after move {area_no['num']}")
  else:
    print("input invalid.")
start_screen()
# Start the Tkinter event loop
root.mainloop()
