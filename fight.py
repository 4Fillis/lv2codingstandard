#fighting fight
from random import randint
fightchoices = ['paper', 'scissors', 'rock']

#dict of health n stuff
health = {
    "bread":0,
    "human":5,
    "user":3,
    "clam":2
}

#variables
interaction = "bread"

#sequence for fighting
def fightsequence(interaction):
    user = input(f"Would you like to: {fightchoices[1]}, {fightchoices[2]}, or {fightchoices[3]}")
    npc = fightchoices[randint(0, 2)]
    while health[user]
    if npc == 
    if npc == 'paper' and user == 'rock':
        print("youlose")

#fight function
def fight(interaction):
    if interaction in npcs:
        print(f"you decide to fight {interaction}")
        fightsequence(interaction)


if useraction == "fight":
    fight(interaction)
