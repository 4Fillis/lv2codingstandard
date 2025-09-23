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

#add 5 space or _ characters after each description as removed later when error handling
#all drop descrrptions must begin with drop, for error handling
drop_desc = ["drop, a very long drop.._____", "drop, just nothing.._____", "drop, just empty space.._____"]
area_no = {"num": 0}

#Variables : AREAS
#use variables to show in what direction there is no path

def drop(drop_desc):
   desc = random.choice(drop_desc)
   return desc


#messages for key game points
txts = {
   "start":"You were travelling back to your home in Plasnamesrehard.\n"
   "After going out to buy groceries, you got stuck in the sky a while ago\n"
   "when a natural disaster lauched part of the old city into the sky\n"
   "you've been camping up here a couple days and have decided\n"
   "to try and get home as your grocieries will go bad if you do not.\n"
   "\nClick the appearing message text to speed up it's appearance"
   "\n\n Type in the direction you wish to travel,\n your goal "
   "is to escape this floating complex you're on, goodluck"
}


#areas list with key numbers + description 
al = {
    0:  {"area": "your old camp",
         'desc': "your old campsite, there's not much here\n"},

    1:  {"area": "a hiding place",
         'desc': "a small hollow beneath the roots of a cherry \ntree near your old camp\n"},

    2:  {"area": "old beige balcony",
         'desc': "a dusty yet open beige tiled balcony\n"},

    3:  {"area": "blue stairs",
         'desc': "faded blue stairs inscribed with patterns in\na language you can't translate\n"},

    4:  {"area": "broken wood path",
         'desc': "an old worn path made of splintering wood planks\n"},

    5:  {"area": "cloth opening",
         'desc': "a gap in the faded purple cloth of an old shopfront,\njust small enough to fit through\n"},

    6:  {"area": "light blue pavlivion",
         'desc': "an old vine-covered light blue pavlivion \nstill standing despite it's cracks\n"},

    7:  {"area": "old train station",
         'desc': "a terminal with some benches, \nthey're very old and worn, breaking apart\n"},

    8:  {"area": "clearing",
         'desc': "a standing circle of stones surrounding \nthousands of tiny red-white mushrooms\n"},

    9:  {"area": "Gelatinous River",
         'desc': "a thick gooey river made of some substance\n"},

    10: {"area": "Gelatinous Pool",
         'desc': "a circular pool of this gooey semi transparent substance\n"},

    11: {"area": "Marshlands",
         'desc': "\nfeilds of marshy wetland caked in a thick fog\n"},

    12: {"area": "old docks",
         'desc': "\ndecrept wooden planks stretching \ninto the mist\n"},

    13: {"area": "old boat",
         'desc': "\na small wooden boat apparently \nabandoned an age ago\n"},

    14: {"area": "Wasteland",
         'desc': "\nbleak scorched earth covered \nin ash and burnt gravel\n"},

    15: {"area": "Decrepit Tower",
         'desc': "\nan old yet proud building \nspiralling into the sky\n"}
}

a = "area"
#possible paths from _each location
paths_dict = {
   #               _north             _south            _east             _west
    # Your old camp
    al[0][a]: [f"{al[2][a]} ~0;n", drop(drop_desc), drop(drop_desc), f"{al[1][a]} ~3;w"],

    # Hiding Place
    al[1][a]: [drop(drop_desc), drop(drop_desc), f"{al[0][a]} ~2;e", drop(drop_desc)],

    # Vanilla Plateau
    al[2][a]: [drop(drop_desc), f"{al[0][a]} ~1;s", f"{al[6][a]} ~2;e", f"{al[3][a]} ~3;w"],

    # DiamondStaircase
    al[3][a]: [drop(drop_desc), drop(drop_desc), f"{al[2][a]} ~2;e", f"{al[4][a]} ~3;w"],

    # Broken Path to Docks
    al[4][a]: [f"{al[5][a]} ~0;n", drop(drop_desc), f"{al[3][a]} ~2;e", f"{al[12][a]} ~3;w"],

    #_SecretExit
    al[5][a]: [f"{al[8][a]} ~0;n", f"{al[4][a]} ~1;s", drop(drop_desc), drop(drop_desc)],

    # Blue-White Pavilion
    al[6][a]: [drop(drop_desc), drop(drop_desc), f"{al[7][a]} ~2;e", f"{al[2][a]} ~3;w"],

    #_Station
    al[7][a]: [f"{al[9][a]} ~0;n", drop(drop_desc), f"{al[11][a]} ~2;e", f"{al[6][a]} ~3;w"],

    # Gelatinous River
    al[9][a]: [f"{al[8][a]} ~0;n", f"{al[7][a]} ~1;s", drop(drop_desc), drop(drop_desc)],

    # Gelatinous Pool
    al[10][a]: [f"{al[8][a]} ~0;n", f"{al[7][a]} ~1;s", drop(drop_desc), drop(drop_desc)],

    # Docks
    al[12][a]: [drop(drop_desc), drop(drop_desc), f"{al[4][a]} ~2;e", f"{al[13][a]} ~3;w"],

    # Marshlands (ending)
    al[11][a]: "ending",

    # Boat (ending)
    al[13][a]: "ending",

    # Woods Ghost (ending)
    al[8][a]: "ending",

    # Wasteland (ending)
    al[14][a]: "ending",

    # Old Tower (ending)
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
   start_moves = (
    f"\nYou're in the {ca}\n"
    f"To your North: {paths_dict[ca][0][:-5]}\n"
    f"To your South: {paths_dict[ca][1][:-5]}\n"
    f"To your East:  {paths_dict[ca][2][:-5]}\n"
    f"To your West:  {paths_dict[ca][3][:-5]}")
   update_gui(txt=f"{txts['start']}\n{start_moves}", index=0)

#function to check direction user is moving to is valid
def check_dirvalid(paths_list):
    # direction, number in paths_dict directions and short letter version for checking
    dirs = {
        "north": (0, "n"),
        "south": (1, "s"),
        "east":  (2, "e"),
        "west":  (3, "w"),}
    valid_dirs = []
    #loop through all directions to check if valid or drop
    for dir, (idx, initial) in dirs.items():
        all_paths = paths_list[idx]
        
        #remove drop descriptions from valid directions
        if all_paths.startswith("drop"):
            continue
        #use ending string to check dirs are actual dirs
        ider = f"~{idx};{initial}"
        if all_paths.endswith(ider):
            valid_dirs.append(dir)       
    return valid_dirs
  
#functin to display error msg
def error_msg(valid_acts, input):
    error_txt = "\n\n" +"Apologies!\n" \
    f"You cannot input '{input}'\n Valid inputs are: {valid_acts}.\n" 
    "Please try again..."

    ct = game_txt.cget("text")
    error_start = ct.find("Apologies")
    #if error message being displayed already
    if error_start != -1:
        ct = ct[:error_start].rstrip()
    update_gui(txt=(ct + error_txt), index=0, txt_done=txt_done, 
    skip=True)
    input_bar.delete(0, tk.END)
    return 

#function to to change the users area and display new area details
def move(going_to, name_number, area_no, paths_dict):
    a = 'area'
    # gets what area you're in / number
    ca_no = area_no["num"]
    ca = al[ca_no][a]

    # direction -> place in paths list
    dirs_num = {
        "north": 0,
        "south": 1,
        "east": 2,
        "west": 3,
    }
    # finds place name
    dir_no = dirs_num[going_to]
    place_go = paths_dict[ca][dir_no][:-5]

    #checks if place_go is an area or not
    if place_go not in name_number:
        paths_opts = paths_dict[ca]
        valid_acts = check_dirvalid(paths_opts)
        error_msg(valid_acts, going_to)
    
    #gets area number from area name : number dict
    area_no["num"] = name_number[place_go]
    movn = f"You move {going_to} to {place_go}."

    go = {
      "north": paths_dict[al[area_no['num']][a]][0][:-5],
      "south": paths_dict[al[area_no['num']][a]][1][:-5],
      "east": paths_dict[al[area_no['num']][a]][2][:-5],
      "west": paths_dict[al[area_no['num']][a]][3][:-5]
    }
    #areas in each direction
    moves = (
    f"\nTo your North: {go['north']},\n"
    f"To your South: {go['south']},\n"
    f"East: {go['east']},\n"
    f"West: {go['west']}."
    )
    #update current area number
    ca_no = area_no["num"]
    ca = al[ca_no]["area"]
    # If at an endpoint
    if "ending" == paths_dict[ca]:
        newarea_desc = (f"you carfully jump down to the {al[ca_no]['desc']}")
        update_gui(
            txt = (
            f"Congrats :), You found a path out of the sky.\n"
            f"\n{newarea_desc} and onto solid ground once more,\n"
            "Consider your groceries saved from going old\n"
            "Thank you for playing."),
            index=0
        )
        input_bar.destroy()
        input_button.destroy()
        entry_frame.destroy()
        input_msg.destroy()
        return
    

    newarea_desc = f"\n it's {al[ca_no]['desc']}\n"
    
    #update screen
    update_gui(
    txt=movn + newarea_desc + moves, index=0,
    txt_done=txt_done, skip=False)
    return ca
    

#Takes user input and clears input bar
def user_input(paths_dict, event=None):
    ca_no = area_no['num']
    ca = al[ca_no]['area']
    input = input_bar.get().strip()
    input = input.lower()
    #creates dict of area name : id number
    name_number = {value[a]: key for key, value in al.items()}
    paths_opts = paths_dict[ca]
    valid_acts = check_dirvalid(paths_opts)
    if input not in valid_acts:
        error_msg(valid_acts, input)
        return
    
    input_bar.delete(0, tk.END)
    move(input, name_number, area_no, paths_dict)

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
input_bar.bind("<Return>", lambda event: user_input(paths_dict, event))

input_button = tk.Button(
    root,
    text="Move",
    #uses lambda function to send ca and paths_dict to function
    command=lambda: user_input(paths_dict, event=None),
    bg=bg_clr, #background color
    fg=btn_txt_clr, #text color
    activebackground=btn_press_bg, #color change when pressed
    font=(font, fontsize, "bold"))
#button space 10 above, 20 below
input_button.pack(pady=(10, 20))


start_screen()
# Start the Tkinter event loop
root.mainloop()