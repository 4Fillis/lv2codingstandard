#function to encrypt the npcs text so it and the code is easily changable

#dictionaries
from random import randint

#name of npc being interacted with
npcname = "Coral"

def npctalk(npcname):
    #npc dialogue options INSERT MORE
    #INSERT MORE NPCS
    npctext = {
    "Coral": [" hello1", 'oh hi its you again'],
    "Persephone": ["beware small creature leave if you value your life", "you wont last long here"]
    }
    #counting number of interactions per npc 
    #INSERT MORE NPCS
    npcintercnt = {
        "Coral": 0,
        "Persephone": 0
    }

    #dictionary with english letters and npc equivilent
    converter = {
    "a": "🎬",
    "b": "☣️",
    "c": "🎥",
    "d": "🕊️",
    "e": "✝️",
    "f": "⚜️",
    "g": "🏳️‍🌈",
    "h": "⛧",
    "i": "☪️",
    "j": "🔪",
    "k": "💋",
    "l": "🤟",
    "m": "🕌",
    "n": "🧿",
    "o": "🅾️",
    "p": "🙏",
    "q": "👑",
    "r": "🛐",
    "s": "⛤",
    "t": "📺",
    "u": "👉",
    "v": "💣",
    "w": "👁️",
    "x": "🔪",
    "y": "🌻",
    "z": "🥀",
    " ": " ⎛⎝ ≽ ^ ⩊ ^ ≼ ⎠⎞",
    "1": "1️⃣",
    "2": "2️⃣",
    "3": "3️⃣",
    "4": "4️⃣",
    "5": "5️⃣",
    "6": "6️⃣",
    "7": "7️⃣",
    "8": "8️⃣",
    "9": "9️⃣", 
    "0": "0️⃣"
    }

    #unless first interaction, randomise response within npctext list
    if npcintercnt[npcname] < 1:
        npcmsg = npctext[npcname][0]
    else:
        npcmsg = npctext[npcname][randint(0, (len(npctext[npcname]))-1)]

    npcmsg = npcmsg.lower()

    #turns input text into emoji translate
    for i in range(len(npcmsg)):
        print(converter[npcmsg[i]], end = " ")

npctalk(npcname)