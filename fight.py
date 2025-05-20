#fighting fight
from random import *

npcs = {
  #   name       stature         wearing            action                where                 pronouns   friendship interest / 10
  1:["Coral", "small woman", "pink lab coat", "mixing chemicals", "on a table in the corner", "she", "her", 9],
  2:["Persephone", "tall dark woman", "black mechanics fit", "engineering something in the cogswork", "under a vicious looking copper machine", 4],
  3:["3", "small woman", "pink lab coat", "kind"],
  4:["4", "small woman", "pink lab coat", "kind"],
  5:["5", "small woman", "pink lab coat", "kind"],
  6:["6", "small woman", "pink lab coat", "kind"],
  7:["7", "small woman", "pink lab coat", "kind"],
  8:["8", "small woman", "pink lab coat", "kind"],
}

#dict of health n stuff
health = {
    "bread":0,
    "Coral":5,
    "user":3,
    "clam":2
}

#variables
interaction = "Coral"

fightchoices = ['rock', 'paper', 'scissors']
bodyparts = {
    "left arm": "hits", 
    "right arm": "scratches", 
    "left leg": "lower body", 
    "right leg": "lower body", 
    "head": "yanks", 
    "eyeball": "pokes",
    "stomach": "pushes", 
    "shin": "bruises"
}

#sequence for fighting
def fightsequence(interaction):
    user = input(f"Would you like to: {fightchoices[0]}, {fightchoices[1]}, or {fightchoices[2]}")
    npc = fightchoices[randint(0, 2)]
    print(f"npc choice is {npc}")

    while health[user] > 0:
        if npc == user:
            print(f"you both try to {user}. Nothing happens.")
        #if npc wins
        elif fightchoices.index(npc) == (fightchoices.index(user) -1):
            print(f"{interaction} {random.choice(bodyparts)}")


#fight function
def fight(interaction):
    if interaction in npcs:
        print(f"you decide to fight {interaction}")
        fightsequence(interaction)
    else:
        print("cant fight this thing")
    fightsequence(interaction)


#if useraction == "fight":
#    fight(interaction)

fight(interaction)
