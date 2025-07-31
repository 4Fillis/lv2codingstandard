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
level = 0

#areas list with key numbers + description & elevation (level)
al = {
    0: {"area": "Caravan", "desc": "A dusty wagon parked on the ridge with canvas flapping in the wind.", "level": 1},
    1: {"area": "Hiding Place", "desc": "A cramped nook hidden under roots and thick foliage.", "level": 1},
    2: {"area": "Vanilla Plateau", "desc": "Sweeping highlands with icy air and a faint vanilla aroma.", "level": 1},
    3: {"area": "Diamond Staircase", "desc": "Gleaming steps that spiral downward toward the clouds.", "level": 1},
    4: {"area": "Suspended Gold Tiled Walkway", "desc": "A precarious path of golden tiles suspended above fog.", "level": 1},
    5: {"area": "Broken Path to Docks", "desc": "Splintered wood and cracked stone lead down toward the shore.", "level": 1},
    6: {"area": "Secret Exit", "desc": "A narrow tunnel carved through shale, barely wide enough to crawl.", "level": 1},
    7: {"area": "Gondola", "desc": "A sleek lift swaying gently over an abyss, tethered to fraying cables.", "level": 1},
    8: {"area": "Blue Ice Path", "desc": "A slick icy trail glittering under pale light.", "level": 1},
    9: {"area": "Blue-White Pavilion", "desc": "An open terrace shaded by frosted arches.", "level": 1},
    10: {"area": "Icy Rails", "desc": "Twin rails etched with frost, cutting through silent woods.", "level": 1},
    11: {"area": "Station", "desc": "An abandoned terminal echoing with forgotten announcements.", "level": 1},
    12: {"area": "Woods Ghost", "desc": "A grove where trees whisper and shadows linger.", "level": 1},
    13: {"area": "Gelatinous River", "desc": "A wobbling stream of goo, flowing reluctantly through the landscape.", "level": 1},
    14: {"area": "Gelatinous Pool", "desc": "A thick pool of trembling jelly, with strange ripples.", "level": 1},
    15: {"area": "Sunken Steps", "desc": "Stairs half-swallowed by swampy ground and decay.", "level": 1},
    16: {"area": "Marshlands", "desc": "Fog-shrouded wetlands teeming with chirps and rustles.", "level": 1},
    17: {"area": "Docks", "desc": "Wooden platforms stretching out into misty waters.", "level": 1},
    18: {"area": "Boat", "desc": "A simple vessel bobbing gently, its deck slick with morning dew.", "level": 1},
    19: {"area": "Forest Path", "desc": "Twisting path carpeted with damp moss and fallen leaves.", "level": 1},
    20: {"area": "Wasteland", "desc": "Bleak terrain of cracked soil and ash-colored skies.", "level": 1},
    21: {"area": "Decrepit Tower", "desc": "A crumbling spire looming over ruins below.", "level": 1},
    22: {"area": "Stay", "desc": "You remain in place, watching shadows shift around you.", "level": 1}
}

#to edit paths in each al[a]['thingtoget'] a is the index number from the al dict
a = 'area'
paths_dict = {
  #area      north                 south                east                west,
  #caravan
  al[0][a]:  [(f"{al[2][a]} n"),  (f"{al[20][a]} s"),  drop(drop_desc),     (f"{al[1][a]} w")],
  #hiding place
  al[1][a]:  [drop(drop_desc),    drop(drop_desc),     (f"{al[0][a]} e"),   drop(drop_desc)],
  #vanilla plateu
  al[2][a]:  [drop(drop_desc),    (f"{al[0][a]} s"),   (f"{al[8][a]} e"),   (f"{al[3][a]} w")],
  #LEFT diamond staircase
  al[3][a]:  [drop(drop_desc),    drop(drop_desc),     (f"{al[4][a]} e"),   (f"{al[2][a]} w")],
  #suspended gold tiled walkway
  al[4][a]:  [drop(drop_desc),    drop(drop_desc),     (f"{al[3][a]} e"),   (f"{al[5][a]} w")],
  #broken path to docks
  al[5][a]:  [(f"{al[6][a]} n"),  drop(drop_desc),     (f"{al[4][a]} e"),   (f"{al[17][a]} w")],
  #secret exit
  al[6][a]:  [(f"{al[7][a]} n"),  (f"{al[5][a]} s"),   drop(drop_desc),     drop(drop_desc)],
  #gondola
  al[7][a]:  [drop(drop_desc),    (f"{al[6][a]} s"),   (f"{al[12][a]} e"),  drop(drop_desc)],
  #blue ice path
  al[8][a]:  [drop(drop_desc),    drop(drop_desc),     (f"{al[9][a]} e"),   (f"{al[2][a]} w")],
  #blue-white pavivion
  al[9][a]:  [drop(drop_desc),    drop(drop_desc),     (f"{al[10][a]} e"),  (f"{al[8][a]} w")],
  #icy rails
  al[10][a]: [drop(drop_desc),    drop(drop_desc),     (f"{al[11][a]} e"),  (f"{al[9][a]} w")],
  #station
  al[11][a]: [(f"{al[13][a]} n"), drop(drop_desc),     (f"{al[16][a]} e"),  (f"{al[10][a]} w")],
  #woods ghost
  al[12][a]: [(f"{al[21][a]} n"), drop(drop_desc),     (f"{al[19][a]} e"),  (f"{al[7][a]} w")],
  #gelationous liquid
  al[13][a]: [(f"{al[14][a]} n"), (f"{al[11][a]} s"),  drop(drop_desc),      drop(drop_desc)],
  #gelatinous pool
  al[14][a]: [(f"{al[15][a]} n"), (f"{al[13][a]} s"),  drop(drop_desc),      drop(drop_desc)],
  #sunken steps
  al[15][a]: [drop(drop_desc),    (f"{al[14][a]} s"),  (f"{al[16][a]} e"),   (f"{al[19][a]} w")],
  #marshlands
  al[16][a]: [drop(drop_desc),    drop(drop_desc),     drop(drop_desc),      drop(drop_desc)],
  #docks
  al[17][a]: [drop(drop_desc),    drop(drop_desc),     (f"{al[5][a]} e"),    (f"{al[18][a]} w")],
  #boat escape
  al[18][a]: [drop(drop_desc),    drop(drop_desc),     drop(drop_desc),      drop(drop_desc),],
  #forest path
  al[19][a]: [drop(drop_desc),    drop(drop_desc),     (f"{al[15][a]} e"),   (f"{al[12][a]} w")],
  #caught
  al[20][a]: [drop(drop_desc),    drop(drop_desc),     drop(drop_desc),      drop(drop_desc),],
  #Decrepit tower
  al[21][a]: [drop(drop_desc),    drop(drop_desc),     drop(drop_desc),      drop(drop_desc),],
  #staying in same location
  al[22][a]: [(f"{al[22][a]} n"),  (f"{al[22][a]} s"), 
               (f"{al[22][a]} e"), (f"{al[22][a]} w")]
}

#creating window
root = tk.Tk()
root.geometry("550x450")
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

txts = {
   "start":"You're travelling away from your homeland Plasnamesrehard, "
   "the journey has been hard... yet you persist.. taking a different, "
   "route than that of your fellow refugees to better your odds of, "
   "remaining invisible to the dark wizards whom hunt your people out, "
   "of an old grudge your forefathers held.\n They posses magicks honed, "
   "to find most beings, yet solo, scruffy travellers become too far, "
   "below their notice."
}
#start sequence 
def start_screen():
   update_gui(txt=txts["start"])
start_screen()
#first move screen
#ca=current area
ca = al[area_no['num']][a]
update_gui(txt=(
    f"\nYou're in the {ca}\n"
    f"To your North is {paths_dict[ca][0][:-2]}\n"
    f"South is {paths_dict[ca][1][:-2]}\n"
    f"To your East is {paths_dict[ca][2][:-2]}\n"
    f"The west sunset lights the {paths_dict[ca][3][:-2]} in that direction"
), index=0)

pos_actions = {
   "north": ["nth", "northh"],
   "south": ["sth", "ssouth"],
   "east": ["est", "esst"],
   "west": ["wst", "wstt"]
}
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
  elif input == "letsgo":
    move("stay", area_no, paths_dict)

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
    print("no u cant go that way theres a wall or smth")
# Start the Tkinter event loop
root.mainloop()
