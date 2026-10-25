print("Welcome to the Interactive Nature Game, where you will be expected to solve a mystery!")
print("...")
old_hp = 100
import time
import random
game_status = "pending"
mode_error = "no"
game_mode = "incomplete"
mode_error_resolved = "incomplete"
#can be "incomplete", "Invalid", or "done"
time.sleep(1)
print("--> Are you excited to try out this game?")
q1 = input("Please type 'y' or 'n' for yes/no.")
print("------")
time.sleep(1)

#game mode selection:
for gap in range(5):
    print(" ")
print("...")
print("------  GAME SET-UP  ------")
print("                        ...")
for gap in range(5):
    print(" ")
print("                     ------")
time.sleep(1.5)
print("It\'s now time to select your game mode! There are 2: NORMAL and DIFFICULT. Please indicate which you\'d like to use! ")
time.sleep(1)

print("...............")
mode = input("==> Would you like to try DIFFICULT or NORMAL mode?  ")
print("..............")

if mode not in {"normal", "NORMAL", "difficult", "DIFFICULT"}:
    game_mode = "invalid"
    mode_error = "yes"
    print("<Error: player has requested an *invalid*    '" + mode + "'    mode>")
    mode_error_resolved = "false"
#error false below.
if mode in ["normal" or "NORMAL" or "difficult" or "DIFFICULT"]:
    game_mode = "done"
    mode_error = "no"
    print("Moving on...")
    time.sleep(0.5)
    print("<Player typed " + mode + " mode>")
    print("...")
    time.sleep(1)
    print("configuring...")
#if error true:
if mode not in ["NORMAL", "normal", "DIFFICULT", "difficult"]:
    time.sleep(0.5)
    print("TIP: Some baby animals are educated, but others aren\'t as bright.")
    time.sleep(0.5)
    print(" ")
    print("------")
    print(" ")
    time.sleep(0.5)
    mode = input("==> Please type 'NORMAL', 'normal', 'DIFFICULT', or 'difficult'.  ")
if mode in ["NORMAL", "normal", "DIFFICULT", "difficult"] and mode_error_resolved == "true":
        print("<the mode_error has been resolved!>")

#----------
for gap in range(3):
    print(" ")
q2 = input("--> Are you going to win? (y/n)  ")
#----------

while mode not in ["NORMAL", "normal", "DIFFICULT", "difficult"]:
    if game_mode == "invalid":
        print("Error? = True")
        print("error: game_mode = 'invalid'")
        mode_error == "yes"
    mode = input("Please choose either NORMAL or DIFFICULT mode:  ")
    while mode not in ["NORMAL", "normal", "DIFFICULT", "difficult"]:
                mode_error_wb1 = ["Please select a valid gamemode (NORMAL/DIFFICULT).", "Please type NORMAL or DIFFICULT, then press ENTER on your keyboard."]
                randomized_mode_error_phrase = random.choice(mode_error_wb1)
                mode = input(randomized_mode_error_phrase)
                print(" ")
    else:
        if mode in ["NORMAL", "normal", "DIFFICULT", "difficult"]:
            mode_error == "no"
            game_status = "active"
            game_mode = "done"
            mode_error_resolved = "true"
            print("<game_mode = 'invalid' error resolved>")
            break
for gap in range(5):
    print(" ")

#code stopped working after this line, seemingly ^
#segments of code that were cut out were located below this line ^
#working, noww!!

#intro-fun q3
for gap in range(3):
    print(" ")
q3 = input("--> Make sure you replay the game to discover all of the endings! (y/n)  ")
for gap in range(3):
    print(" ")
time.sleep(0.5)

#if mode == "DIFFICULT" or "difficult":
    #game_mode = "done"
    #mode_error == "no"

while mode_error_resolved == "true":
    mode_error = "no"
    time.sleep(0.5)
    print("please wait a moment...")
    print("...")
    time.sleep(1)
    print(mode + " mode has successfully been selected!")
    time.sleep(0.5)
    print("...")
    time.sleep(0.5)
    print("We\'re almost done!")
    time.sleep(0.5)
    break
if mode_error == "yes":
    time.sleep(0.5)
    print("<Invalid game mode; triggered pre-selected game mode. (Game mode selection has been auto-skipped. If you\'d like to choose it, still, please exit and restart the game.)>")
    print("-------")
    time.sleep(1)
    input("<Press enter to continue>")


#bottom of the working code ^

time.sleep(0.5)
for gap in range(3):
    print(" ")
game_tips = input("==> Keep game tips enabled? (y/n)  ")
for gap in range(3):
    print(" ")
time.sleep(0.5)

if mode_error == "yes":
    print("<An error has been detected. We\'re sorry!>")
if mode_error == "no":
    if mode == "NORMAL" or "normal":
        while game_tips == "y":
            print("...")
            time.sleep(1)
            print("Tip: You might be sneakier than some of the creatures...")
            time.sleep(0.5)
            break
    if mode == "DIFFICULT" or "difficult":
        time.sleep(0.5)

for gap in range (3):
    print(" ")
animal_roll = input("==> Would you like to select the order of some of the creatures that you will encounter? (y/n)  ")
print("<input recieved!>")
for gap in range (3):
    print(" ")
time.sleep(0.5)
if mode == "DIFFICULT" or "difficult":
    mode_error == "no"
    while game_tips == "y":
        print("...")
        time.sleep(1)
        print("Tip: not all of the creatures have common sense! Some are trickable...")
        break
    else:
        time.sleep(0.5)




if mode == "normal" or "NORMAL":
    choose_name = input("==> Would you like to choose your character\'s name?  (y/n)  ")
    if choose_name == "y":
        name = input("==> Please name your character:  ")
        time.sleep(2)
        print(" ")
        print("┈┈┈┈┈")
        print(name + ", welcome!!")
        print("┈┈┈┈┈")
        print(" ")
    if choose_name == "n":
        name = "You"
        time.sleep(2)
        for gap in range(2):
            print(" ")
        print("┈┈┈┈┈")
        print("Welcome, mysterious traveller!!")
        print("                          ┈┈┈┈┈")
    


for gap in range(5):
    print(" ")
time.sleep(0.5)
print("┅┅┅┅┅     ┅┅┅┅┅     ┅┅┅┅┅     ┅┅┅┅┅")
print(mode + " |  NATURE WALK")
print("┅┅┅┅┅     ┅┅┅┅┅     ┅┅┅┅┅     ┅┅┅┅┅")
time.sleep(0.5)
for gap in range(3):
    print(" ")
print("Good luck.")
for gap in range(5):
    print(" ")


if animal_roll == "y":
    time.sleep(0.2)
    print("Choose:")
    print(" ")
    print("a) squirrel")
    print("b) chipmunk")
    animal_1 = input("==> a or b?  ")
    if animal_1 == "a":
        animal_1 = "squirrel"
    if animal_1 == "b":
        animal_1 = "chipmunk"
        time.sleep(1)
    print("Choose:")
    print(" ")
    print("a) butterfly")
    print("b) moth")
    animal_2 = input("==> a or b?")
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
    animal_3 = input("==> a or b?")
    if animal_3 == "a":
        animal_3 = "moose"
    if animal_3 == "b":
        animal_3 = "deer"
    time.sleep(1)
    print("Selection concluded. One moment...")
    time.sleep(2)
if animal_roll == "n":
    print(" ┈┈┈┈┈")
    print("<Opted out of animal roll>")
    print("<We will select them for you!>")
    print("                        ┈┈┈┈┈")
    if q1 == "y":
        animal_1 = "chipmunk"
        animal_2 = "butterfly"
        animal_3 = "deer"
    if q1 == "n":
        animal_1 = "squirrel"
        animal_2 = "moth"
        animal_3 = "moose"
    if q2 == "y":
        animal_2 = "moth"
    if q2 == "n":
        animal_2 = "butterfly"
    if q3 == "y":
        animal_3 = "deer"
    if q3 == "n":
        animal_3 = "moose"






       
       #need to add if they opt out of choosing their character's name!! (done)
for gap in range(5):
    print(" ")
print("STORYTIME: ")
for gap in range(5):
    print(" ")
print("►  It's a sunny day-- perfect for a hike.")
time.sleep(1)
print("City-life is stressful. The thick air suffocates you with pollutants. Oh, how you miss your rural home.")
time.sleep(1)
input("<Press enter to continue>")
print("►  It's Thanksgiving Break! You've travelled all the way to Sholow Trails. You chose this hiking site because of the ancient myths and the trail's abundance of wildlife.")
time.sleep(1)
print("*You walk over to the start of the trail, and grab a map.* You are equipped with nothing but a teacup. Your mother had questioned your sanity, insisting that you carry more supplies. But nobody could stop you from charging out of the house.")
time.sleep(1)
input("<Press enter to continue>")
print("►  *Your empty teacup's lid quietly clinks against the ceramic body of the teacup.* You march onwards, and time seems to stall.")
time.sleep(1)
print("In no time, the first fork in the path is ahead of you. You see two signs. The first path leads to a waterfall, and the other leads to a cliff.")
if mode in ["difficult" or "DIFFICULT"]:
    path_1 = "SECOND"
if mode == "normal":
    path_1 = input("==> Should you take the SECOND path?  (respond with either: FIRST/SECOND)")
if path_1 == "SECOND" or "second":
    confirm = input("==> Are you sure?? (y = SECOND path/n = FIRST path)  ")
    if confirm == "y":
        print("►  Second path it is. ...")
        time.sleep(0.5)
        print("[ ☁︎ ]  Hours pass. You're exhausted.")
        print(" ")
        time.sleep(0.5)
        input("Press enter to continue.")
        print(" ")
        time.sleep(0.5)
        print("►  *You hear a sound akin to a rattlesnake's rattling tail. It terrifies you.*")
        time.sleep(0.5)
        print("You are just a kid in a lonely forest. What were you even thinking??")
        qq1 = input("==> Should you head back? (y/n)  ")
        if qq1 == "n":
            print("[ ☁︎ ] There seems to be a lot of dark clouds in the sky. Maybe it\'s best to start heading back.")
            qq1 == "y"
        if qq1 == "y":
            for gap in range(2):
                print(" ")
            print("» " + name + "This is not the peaceful day I was hoping for.")
            for gap in range(2):
                print(" ")
            time.sleep(0.5)
            print("►  *You start to turn around...*")
            time.sleep(0.2)
            print("...")
            time.sleep(0.3)
            print("Oh-- It's a baby fox! How adorable!")
            time.sleep(0.2)
            qq1_1 = input("==> Try to pet it? (y/n)  ")
            if qq1_1 == "n":
                print("You can\'t resist the urge to pet the baby fox. It\'s too cute.")
                qq1_1 == "y"
            if qq1_1 == "y":
                print("►  *You slowly approach the baby fox.* It seems to be asleep; it's little body rises and falls gently with each breath.")
                time.sleep(1)
                print("Its fur is surprisingly soft. You want to keep it.")
                time.sleep(0.5)
                print("...")
                time.sleep(0.2)
                print("You continue to admire the baby fox.")
                kit_name = input("==> You love it so much, you want to name it. Choose a name; it\'d be a shame if you chose it\'s name poorly.  ")
                for gap in range(2):
                    print(" ")
                print("» " + name + ": Aww you are SOO so very adorable, " + kit_name + ". I wish I could talk to you!")
                for gap in range(2):
                    print(" ")
                time.sleep(1)
                print("►  You continue to stroke the delicate fur atop " + kit_name + "\'s head.")
                time.sleep(1)
                print("You hear the loud sounds of rowdy teenagers. They're approaching you.")
                qq1_2 = input("==> Should you hide the fox, just in case? (y/n)  ")
                if qq1_2 == "n":
                    print("►  How dare you. It's a vulnerable baby fox!!")
                    print("<" + name + " has been forced to hide the baby fox for its own safety from the up-to-no-good-rowdy-teens.>")
                    qq1_2 = "y"
                if qq1_2 == "y":
                    print("►  But what could you even use to hide " + kit_name + "??")
                    time.sleep(0.5)
                    print("Oh! Your jacket!!")
                    input("<Press enter to continue>")
                    print("►  *You quickly place your jacket over the fox, and sit on the front edge of the jacket.*")
                    time.sleep(1)
                    print("Now, you're blocking " + kit_name + " from view. Nice improvisation!")
                    time.sleep(2)
                    for gap in range(2):
                        print(" ")
                    print("» UNKNOWN: --bruhh where did my cat goooooo.")
                    print("» CLASSMATE: That was a fox, genius.")
                    for gap in range(2):
                        print(" ")
                    input("<Press enter to continue>")
                    print("►  *You pose with your tea cup, pretending that you are sipping from it.*    Your experience in acting is finally paying off.")
                    time.sleep(1)
                    print(0.5)
                    for gap in range(2):
                        print(" ")
                    print("» UNKNOWN: GOGOGOGOGOGOO I SAW HIM RUN THROUGH THOSE BUSHES!")
                    for gap in range (2):
                        print(" ")
                    time.sleep(0.5)
                    print("►  *One of the rowdy teens audibly trips.* Unfortunately, they splash into a creek.")
                    time.sleep(0.5)
                    for gap in range(2):
                        print(" ")
                    print("» CLASSMATE: BRO HURRY UP!")
                    for gap in range(2):
                        print(" ")
                    time.sleep(1)
                    print("►  *You are scared. That voice... it\'s the voice of your old classmate... the one that you ghosted when you moved to the city...")
                    qq1_3 = input("==> Should you just run? (y/n)  ")
                    if qq1_3 == "y":
                        print("►  anddddd off you go! You scooped up the baby fox, and it startles awake.")
                        print("» " + name + ": Shhh, " + kit_name + ", don\'t worry.")
                #ending messages:
                        time.sleep(2)
                        for gap in range(4):
                            print(" ")
                        badge1 = "<MAKE " + animal_1 + " CRY TEARS OF RELIEF>"
                        end_msg1 = ["Congratulations--you've earned: " + badge1 + "!! I\'m mighty proud of ya. (screenshot to save!)", "<  + 1   " + badge1 + " earned. Screenshot this message to store in inventory."]
                        print("꒰ " + end_msg1 + " ꒱")
                        end1 = ["end", "stop game here", "stop", "quit", "end game here", "quit game", "replay", "retry", "reattempt game"]
                        time.sleep(2)
                        end1_confirm = input("Type 'End' to end the game here.  ")
                        if end1_confirm == end1:
                            print(" ")
                            print(" ")
                            print(" ")
                            print("------")
                            print("<Restart the game to discover more endings!!>")


if path_1 == "FIRST" or "first":
    print("►  First path it is. ... 8 minutes pass, akin to the numerous towering oak trees. You've lost track of time again, when a " +  animal_1 + " scurries out of your path.")
    print("» " + animal_1 + ": ⇀‸↼  WATCH IT!! I was munching on this here seed, you INCONSIDERATE tower.")
    one = input("==> Converse with the creature, or return the attitude? (a/b)")
    if one == "b":
        print("» " + name + ": ¬_¬  Shut up, I'm trying to relax on my one day outdoors.")
        time.sleep(1)
        print("►  A thousand acorns pelt at you. *You look up, squinting until you spot a whole gathering of " + animal_1 + "s.")
        input("<Press enter to continue>")
        print("» " + name + ": O_O  Ohhh fudge.")
        time.sleep(0.5)
        print("►  The next moment is filled with " + animal_1 + "s\' screeches.")
        #ending messages:
        badge2 = "<GET ACORNS THROWN AT YOU BY:  " + animal_1 + "s>"
        end_msg2 = ["Congratulations--you've earned: " + badge2 + "!! I\'m mighty proud of ya. (screenshot to save!)", "<  + 1   " + badge2 + " earned. Screenshot this message to store in inventory."]
        print("꒰" + end_msg2+ "꒱")
        end2 = ["end", "stop game here", "stop", "quit", "end game here", "quit game", "replay", "retry", "reattempt game"]
        time.sleep(2)
        end2_confirm = input("Type 'End' to end the game here.  ")
        if end2_confirm == end2:
            print(" ")
            print(" ")
            print(" ")
            print("------")
            print("<Restart game, and try to earn more badges!>")
        #add ending badge here!
    if one == "a":
        print("» " + name + "Oops, I didn't notice that I had company. How are you, er... sir " + animal_1 + "?")
        time.sleep(0.2)
        print("» " + animal_1 + ": (ノಠ益ಠ)ノ  Well, I've been doing QUITE fine without some walking skyscraper OBLITERATING my acorn-- how \'bout that??")
        time.sleep(0.2)
        print("» " + animal_1 + ": ゜-゜  Anyhow, what\'s with the fancy cup, stranger skyscraper?")
        time.sleep(0.5)
        print("►  You look down. You had forgotten about the teacup that you\'ve been holding all this time.")
        time.sleep(1)
        print("OH!! Is that a baby fox, hiding hiding behind you??")
        input("<Press enter to continue>")
        one1 = input("==> Also... is it just your imagination, is does the little foxie look a bit scared? (y/n; y = yes, it\'s scared/n = no, it\'s fine.)")
        if one1 == "n":
            print("You make a double-take, and realize that the baby fox is indeed looking a bit afraid of its surroundings... yet it remains at your side.")
            one1 = "y"
        if one1 == "y":
            print("» " + name + ": °□°  Hey foxie. I didn't know that you followed me. What\'s wrong?")
            time.sleep(1)
            print("►  The baby fox raises its head, slowly meeting your gaze.")
            input("<Press enter to continue>")
            print("» " + kit_name + ": °_o  hellow!")
            time.sleep(0.5)
            print("» " + name + ": Hi, foxie.")
            print("» " + kit_name + ": ●〰●  Me hangry. Want foods. Pweeze. Very hangry.")
            time.sleep(1)
            print("» " + name + ": Awwh.. but I didn\'t bring any food with me...")
            time.sleep(0.5)
            print("►  *You look up, making awkward eyecontact with " + animal_1 + ", who definetely was *not* trembling when you first spoke.")
            input(">Press enter to continue>")
            print("» " + name + ": Okay, " + kit_name + ". I hear you.")
            time.sleep(1)
            print("►  You swear that " + animal_1 + " just gulped.")
            input("<Press enter to continue>")
            print("►  *You look back up at " + animal_1 + ".*")
            time.sleep(0.5)
            print(" ")
        two = input("==> Admit your confusion, or make up a story to sound more sane? (a/b)")
        if two == "a":
            print("» " + name + ": I don't know.")
            time.sleep(0.5)
            print("►  Is it just your imagination, or.. does " + animal_1 + " seem a bit suspicious of you?")
            two_1 = input("==> Yes, I should leave ASAP.  --or--  No, I must be imagining things.  (y/n)")
            if two_1 == "y":
                print("►  <First option selected>")
                print("--------------")
                print("» " + name + ": Hey, I\'m kind of on a mission to make it to a waterfall-- I\'m really sorry for stepping on your acorn.")
                time.sleep(1)
                print("►  An unnatural amount of drool foams at the corners of " + animal_1 + "\'s mouth.")
                print("» " + kit_name + ": Are you guys going to eat me?")
                print("» " + animal_1 + ": W-waaaaaht?? YOUUUU think that an APOLOGY will fix DORA THE ACORN???? HOW DAREEEEE YOU.")
                time.sleep(1.5)
                print("» " + name + ": ...")
                time.sleep(0.5)
                two_2 = input("==> Should you run, now? (y/n)")
            if two_2 == "y":
                print("►  *You\'re running like your life depends on it. Maybe it does.*")
                time.sleep(1)
                print("Adrenaline urges you on, even as sharp pebbles get buried deeper and deeper into the soles of your plain tennis shoes. Maybe you should have invested in quality hiking gear.")
                time.sleep(2)
        if two == "b":
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
            print(name + ": Everything has just been too much, lately. I\'m just trying to take a breather through this beautiful nature.")
            input("<Press enter to continue>")
            print(name + ": You seem like the kinda guy to let me prove myself. So let me.")
            time.sleep(2)
            print(animal_1 + ": FINE, annoying giant. As I've told you already, I\'m famished for entertainment. But, I\'m also a chill " + animal_1 + ". So, I\'ll offer you the deal of your lifetime.")
            time.sleep(2)
            two1 = input("Should you back out of any deals, or continue? (type leave/stay)")
            if two1 == "stay":
                print(animal_1 + ": In order to win this little game, you must risk yourself and first get past the Red Evil Creature.")
                time.sleep(1)
                print(name + ": And who would be this 'Red Evil Creature'?")
                time.sleep(1.5)
                print(animal_1 + ": ...")
                time.sleep(1)
                print(animal_1 + ": Do not give me further reason to doubt your capabilities as my representative in the Den.")
                two1_1 = input(animal_1 + ": I will allow you the opportunity to guess what you\'re going to face. (y=proceed; n=decline offer)")
                if two1_1 == "y":
                    print(name + ": ...okay, let\'s do it then.")
                    time.sleep(0.5)
                    print(animal_1 + ": GET IN YOUR PLACE, TOWER!! I MAKE THE DECISIONS HERE!!")
                    input("<Press enter to continue>")
                    print("<You sigh inwardly, preparing for a waste of time>")
                    print(" ")
                    print("-------")
                    print(" ")
                    a = ["fox", "vixen", "mama fox", "foxes"]
                    b = input("Hurry up and guess what you're going to face, huge thing.  ")
                    if a == b:
                        print(animal_1 + ": Wow, you\'re actually...")
                        time.sleep(1)
                        print(animal_1 + ": ...not so dull as my round tail-- *sniffles but in pride*")
                        input("<Press enter to continue>")
                        print(animal_1 + " seems to be a little... proud of you.")
                        input("<Press enter to continue>")
                        print(animal_1 + ": *muttering to self; clearly deeply emotional for unknown reasons* ...well I might finally get back Dora... my precious acorn...*nostalgic and sad sniffling*")
                if two1_1 == "n":
                    print(name + ": Uhhh okay nevermind!")
                    time.sleep(2)
                    print("Some time passes. You start to wonder if the day can get any crazier.")
                    two1_2 = input("...Can it?? (y/n)")
                    if two1_2 == "y":
                        print("<a bush is rustling, how odd!>")
                        two1_3 = input("Investigate it?")
                        if two1_3 == "y":
                            print("<The MOST ADORABLE baby fox trips, stumbling out from under the cover of the leafy bush.>")
                            two1_4 = input("Awww, it's so tiny!! Should you stop to admire it? (y/n)")
                            if two1_4 == "y":
                                print("You stop to coo at the baby fox, feeling a new appreciation for nature.")
                                time.sleep(1.5)
                                print("Kit (baby fox): HEY, BRO!! Let me keep my aura, alright?? What if my siblings overhear??? I'm going to get targeted during play time.")
                                time.sleep(0.5)
                                print("The kit is right... how could you???")
                                time.sleep(0.5)
                                two1_5 = input("Try to apologize? (y/n)  ")
                                if two1_5 == "n":
                                    print(name+ ": Deal with it. I was only trying to appreciate nature--")
                                    time.sleep(0.5)
                                    print("Kit (angy): MOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOM MOOOOOM MOOOOM MOOOOMM MMOMOMMM!")
                                    time.sleep(3)
                                    print("<You might be in trouble.>")
                                if two1_5 == "y":
                                    print(name + ": I\'m sorry.")
                                    time.sleep(1)
                                    print(" ")
                                    print("...")
                                    print(" ")
                                    time.sleep(1)
                                    print("Kit: *tsks* You should be.")
                                    two1_6 = input("Walk away? (y/n)  ")
                                    if two1_6 == "y":
                                        print("Seeing as there\'s not much else that you can do, now, you begin to walk away.")
                                        time.sleep(0.5)
                                        print("*Suddenly, a bush rustles, and a vixen pounces on top of you.*")
                                        time.sleep(0.2)
                                        print("<You are losing health.>")
                                        print("<You had " + hp + " amount of health.")
                                        hp = (old_hp - 2)
                                        print("<You now have " + hp + " health.")
                                        input("<Press enter to continue>")
                                        print("<You scream like a feral animal. Maybe you are one.>")
                                        print("Vixen: QUIT YOWLING YOU BEAST. LEAVE.")
                                        input("<Press enter to continue>")
                                        print("*The moment that the vixen releases you, you stumble and then take off, following the dirt path before you.*")
#committing changes at this point.