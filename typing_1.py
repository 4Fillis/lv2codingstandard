import random 
#INSULT GENERATOR
insults1 = ["jam", "bird", "weak", "annoying", "underbaked", "peirced"]
insults2 = ["brained", "filled", "bag of", "limbed"]
insults3 = ["fool", "child", "elderich horror", "skin"]

def generate_insults(insults1, insults2, insults3):
  i1 = random.choice(insults1)
  i2 = random.choice(insults2)
  i3 = random.choice(insults3)
  insult = i1 + " " + i2 + " "+ i3
  return(insult)


#AREAS
#use variables to show in what direction there is nothing
f = "n/a f"
l = "n/a l"
r = "n/a r"
b = "n/a b"
#areas list with key numbers
al = [{0:"hospital room"}, {1:"bathroom"}, {2:"rainbow door"}, {3:"sea themed hallway"},
{4:"stairs"}, {5:"seaweed farm"}, {6:"side door"}, {7:"carparkl"},
{8:"minnie mouse hallway"}, {9:"nurses office"}, {10:"mickey mouse hallway"}, {11:"childrens ward"},
{12:"elevator down"}, {13:"bakery"}, {14:"outside"}, {15:"carparkr"}, {16:"End"}
]

#to edit paths in each al[a][a] a is the index number from the al list, add location and
#change where it connects
paths_dict = {
  #area   forwards                 left                right      backwards
  al[0][0]: [(f"{al[2][2]} f"),   (f"{al[1][1]} l"),   r,                  b],
  al[1][1]: [f,                    l,                  r,                  (f"{al[0][0]} b")],
  al[2][2]: [f,                   (f"{al[3][3]} l"),   (f"{al[8][8]} l"),  (f"{al[0][0]} b")]
}
print(paths_dict)
