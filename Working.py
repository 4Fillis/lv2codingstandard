'''program for a basic escape game for python programming standard lv2'''
'''uses tkinter GUI with input of direction moving to move user through areas to escape the floating island complet they're on'''

#working document
import tkinter as tk
from functools import partial
import random

#main colors for gui
txt_clr = "#0e021b" #main text highlight color
txtbg_bar_clr = "#e3d5f1" #input bar bg
txt_bar_clr = "#390846" #user input text color
bg_clr = "#C0B738" #main text color
btn_press_bg = "#C0B738"
btn_txt_clr = "#2E2E2B"
font = "OpenDyslexic"
fontsize = 12

#last letters of string cannot contain any of action letters (nsew)
drop_desc = ["....empty air... "]

#Variables : AREAS
#use variables to show in what direction there is no path

def drop(drop_desc):
   desc = random.choice(drop_desc)
   return desc
area_no = {"num": 0}

#messages for key game points
txts = {
   "start":"You're travelling away from your homeland Plasnamesrehard,\n"
   "the journey has been hard... \nyet you persist.. taking a different "
   "route \nthan that of your fellow refugees to better your odds \nof "
   "remaining invisible to the dark wizards who hunt \nyour people out "
   "of an old grudge your forefathers held.\n They posses magicks honed "
   "to find most beings, \nyet solo, scruffy travellers \nare too far, "
   "below their notice.\n\n Input direction you wish to travel,\n your goal "
   "is to escape this floating complex you're on, goodluck",
   "ending1":"you"
}


#areas list with key numbers + description + relevant btns
al = {
    0:  {"area": "your old camp",
         "desc": "your old campsite, there's not much here"},

    1:  {"area": "a hiding place",
         "desc": "a small hollow beneath the roots of a cherry \ntree near your old camp"},

    2:  {"area": "old beige balcony",
         "desc": "a dusty yet open beige tiled balcony"},

    3:  {"area": "blue stairs",
         "desc": "faded blue stairs inscribed with patterns, \na language you can't translate"},

    4:  {"area": "broken wood path",
         "desc": "an old worn path made of splintering wood planks"},

    5:  {"area": "cloth opening",
         "desc": "a gap in the faded purple cloth of an old shopfront,\njust small enough to fit through"},

    6:  {"area": "light blue pavlivion",
         "desc": "an old vine-covered light blue pavlivion \nstill standing despite it's cracks"},

    7:  {"area": "old train station",
         "desc": "a terminal with some benches, \nthey're very old and worn, breaking apart"},

    8:  {"area": "clearning",
         "desc": "a standing circle of stones surrounding \nthe half-corporal form of a being"},

    9:  {"area": "Gelatinous River",
         "desc": "a thick gooey river made of some substance"},

    10: {"area": "Gelatinous Pool",
         "desc": "a circular pool of this gooey semi transparent substance"},

    11: {"area": "Marshlands",
         "desc": "feilds of marshy wetland caked in a thick fog"},

    12: {"area": "Docks",
         "desc": "decrept wooden planks stretching \ninto the mist"},

    13: {"area": "Boat",
         "desc": "a small wooden boat apparently \nabandoned an age ago"},

    14: {"area": "Wasteland",
         "desc": "bleak scorched earth covered \nin ash and burnt gravel"},

    15: {"area": "Decrepit Tower",
         "desc": "an old yet proud building \nspiralling into the sky"}
}

a = "area"
#Where each location goes
paths_dict = {
   #               north             south            east             west
    # Your old camp
    al[0][a]: [f"{al[2][a]} n", drop(drop_desc), drop(drop_desc), f"{al[1][a]} w"],

    # Hiding Place
    al[1][a]: [drop(drop_desc), drop(drop_desc), f"{al[0][a]} e", drop(drop_desc)],

    # Vanilla Plateau
    al[2][a]: [drop(drop_desc), f"{al[0][a]} s", f"{al[6][a]} e", f"{al[3][a]} w"],

    # Diamond Staircase
    al[3][a]: [drop(drop_desc), drop(drop_desc), f"{al[2][a]} e", f"{al[4][a]} w"],

    # Broken Path to Docks
    al[4][a]: [f"{al[5][a]} n", drop(drop_desc), f"{al[3][a]} e", f"{al[12][a]} w"],

    # Secret Exit
    al[5][a]: [f"{al[8][a]} n", f"{al[4][a]} s", drop(drop_desc), drop(drop_desc)],

    # Blue-White Pavilion
    al[6][a]: [drop(drop_desc), drop(drop_desc), f"{al[7][a]} e", f"{al[2][a]} w"],

    # Station
    al[7][a]: [f"{al[9][a]} n", drop(drop_desc), f"{al[11][a]} e", f"{al[6][a]} w"],

    # Gelatinous River
    al[9][a]: [f"{al[8][a]} n", f"{al[7][a]} s", drop(drop_desc), drop(drop_desc)],

    # Gelatinous Pool
    al[10][a]: [f"{al[8][a]} n", f"{al[7][a]} s", drop(drop_desc), drop(drop_desc)],

    # Docks
    al[12][a]: [drop(drop_desc), drop(drop_desc), f"{al[4][a]} e", f"{al[13][a]} w"],

    # Marshlands (ending)
    al[11][a]: "end point",

    # Boat (ending)
    al[13][a]: "ending",

    # Woods Ghost (ending)
    al[8][a]: "ending",

    # Wasteland (ending)
    al[14][a]: "ending",

    # Decrepit Tower (ending)
    al[15][a]: "ending",
}

#setting current area
ca = al[area_no['num']][a]

#creating window
root = tk.Tk()
root.geometry("700x620")
root.title("Python Standard - ELLM")
root.configure(bg=txt_clr) #background color

#doing background
bg_img = tk.PhotoImage(file="resources/satin_purple.png")
bg_label = tk.Label(root, image=bg_img)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)


#game text
game_txt = tk.Label(
    root,
    text="",
    bg=txt_clr, #gui background
    fg=bg_clr, #text color
    font=(font, fontsize, "bold")
)
#padding above, below
game_txt.pack(pady=(20, 5))

txt_done = [None] #list so changeable in function
#ending typing 
def tpg_end(root, txt_done):
  if txt_done[0] is not None:
     root.after_cancel(txt_done[0])
     txt_done[0] = None

#skip typing effect
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
   start_moves = f"\nYou're in the {ca}\n"f"To your North: {paths_dict[ca][0][:-2]},\n"f"South: {paths_dict[ca][1][:-2]}\n"f"To the East: {paths_dict[ca][2][:-2]}\n"f"and West: {paths_dict[ca][3][:-2]}"
   update_gui(txt=txts["start"] + f"\n{start_moves}" +"", index=0)


def move(going_to, area_no, paths_dict):
    a = 'area'
    # gets what area you're in / number
    ca_no = area_no["num"]
    ca = al[ca_no]["area"]

    pos_places = paths_dict.get(ca)
    print(pos_places)

    # direction -> place in paths list
    dirs_num = {
        "north": 0,
        "south": 1,
        "east": 2,
        "west": 3,
    }
    # finds place name
    dir_no = dirs_num[going_to]
    place_go = pos_places[dir_no]
    print(f"place go {place_go}")

    place_go = paths_dict[ca][dir_no][:-2]

    #dict of area name by area number from al dict
    name_number = {value[a]: key for key, value in al.items()}
    area_no["num"] = name_number[place_go]
    
    movn = f"You move {going_to} to {place_go}."
    go = {
      "north": paths_dict[al[area_no['num']][a]][0][:-2],
      "south": paths_dict[al[area_no['num']][a]][1][:-2],
      "east": paths_dict[al[area_no['num']][a]][2][:-2],
      "west": paths_dict[al[area_no['num']][a]][3][:-2]
    }
    moves = f"\nTo your North is {go['north']}, \nTo your South is {go['south']}, "f"\nEast there's {go['east']}, \n To your West is {go['west']}."
    #update current area number
    ca_no = area_no["num"]
    ca = al[ca_no]["area"]
    pos_places = paths_dict.get(ca)
    print(f"new {pos_places}")
    # If this is an ending point
    if "ending" in pos_places:
        update_gui(
            txt=f"You've reached an ending, eascaping the floating islands'\n"
                "Thanks for playing!",
            index=0
        )
        input_bar.destroy()
        input_button.destroy()
        entry_frame.destroy()
        input_msg.destroy()
        return
    # ADD END SCREEN CHECK WHICH ENDING

    newarea_desc = "\n it's " + al[ca_no]["desc"] + "\n"
    
    #update screen
    update_gui(txt=movn + newarea_desc + moves, index=0, txt_done=txt_done, skip=False)
    return ca
    

#Takes user input and clears input bar
def user_input(ca, paths_dict, event=None):
    input = input_bar.get()
    input = input.lower()
    valid_actions = ['north', 'south', 'east', 'west']
    if paths_dict[ca][0][-2:] != ' n':
       valid_actions.remove('north')
    if paths_dict[ca][1][-2:] != ' s':
       valid_actions.remove('south')
    if paths_dict[ca][2][-2:] != ' e':
       valid_actions.remove('east')
    if paths_dict[ca][3][-2:] != ' w':
       valid_actions.remove('west')
    #give error message if invalid direction
    if input not in valid_actions:
       error_msg = "\n\n" +"Apologies!\n" \
       f"You cannot input '{input}'\n Valid inputs are: {valid_actions}.\n" 
       "Please try again..."
       ct = game_txt.cget("text")
       error_start = ct.find("Apologies!")
       if error_start != -1:
            ct = ct[:error_start].rstrip()
       update_gui(txt=(ct + error_msg), index=0, txt_done=txt_done, 
       skip=True)
    input_bar.delete(0, tk.END)
    move(input, area_no, paths_dict)

#input message
input_msg = tk.Label(
    root,
    text="Where do you wish to go?",
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
    bg=txtbg_bar_clr, #input box bg color
    fg=txt_bar_clr, #text color
    font=(font, fontsize, 'bold')
)
input_bar.pack()
#uses lambda to use function with specs in brackets
input_bar.bind("<Return>", lambda event: user_input(ca, paths_dict, event))

input_button = tk.Button(
    root,
    text="Move",
    #uses lambda function to send ca and paths_dict to function
    command=lambda: user_input(ca, paths_dict, event=None),
    bg=bg_clr, #background color
    fg=btn_txt_clr, #text color
    activebackground=btn_press_bg, #color change when pressed
    font=(font, fontsize, "bold"))
#button space 10 above, 20 below
input_button.pack(pady=(10, 20))


start_screen()
# Start the Tkinter event loop
root.mainloop()
