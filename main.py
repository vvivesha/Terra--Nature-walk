print("Welcome to the Interactive Nature Game, where you will be expected to solve a mystery!")
print("...")
import time
game_status = "pending"
mode_error = "no"
game_mode = "incomplete"
time.sleep(1)
print("It\'s now time to select your game mode! There are 2: NORMAL and DIFFICULT. Please indicate which you\'d like to use!' ")
time.sleep(1)

#game mode selection:

mode = input("Would you like to try DIFFICULT or NORMAL mode?  ")
  #might be the error (1)
if mode not in {"normal", "NORMAL", "difficult", "DIFFICULT"}:
    game_mode = "invalid"
    if game_mode == "invalid":
        print("<Player has requested an *invalid* " + mode + " mode>")
if mode == "normal" or "NORMAL" or "difficult" or "DIFFICULT":
        game_mode = "done"
        mode_error = "no"
        if game_mode == "done":
            print("Moving on...")
if mode == "NORMAL" or "normal":
    game_mode = "done"
    mode_error = "no"
    print("<Player typed " + mode + " mode>")
if mode_error == "no":
    print("...")
    time.sleep(1)
if game_mode == "done":
        time.sleep(0.5)
        print("configuring...")

#normal above, difficult below.


while mode != "NORMAL" or "normal" or "DIFFICULT" or "difficult":
    if game_mode == "invalid":
        print("error is here!!")
#maybe worked; use "break" cmd rather than "continue" cmd...?
        mode_error == "yes"
    if mode == "NORMAL" or "normal" or "DIFFICULT" or "difficult":
        mode_error == "no"
    if mode_error == "no":
        game_status = "active"
        break


    elif mode not in ["NORMAL" or "normal" or "DIFFICULT" or "difficult"]:
        mode_error = "yes"
        if mode_error == "yes":
            print("Please select a valid gamemode: NORMAL or DIFFICULT.")
            print("...")
            time.sleep(0.5)
            mode = input('''Which gamemode would you like to try out?  ("DIFFICULT"/"NORMAL")''')
    while mode != "NORMAL" or "normal" or "DIFFICULT" or "difficult":
        attempt = 1
        if game_mode == "done":
            break
        while attempt < 2:
            if game_mode == "done":
                break
            attempt += 1
        if attempt == 2:
            break

#error  is somewhere around here!!

    if mode == "normal" or "NORMAL":
        print(mode + " mode selected.")
        time.sleep(0.5)
        print("loading...")
    if mode == "difficult" or "DIFFICULT":
        print(mode + " mode selected.")
        time.sleep(0.5)
        print("loading...")
    if mode_error == "yes":
        time.sleep(0.5)
        for i in range(4):
            print(" ")
        print("<Please supply a game mode in order to play the game.>")
        for i in range(4):
            print(" ")
        time.sleep(0.5)


if game_mode == "done":
    time.sleep(0.5)
    print("please wait a moment...")
if mode == "DIFFICULT" or "difficult":
    game_mode = "done"
    mode_error == "no"
if mode_error == "no":
    print("...")
    time.sleep(1)
    print(mode + " mode has successfully been selected!")
    time.sleep(0.5)
    print("Goodluck.")
    time.sleep(0.5)
    print("...")
if game_mode == "done":
    time.sleep(0.5)
    print("We\'re almost done!")

#bottom of the working code ^




if game_mode == "done":
    time.sleep(0.5)
    print("...")
    #break

#no "break" needed following the above "if" segment..?
if mode not in ["normal" or "NORMAL" or "difficult" or "DIFFICULT"]:
    print("<An error has been detected. We\'re sorry!>")
if mode_error == "no":
    if mode == "NORMAL" or "normal":
        mode_error == "no"
        print("...")
        time.sleep(1)
        print("Tip: You might be sneakier than some of the creatures...")
        time.sleep(2)
    if mode == "DIFFICULT" or "difficult":
        mode_error == "no"
        print("...")
        time.sleep(1)
        print("Tip: not all of the creatures have common sense! Some are trickable...")
        time.sleep(2)
time.sleep(0.5)
print("Good luck.")
print(mode + " |  NATURE WALK")
if mode == "normal" or "NORMAL":
    choose_name = input("Would you like to choose your character\'s name?  (y/n)")
    if choose_name == "y":
        name = input("Please name your character:  ")
        time.sleep(2)
        print("...")
        print(name + ", welcome!!")
    if choose_name == "n":
        name = "You"
        time.sleep(2)
        print("...")
        print(name + ", welcome, mysterious traveller!!")
    animal_roll = input("Would you like to select the order of some of the creatures that you will encounter? (y/n)")
    if animal_roll == "y":
        time.sleep(0.2)
        print("Choose:")
        print(" ")
        print("a) squirrel")
        print("b) rat")
        print("c) chipmunk")
        animal_1 = input("a, b, or c?")
        if animal_1 == "a":
            animal_1 = "squirrel"
        if animal_1 == "b":
            animal_1 = "rat"
        if animal_1 == "c":
            animal_1 = "chipmunk"
            #animal_2
            time.sleep(1)
        print("Choose:")
        print(" ")
        print("a) butterfly")
        print("b) moth")
        animal_2 = input("a or b?")
        if animal_2 == "a":
            animal_2 = "butterfly"
        if animal_2 == "b":
            animal_2 = "moth"
            time.sleep(1)
        print("Choose:")
        print(" ")
        print("a) moose")
        print("b) deer")
        print("c) horse")
        animal_3 = input("a, b, or c?")
        if animal_3 == "a":
            animal_3 = "moose"
        if animal_3 == "b":
            animal_3 = "deer"
        if animal_3 == "c":
            animal_3 = "horse"
            time.sleep(1)
        print("Selection concluded. One moment...")
        time.sleep(2)


        #need to add if they opt out of choosing their character's name!! (done)

print("It's a sunny day-- perfect for a hike.")
time.sleep(1)
print("City-life is stressful. The thick air suffocates you with pollutants. Oh, how you miss your rural home.")
time.sleep(1)
input("<Press enter to continue>")
print("It's Thanksgiving Break! You've travelled all the way to Sholow Trails. You chose this hiking site because of the ancient myths and the trail's abundance of wildlife.")
time.sleep(1)
print("*You walk over to the start of the trail, and grab a map.* You are equipped with nothing but a teacup. Your mother had questioned your sanity, insisting that you carry more supplies. But nobody could stop you from charging out of the house.")
time.sleep(1)
input("<Press enter to continue>")
print("*Your empty teacup's lid quietly clinks against the ceramic body of the teacup.* You march onwards, and time stalls.")
time.sleep(1)
path_1 = input("In no time, the first fork in the path is ahead of you. You see two signs. The first peath leads to a waterfall, and the other leads to a cliff. Will you take the FIRST or SECOND path?")
if path_1 == "FIRST" or "first":
    print("First path it is. ... 8 minutes pass, akin to the numerous towering oak trees. You've lost track of time again, when a " +  animal_1 + " scurries out of your path.")
    print(animal_1 + '''"WATCH IT!! I was munching on this here seed, you inconsiderate tower."''')
    one = input("Converse the creature, or return the attitude? (a/b)")
    if one == "a":
        print("Oops, I didn't notice that I had company. How are you, er... sir " + animal_1 + "?")
        time.sleep(0.2)
        print(animal_1 + ": Well, I've been doing QUITE fine without some walking skyscraper OBLITERATING my acorn-- how \'bout that??")
        time.sleep(0.2)
        print(animal_1 + ": Anyhow, what\'s with the fancy cup, stranger skyscraper?")
        time.sleep(0.5)
        two = input("Admit your confusion, or make up a story to sound more sane? (a/b)")
    if two == "a":
        print(name + ": Uhh, I just felt like it.")
        time.sleep(0.5)
        print(animal_1 + ": Mm. ...")
        time.sleep(0.5)
        print("...")
        time.sleep(1)
        print("*You start to feel awkward.*")
        time.sleep(1)
        print(name + ": You know, I actually was going to visit the waterfalls and make a cup of tea to celebrate my evening outdoors. You know, harvest some flowers and just top my tea with \'em. Learned of it from Granny.")
        print("... ")
        print(animal_1 + ": How dare you. EVERY FLOWER IS MINE MUAHAHAHAHAHHA. My minions will alert me should you try to steal from my territory.")
        time.sleep(0.5)
        print(name + ": Says who.")
        time.sleep(1)
        print(animal_1 + ": ME. I am king of the " + animal_1 + " realm. You are lucky that I am bored, else I would signal my " + animal_1 + "army to expel you of my lands.")
        time.sleep(0.5)
        print(name + ": Please, everything has just been too much, lately. I\'m just trying to take a breather through this beautiful nature.")
        time.sleep(2.5)
        print(name + ": You seem like the kinda guy to let me prove myself. So let me.")
        time.sleep(2)
        print(animal_1 + ": FINE, annoying giant. As I've told you already, I\'m famished for entertainment. But, I\'m also a chill " + animal_1 + ". So, I\'ll offer you the deal of your lifetime.")
        time.sleep(2)
        three = input("Should you back out of any deals, or continue? (type leave/stay)")
        if three == "leave":
            print(name + ": Uhhh okay nevermind!")
            time.sleep(2)
            print("Some time passes. You start to wonder if the day can get any crazier.")
            four = input("...Can it?? (y/n)")
            if four == "y":
                print("<a bush is rustling, how odd!>")
                five = input("Investigate it?")
                if five == "y":
                    print("<The MOST ADORABLE baby fox trips, stumbling out from under the cover of the leafy bush.>")
                    six = input("Awww, it's so tiny!! Should you stop to admire it? (y/n)")
                    if six == "y":
                        print("You stop to coo at the baby fox, feeling a new appreciation for nature.")
                        time.sleep(1.5)
                        print('''Kit (baby fox): "HEY, BRO!! Let me keep my aura, alright?? What if my siblings overhear??? I'm going to get targeted during play time."''')
                        time.sleep(0.5)
#committing changes at this point.
