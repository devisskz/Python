# coding: utf-8
#
# hw0pr10.py
#

""" 
Title for your adventure:   The Quest.

Notes on how to "win" or "lose" this adventure:
  To win, choose the table.
  To lose, choose the door.

"""

import time

def adventure():
    """ this function runs one session of interactive fiction
        Well, it's "fiction," depending on the pill color chosen...
        inputs: no inputs    (prompted text doesn't count as input)
        outputs: no outputs  (printing doesn't count as output)
    """
    delay = 2.0          # change to 0.0 for testing/speed runs; larger for dramatic effect!

    username = input("Peace be upon you my friend, what is your name?")
    
    if username == "parker":
        print("Parker of Alexandria? I heard a lot about you...")
    time.sleep(delay)
    print()
    print("Nice to meet you", username, ",I think it's time we head out towards the desert..")
    time.sleep(delay)
    print("Get on the camel, we are on our hunt for the treasures of the Pharaohs!")
    print()
    time.sleep(delay)
    print("Thousands have failed to reach them, because first we have to get through the traps in the Tomb of Khafre?")
    print()
    time.sleep(delay)
    answer1 = input("Do you know anything about the tombs of the Pharaohs? [yes/no]")
    if answer1 == "yes":
        print("Great, then you know how dangerous our quest is..")
    elif answer1 == "no":
        print("Well, you have a lot to learn!")
    else:
        print("I'll consider that as a yes..")
    print()
    time.sleep(delay)
    print("There! a pyramid in the distance!\n")
    print("What a creation, words can not describe...")
    print("I think I see an entrance, follow me!")
    time.sleep(delay)
    print("So dark, I can not see anything.. Light up the torch!")
    time.sleep(delay)
    print("I see a way down the stairs, go, I will follow you")

    answer2 = input("Go First? [yes/no]")
    if answer2 =="yes":
        print()
        print("Brave soul!")
    elif answer2 =="no":
        print("You coward, why did I even take you with me?")
    time.sleep(delay)

    print()
    print("As you come down the stairs, you see")
    print("Two paths.. Which one do you choose?")

    answer3 = input(" [right/left] ")
    print()

    if answer3 == "right":
        print("As you walk, a hundred of deadly scorpions appear in front of you")
        time.sleep(delay)
        print()
        print("Run, Run back!")
        print("Lets go the other way...")
        print("You walk forward in darkness, on perfectly polished sandstone blocks..")
        print("When suddenly, you see a dot of light in front of you..")
        time.sleep(delay)
        print("Could this be it.. The tomb of Khafre?")
        time.sleep(delay)
        print("As you approach closer")
        print("You see that the light is coming from a small gap in one of the sandstones")
        time.sleep(delay)
        print("As you squeeze your way through the gaps, you realize what a beauty have you reached..")
        time.sleep(delay)
        print("Oh no! You were so blinded by the treasures you saw around that you accidentally opened the coffin, releasing the soul of Khafre...")
        time.sleep(3)
        print("His soul is indignant and ready to thwart anyone who entered his tomb")
        time.sleep(delay)

    else:
        print()
        print("You walk forward in darkness, on perfectly polished sandstone blocks")
        print("When suddenly, you see a dot of light in front of you..")
        time.sleep(delay)
        print("Could this be it.. The tomb of Khafre?")
        time.sleep(delay)
        print("As you approach closer")
        print("You see that the light is coming from a small gap in one of the sandstones")
        time.sleep(delay)
        print("As you squeeze your way through the gaps, you realize what a beauty have you reached..")
        time.sleep(delay)
        print("Oh no! You were so blinded by the treasures you saw around that you accidentally opened the coffin, releasing the soul of Khafre...")
        time.sleep(3)
        print("His soul is indignant and ready to thwart anyone who entered his tomb")
        time.sleep(delay)
            
    answer4 = input("There are three weapons you have with you, choose one and defend yourself from the brutish soul? [spear/sword/scepter]")
    if answer4 == "spear":
                print("The spear made from metal of the mortals can not penetrate through the Pharaohs")
                print("You have chosen the wrong weapon and soul of Khafre has defeated you...")
    elif answer4 == "sword":
                print("The sword made from metal of the mortals can not penetrate through the Pharaohs")
                print("You have chosen the wrong weapon and soul of Khafre has defeated you...")
    elif answer4 == "scepter":
                print("The scepter appears to be from the world of the dead, it can send the souls back with a single touch")
                print()
                print("Great job", username, "! you have completed the quest and became the richest person of Ptolematic Egypt!")