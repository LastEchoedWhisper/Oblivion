#master variable list
what = "What will you do?"

scene_1 = "You awaken to find yourself in a dark room. You hear a faint scream in the distance; lights \
flicker on and illuminate the room that you are in."

scene_2 = "As you observe the hallway, you notice three other doors, one on your right with a red circle, \
two on your left bearing identical purple squares. You hear a screeching sound closer to you each second."

scene_3 = "You enter a smoke filled hallway; the smoke makes it difficult for you to breathe. You don’t know \
which direction the fire is in."


what = "What will you do?"

dead = "You have died, please refresh the page to start over."

which = "Which will you choose?"

#beginning of intro code
print('Welcome to Oblivion')
print("Developed by Andres Dorado & Jose Torres")

from datetime import datetime
now = datetime.now()
print("\n")
print('%s/%s/%s %s:%s:%s' % (now.month, now.day, now.year,now.hour, now.minute, now.second))
print("\n")

print(scene_1)
print("\n")

print (what)

#all possible selections are presented here

a1 = "A. Inspect desk"
b1 = "B. Open door"
c1 = "C. Turn off lights"

a2 = "A. Door with a red circle"
b2 = "B. First door with a purple square"
c2 = "C. Second door with a purple square"

two_a_green = 'Green button'
two_a_white = 'White button'
two_a_red = "Red button"
two_a_yellow = "Yellow button"
two_a_blue = "Blue button"

two_c_novial = 'A) Do not take a vial'

two_c_poison = 'B) .--.---.. ...--- -.'

two_c_language = 'C) .-.. .- -. --. ..-.- --. .'

two_c_tech = 'D) -.-.-.....-.---.-..-----...-.-.'

two_c_endurance = 'E) .-.-....-.-..--.-.-..'

two_c_strength = 'F) ...-.-..-.--.-....'


#unoffocial start of code, I don't wanna move this in case I break the code
print(a1)
print(b1)
print(c1)

ans1 = input('Type A, B or C and press enter: ').upper()

#all possible answers are presented here and each question has 3 options
#for simplicity's sake scene 2 will correspond with options 4, 5, and 6. Scene 3 with options 7, 8 and 9, and so on.
option_1 = "You find a notebook and a pen; there are illegible markings in the notebook."
option_2 = "You walk up and open the door. Some creature, vaguely humanoid, slams you into the ground and injects \
you with something. The creature leaves and you slowly lose consciousness..."
option_3 = "You turn off the lights. Something or someone opens the door and peers in, it then closes the door. \
a moment passes and you believe the being is gone. You then walk about and encounter a hallway."
option_4 = "You open the door and upon entering the door shuts immediately behind you."
option_5 =  "You exit out of door 2. You see the hallway and then a robotic creature grasps yours limbs and then \
injects something into you"
option_6 = "You exit out of a door with a yellow triangle, you enter a large room with strange vials lining the walls."

#all list of outcomes in answer variation, thanks to Andrew
outcome_2a = "You awaken strapped to a chair, observing the room you see massive glass tubes with humans floating \
within them. You struggle against the restraints for a while then they become undone. You walk towards a control center \
with many buttons and flashing lights; you have no idea how to operate the controls so you look for labels but find none. \
You have the choice from pushing some of the five most appealing buttons."

outcome_2b = "You enter a room with a door that has a small thick glass window. As you inspect the room you notice a lever \
with two buttons next to it; a green button atop of a red button."

outcome_2c = "You enter a room with shelves lining the walls each full of dials. Each shelf has strange dots and lines next \
to them; you presume that these dots and dashes are labels. You have no idea what the vials do or what they are for."

outcome_2a_green = "The instant you press the button you hear a strange sound, as you look for the source of the sound \
you realize the vents are making a strange noise. You feel lightheaded and head towards the door in order to get a breath \
of fresh air; the door is locked. Your vision blurs as it fades to black." #user dies and restarts game

outcome_2a_yellow = "An alarm reverberates throughout the room, yellow lights flash in two second intervals. The sound \
of rushing water can be heard, in your panic you leave through a door past all of the glass tubes. Entering a large room \
full of strange vials which line the walls." #leads to outcome 2c

outcome_2a_red = "You push the button, nothing happens." #removes option but leaves other open

outcome_2a_blue = "You hear a clicking sound then a door past the glass tubes opens." #leads to outcome 2c

outcome_2a_white = "You notice the lights on the control panel fade and flicker into darkness, the lights in the room \
progressively dim; your only source of light is the glass tubes containing the floating human bodies. As you examine the \
bodies you notice different tubes going into them. You eventually bore of examining the bodies in the glass tubes and \
attempt to leave through the door you came from, the door is locked. Hours pass and the lights illuminating the glass \
tubes slowly flicker out of existence. Trapped in complete darkness you slowly wait for rescue. A sound is heard \
immediately followed by complete silence; days pass by as you are trapped in the cold dark room. You can’t feel your \
arms or your legs. Who are you? Are you even alive?" #user dies LUL

outcome_2c_novial = "You decide that the vials are ominous and most likely lethal; you walk out of the room so that your \
curiosity doesn’t get the best of you."

outcome_2c_poison = "You grab a vial and immediately drink the contents within. The liquid within the vial is sweet and as \
it goes down your throat you feel a slow pain emanating from your stomach. You collapse onto the floor as a burning \
sensation spreads throughout your body. All of the shimmering vials slowly fade to black as you breathe your last breaths."

outcome_2c_language = "You grab a vial and immediately drink the contents within. The liquid within the vial is sour and \
it burns as it goes down your throat. Your vision wanes as you close your eyes; an intense shearing pain spreads through \
your head. You collapse onto the floor; you truly believe you are dying. The throbbing pain slowly lessens until it is gone. \
You walk out of the room regretting having drunk whatever was within the vial."

outcome_2c_tech = "You grab a vial and immediately drink the contents within. The liquid within the vial is bland and \
metallic. As the liquid travels down your throat you feel a searing hot sensation and the liquid feels viscous as it \
slowly slithers down your throat. Your head begins to throb, your forehead burns and aches. You stumble out of the room, \
regretting having drunk what was in the vial as you massage your forehead in an attempt to quell the pain."

outcome_2c_endurance = "You grab a vial and immediately drink the contents within. The liquid within has no taste; you \
assume you just drank water. You feel refreshed and energetic. You stroll out of the room."

outcome_2c_strength = "You grab a vial and immediately drink the contents within. The liquid within is bitter and it makes \
you gag and cough. You compose yourself and walk out of the room ready to take on whatever comes your way."

#all dictionaries will be here
dic1 = {"A": option_1, "B": option_2, "C": option_3}

dic1_a_chosen = {"B": option_2, "C": option_3}

dic2 = {"A": option_4, "B": option_5, "C": option_6}

dic2_buttons = {"GREEN": outcome_2a_green, "YELLOW": outcome_2a_yellow, "BLUE": outcome_2a_blue, "RED": outcome_2a_red,
               "WHITE": outcome_2a_white}

dic2_c_chosen = {"A": outcome_2c_novial, "B": outcome_2c_poison, "C": outcome_2c_language, "D": outcome_2c_tech,
                 "E": outcome_2c_endurance, "F": outcome_2c_strength}

#start of master code
print(dic1[ans1])

if dic1[ans1] == option_1:
   ans1_a_chosen =input('Type B or C and press enter: ').upper()
   print(dic1_a_chosen[ans1_a_chosen])
   print("\n")
   if dic1_a_chosen[ans1_a_chosen] == option_2:
       print(dead)
   if dic1_a_chosen[ans1_a_chosen] == option_3:
       print(scene_2)
       print('Which door do you choose?')
       print(a2)
       print(b2)
       print(c2)
       ans2 = input('Type A, B or C and press enter: ').upper()
if dic1[ans1] == option_2:
   print ('\n')
   print (dead)
#kinda where option 2 starts
if dic1[ans1] == option_3:
   print(scene_2)
   print('\n')
   print('Which door do you choose?')
   print(a2)
   print(b2)
   print(c2)

ans2 = input('Type A, B or C and press enter: ').upper()


print(dic2[ans2])

if dic2[ans2] == option_4:
   print("\n")
   print(outcome_2a)
   print (which)
   print("\n")
   print (two_a_green)
   print (two_a_blue)
   print (two_a_red)
   print (two_a_white)
   print (two_a_yellow)
   ans2_a_chosen = input("Please type the color only and press enter: ").upper()
   if dic2_buttons[ans2_a_chosen] == outcome_2a_green:
       print (outcome_2a_green)
       print (dead)
   if dic2_buttons[ans2_a_chosen] == outcome_2a_blue:
       print("\n")
       print (outcome_2a_blue)
       print (outcome_2c)
       print('\n')
       print("What is your choice?")
       print(two_c_novial)
       print(two_c_poison)
       print(two_c_language)
       print(two_c_tech)
       print(two_c_endurance)
       print(two_c_strength)
       vialq = input("Type the letter corresponding to your choice and press enter: ").upper()
       if dic2_c_chosen[vialq] == outcome_2c_novial:
           print(outcome_2c_novial)
       if dic2_c_chosen[vialq] == outcome_2c_poison:
           print(outcome_2c_poison)
           print(dead)
       if dic2_c_chosen[vialq] == outcome_2c_language:
           print(outcome_2c_language)
   if dic2_buttons[ans2_a_chosen] == outcome_2a_red:
       print (outcome_2a_red)
   if dic2_buttons[ans2_a_chosen] == outcome_2a_white:
       print (outcome_2a_white)
       print (dead)
   if dic2_buttons[ans2_a_chosen] == outcome_2a_yellow:
       print (outcome_2a_yellow)

print("no u")