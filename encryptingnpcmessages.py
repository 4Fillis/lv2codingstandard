npctext = "example"
npctext = npctext.lower()

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

def encodemsg(npcmsg):
    for i in range(len(npctext)):
        print(converter[npctext[i]], end = " ")