#name of npc being interacted with
npcname = "Coral"

def npctalk(npcname):
    #npc dialogue options
    npctext = {
    "Coral": ["hello", "oh hi, it's you again"],
    "Persephone": ["beware small creature, leave if you value your life", "you won't last long here"]
    }
    #counting number of interactions per npc
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
    "z": "🥀"
    }

    #finding correct npc message

    npcmsg = npctext[npcname][npcintercnt[npcname]]
    npcmsg = npcmsg.lower()
    #do smth if out of range


    #turns input text into emoji translate
    for i in range(len(npcmsg)):
        print(converter[npcmsg[i]], end = " ")

npctalk(npcname)
