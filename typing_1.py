import random 

insults1 = ["jam", "bird", "weak", "annoying", "underbaked", "peirced"]
insults2 = ["brained", "kneed", "bag of", "limbed"]
insults3 = ["fool", "child", "elderich horror", "skin"]

def generate_insults(insults1, insults2, insults3):
  i1 = random.choice(insults1)
  i2 = random.choice(insults2)
  i3 = random.choice(insults3)
  insult = i1 + " " + i2 + " "+ i3
  return(insult)

print(generate_insults(insults1, insults2, insults3))