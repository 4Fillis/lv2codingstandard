
hp = 10

#function to check players hp
def healthcheck(hp):
    
    #10 is max hp, buff items could bring beyond
    if hp >= 10:
        print("Oh you feel fine, good in fact,"
              " the voices in your head tells you to forge onwards")

    #increments, messages based on hp %
    elif hp >= 8:
        print(f"you can still feel ")
    elif hp >= 5:
        print(f"you are.... ok .... not great ... but ok, \n"
              "some scratches on your arm are still bleeding...")
    elif hp >= 1:
        print(f"you can feel you're wounds draining your life\n"
              "the voice in your head tells you not to continue"
              "\n....\nnot sure if it'll kill you")
    else:
        print("you collapse on the ground as you're wounds prove too much to handle")
        #INSERT RESTART FUNCTION

    #INSERT OPTION TO DRINK HEALTH POTION

healthcheck(hp=2)
