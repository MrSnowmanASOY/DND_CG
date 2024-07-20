import math
import random
import os
import sys
import logging
import time

print("Locating Current Working Directory")
cwd = os.path.dirname(os.path.realpath(__file__))
print("According to this the file is located at directory " + cwd)
print("Hope thats correct...")
os. chdir(cwd)


class tcolors:
  WARNING = '\033[93m'
  BOLD = '\033[1m'
  UNDERLINE = '\033[4m'
  ENDC = '\033[0m'
  FAIL = '\033[91m'

typing_speed0 = 500 #wpm
def slow_type0(t):
    for l in t:
        sys.stdout.write(l)
        sys.stdout.flush()
        time.sleep(random.random()*10.0/typing_speed1)
typing_speed1 = 250 #wpm
def slow_type1(t):
    for l in t:
        sys.stdout.write(l)
        sys.stdout.flush()
        time.sleep(random.random()*10.0/typing_speed1)
typing_speed2 = 10 #wpm
def slow_type2(t):
    for l in t:
        sys.stdout.write(l)
        sys.stdout.flush()
        time.sleep(random.random()*10.0/typing_speed2)
typing_speed3 = 60 #wpm
def slow_type3(t):
    for l in t:
        sys.stdout.write(l)
        sys.stdout.flush()
        time.sleep(random.random()*10.0/typing_speed3)
typing_speed4 = 140 #wpm
def slow_type4(t):
    for l in t:
        sys.stdout.write(l)
        sys.stdout.flush()
        time.sleep(random.random()*10.0/typing_speed4)

program_lines = len(open('printer.py').readlines(  ))
# program_characters = 

slow_type0("File size: " + str(program_lines) + " lines")
print(" ")
slow_type0("Creating maths...")
print(" ")
slow_type0("Creating randomness...")
print(" ")
slow_type0("Making an operating system...")
print(" ")
slow_type0("Running system software...")
print(" ")
slow_type0("Logging things...")
print(" ")
slow_type0("Creating time...")
print(" ")


slow_type1("Initializing System: [")
time.sleep(1)
slow_type2("▇▇")
try:
    file_check = open("assets/text/equipment/adventuring_gear")
    file_check = open("assets/text/equipment/breath_weapons")
    file_check = open("assets/text/equipment/martial_melee_weapons")
    file_check = open("assets/text/equipment/martial_ranged_weapons")
    file_check = open("assets/text/equipment/simple_melee_weapons")
    file_check = open("assets/text/equipment/simple_ranged_weapons")
    file_check = open("assets/text/equipment/starting_equipment_heavy_armor")
    file_check = open("assets/text/equipment/starting_equipment_light_armor.txt")
    file_check = open("assets/text/equipment/starting_equipment_medium_armor")
    file_check = open("assets/text/equipment/starting_equipment_shield")
    file_check = open("assets/text/equipment/wiz_spells")
    file_check = open("assets/text/equipment/wiz_cantrips")
    file_check = open("assets/text/char_details/ages")
    file_check = open("assets/text/char_details/alignment")
    file_check = open("assets/text/char_details/classes")
    file_check = open("assets/text/char_details/flaws")
    file_check = open("assets/text/char_details/good_traits")
    file_check = open("assets/text/char_details/languages")
    file_check = open("assets/text/char_details/Lifestyle_Expenses")
    file_check = open("assets/text/char_details/Races")
    file_check = open("assets/text/char_details/body/Fantasy_eye_colours")
    file_check = open("assets/text/char_details/body/hair_styles")
    file_check = open("assets/text/char_details/body/skin_styles")
    file_check = open("assets/text/char_details/body/skin_tone")
    file_check = open("assets/text/char_details/body/True_eye_colours")
    file_check = open("assets/text/char_details/dragonborns/draconic_ancestrys")
    file_check = open("assets/text/char_details/dragonborns/skin_style_drag")
    file_check = open("assets/text/char_details/naming/Female_Names")
    file_check = open("assets/text/char_details/naming/Last_Names")
    file_check = open("assets/text/char_details/naming/Male_Names")
except IOError:
    print(" ")
    slow_type1("File Missing...")
    print(" ")
    slow_type1("Errors may occur...")
    time.sleep(2)
finally:
    file_check.close()

slow_type3("▇▇▇▇")

slow_type4("▇▇▇▇▇▇▇▇▇] Done")
print(" ")
print("Good luck Adventurer!")
print(" ")
print(" ")
print(" ")






def clamp(n, minimum, maximum):
  """
  Returns n clamped between the given minimum and maximum values.
  """
  return max(0, min(n, maximum))


def get_number_input(msg, range=None, default=0):
  """
  Waits for console input from the user and converts it to a number.
  If the conversion fails (user entered a letter), then it will ask again.
  Otherwise the input is clamped using the given range or just returned.
  """
  while True:
    try:
      inp = input(msg)
      if inp == "":
        return default

      n = int(inp)
      if range == None:
        return n
      min, max = range
      return clamp(n, min, max)
    except:
      pass

def generator():
  gender = input("What gender is your character? (f or m): ") # selecting the gender
  if gender.lower().startswith("m"):
    gender = "m"
  elif gender.lower().startswith("f"):
    gender = "f"
  else:
    gender = "Truncation Error"  # if the given gender cant be truncated properly then the variable is set to an error and is dealt with later

  aogct = get_number_input(
    "How many good character traits do you want your character to have? (Def:0) (0 - 21) (1 good trait = +2 bad traits) (Rec:5): ",
    (0, 21)
  ) # Asking the user how many good traits they want

  give_align = input("Would you like an alignment? (Y/n): ")
  if give_align == 'n':
    pass
  else:
    alignment_cho = open('assets/text/char_details/alignment').read().splitlines()           #Having a crisis
    print("Having a crisis...")
    time.sleep(0.01)
    rand_align = input("Would you like the alignment to be random? (Y/n): ")
    if rand_align == 'n':
      print("The normal set of alignments are:")
      print("Lawful Good")
      print("Neutral good")
      print("Chaotic good")
      print("Lawful neutral")
      print("True neutral")
      print("Chaotic neutral")
      print("Lawful evil")
      print("Neutral evil")
      print("Chaotic evil")
      print("You my also enter a custom alignment.")
      chos_alignment = input("Pick an alignment (Type the one you want): ")
    else:
      chos_alignment = random.choice(alignment_cho)
      print("Focusing the moral compass...")
      time.sleep(0.1)
      print("Decided on " + chos_alignment)
  pick_real_eyes = input("Would you like your eye colour to be realistic? (y/N): ")
  if pick_real_eyes == 'y':
    eye_options = open('assets/text/char_details/body/True_eye_colours').read().splitlines()          #Coming up with normal eye colours
    print("Coming up with normal eye colours...")
    chos_eye_colour = random.choice(eye_options)
    time.sleep(0.01)
  else:
    eye_options = open('assets/text/char_details/body/Fantasy_eye_colours').read().splitlines()          #Coming up with obscure eye colours
    print("Coming up with obscure eye colours...")
    chos_eye_colour = random.choice(eye_options)
    time.sleep(0.01)

  


  # importing files
  skin_choice_texture_drag = open('assets/text/char_details/dragonborns/skin_style_drag').read().splitlines()   #Taking notes on dragonborns...
  print("Taking notes on dragonborns...")
  skin_choice_colour = open('assets/text/char_details/body/skin_tone').read().splitlines()      #Looking at people
  print("Looking at people...")
  time.sleep(0.01)
  skin_choice_texture = open('assets/text/char_details/body/skin_styles').read().splitlines()   #Feeling people
  print("Feeling people...")
  time.sleep(0.01)
  instaled_languages = open('assets/text/char_details/languages').read().splitlines()      #Studying languages
  print("Studying languages...")
  time.sleep(0.01)

  
  if gender == 'm':
    m_names = open('assets/text/char_details/naming/Male_Names').read().splitlines()                #Coming up with names for males
    print("Coming up with names for males...")
    time.sleep(0.01)
  elif gender == 'f':
    f_names = open('assets/text/char_details/naming/Female_Names').read().splitlines()              #Coming up with names for females
    print("Coming up with names for females...")
    time.sleep(0.01)
  else:
    print(tcolors.WARNING + "Error Retreiving Gender Selection" + tcolors.ENDC)
    print(tcolors.WARNING + gender + tcolors.ENDC)
    print(tcolors.WARNING + "Randomising Gender" + tcolors.ENDC)
    time.sleep(3.00)
    gender = random.randint(0,1)
    if gender == 0:
      gender = 'm'
      print("Decided on Male")
      m_names = open('assets/text/char_details/naming/Male_Names').read().splitlines()                #Coming up with names for males
      print("Coming up with names for males...")
      time.sleep(0.01)
    elif gender == 1:
      gender = 'f'
      print("Decided on Female")
      f_names = open('assets/text/char_details/naming/Female_Names').read().splitlines()              #Coming up with names for females
      print("Coming up with names for females...")
      time.sleep(0.01)

  l_names = open('assets/text/char_details/naming/Last_Names').read().splitlines()                #Thinking of last names
  print("Thinking of last names...")
  time.sleep(0.01)
  c_races = open('assets/text/char_details/Races').read().splitlines()                     #Looking up the list of races
  print("Looking up the list of races...")
  time.sleep(0.01)
  s_m_w = open('assets/text/equipment/simple_melee_weapons').read().splitlines()        #Hand crafting the simple melee weapons
  print("Hand crafting the simple melee weapons...")
  time.sleep(0.01)
  s_r_w = open('assets/text/equipment/simple_melee_weapons').read().splitlines()        #Dusting off the simple ranged weapons
  print("Dusting off the simple ranged weapons...")
  time.sleep(0.01)
  m_m_w = open('assets/text/equipment/simple_melee_weapons').read().splitlines()        #Forging a few martial melee weapons
  print("Forging a few martial melee weapons...")
  time.sleep(0.01)
  m_r_w = open('assets/text/equipment/simple_melee_weapons').read().splitlines()        #Purchasing some martial ranged weapons
  print("Purchasing some martial ranged weapons...")
  time.sleep(0.01)
  DAs = open('assets/text/char_details/dragonborns/draconic_ancestrys').read().splitlines()            #Reading up on some draconic ancestry
  print("Reading up on some draconic ancestry...")
  time.sleep(0.01)
  BWs = open('assets/text/equipment/breath_weapons').read().splitlines()                #Reading up on the breath weapons
  print("Reading up on the breath weapons...")
  time.sleep(0.01)
  LsE_cho = open('assets/text/char_details/Lifestyle_Expenses').read().splitlines()        #Giving Lifestyle choices to pick from 
  print("Giving Lifestyle choices to pick from ...")
  time.sleep(0.01)
  class_cho = open('assets/text/char_details/classes').read().splitlines()                 #Reading the classes list
  print("Reading the classes list...")
  time.sleep(0.01)
  hair_styles = open('assets/text/char_details/body/hair_styles').read().splitlines()           #Coming up with hair styles
  print("Coming up with hair styles...")
  time.sleep(0.01)


  # Randomising strs and ints
  cr = random.choice(c_races)                                   #Creating racism

  # For debugging purposes, uncomment to select
  # cr = "Dragonborn"                                             # Only Dragonborns
  # cr = "Dwarf"                                                  # Only Dwarf
  # cr = "Elf"                                                    # Only Elf
  # cr = "Halfling"                                               # Only Halfling
  # cr = "Human"                                                  # Only Human
  # cr = "Gnome"                                                  # Only Gnome
  # cr = "Half-Elf"                                               # Only Half-Elf
  # cr = "Half-Orc"                                               # Only Half-Orc
  # cr = "Tiefling"                                               # Only Tiefling

  print("Creating racism...")
  time.sleep(0.01)

  if gender == 'm':
    mn = random.choice(m_names)                                     #Choosing cool male name
    print("Choosing cool male name...")
    time.sleep(0.01)
  elif gender == 'f':
    fn = random.choice(f_names)                                     #Choosing an okay female name
    print("Choosing an okay female name...")
    time.sleep(0.01)
  else:
    print(tcolors.FAIL + "Error Retreiving Chosen Gender" + tcolors.ENDC)
    print(tcolors.FAIL + gender + tcolors.ENDC)
    print(tcolors.FAIL + "Defaulting to Female" + tcolors.ENDC)
    fn = random.choice(f_names) 
    time.sleep(5.00)


  ln = random.choice(l_names)                                     #Picking an epic last name
  print("Picking an epic last name...")
  time.sleep(0.01)
  smw1 = random.choice(s_m_w)                                     #Deciding on a simple melee weapon
  print("Deciding on a simple melee weapon...")
  time.sleep(0.01)
  smw2 = random.choice(s_m_w)                                     #Testing out a second simple melee weapon
  print("Testing out another simple melee weapon...")
  time.sleep(0.01)
  srw1 = random.choice(s_r_w)                                     #Firing a simple ranged weapon
  print("Firing a simple ranged weapon...")
  time.sleep(0.01)
  mmw1 = random.choice(m_m_w)                                     #Dragging a martial melee weapon
  print("Dragging a martial melee weapon...")
  time.sleep(0.01)
  mrw1 = random.choice(m_r_w)                                     #Dropping a martial ranged weapon
  print("Dropping a martial ranged weapon...")
  time.sleep(0.01)
  simple_weapons = random.randint(0,1)                            #Deciding weather to have Simple or Martial weapons
  print("Deciding weather to have Simple or Martial weapons...")
  time.sleep(0.01)
  LsE = random.choice(LsE_cho)                                    #Adopting a lifestyle
  print("Adopting a lifestyle...")
  time.sleep(0.01)


  # Checking if the character is a dragon born
  if cr == 'Dragonborn':
    skin_ct = random.choice(skin_choice_texture_drag)
    print("Feeling your scales...")
    chr_hair_style = "NA"
    chr_hair_colour = "NA"
  else:
    skin_cc = random.choice(skin_choice_colour)                     #Eyeing you down
    print("Eyeing you down...")
    time.sleep(0.01)
    skin_ct = random.choice(skin_choice_texture)                    #Feeling you
    print("Feeling your skin...")
    time.sleep(0.01)
    chr_hair_style = random.choice(hair_styles)                     #Styling your hair
    print("Styling your hair...")
    time.sleep(0.01)
    true_hair_colours = input("Would you like your hair to be realistic colours? (y/N): ")
    if true_hair_colours == 'y':
      hair_colour = open('assets/text/char_details/body/True_eye_colours').read().splitlines()
      chr_hair_colour = random.choice(hair_colour)                  #Setting the hair colour
    else:
      hair_colour = open('assets/text/char_details/body/Fantasy_eye_colours').read().splitlines()           #Coming up with hair styles
      print("Coming up with hair styles...")
      chr_hair_colour = random.choice(hair_colour)                  #Setting the hair colour



  # calculating age
  print("Setting your body clock...")
  if cr == 'Dragonborn':
    age = random.randint(2,70)
  elif cr == 'Dwarf':
    age = random.randint(19,340)
  elif cr == 'Elf':
    age = random.randint(30,740)
  elif cr == 'Halfling':
    age = random.randint(10,240)
  elif cr == 'Human':
    age = random.randint(14,75)
  elif cr == 'Gnome':
    age = random.randint(18,490)
  elif cr == 'Half-Elf':
    age = random.randint(18,170)
  elif cr == 'Half-Orc':
    age = random.randint(10,65)
  elif cr == 'Tiefling':
    age = random.randint(18,140)
  else:
    print("Error calculating age, please try again...")
    pass



  # Deciding on player class
  init_plr_cls = random.choice(class_cho)      #decides on a player class

  # init_plr_cls = "Barbarian"                   #Only Barbarian
  # init_plr_cls = "Bard"                        #Only Bard
  # init_plr_cls = "Cleric"                      #Only Cleric
  # init_plr_cls = "Druid"                       #Only Druid
  # init_plr_cls = "Fighter"                     #Only Fighter
  # init_plr_cls = "Monk"                        #Only Monk
  # init_plr_cls = "Paladin"                     #Only Paladin
  # init_plr_cls = "Ranger"                      #Only Ranger
  # init_plr_cls = "Rogue"                       #Only Rogue
  # init_plr_cls = "Sorcerer"                    #Only Sorcerer
  # init_plr_cls = "Warlock"                     #Only Warlock
  # init_plr_cls = "Wizard"                      #Only Wizard
  
  print("Going to " + init_plr_cls + " school.")
  time.sleep(0.01)



  #Wizard stuff
  if init_plr_cls == 'Wizard':
    opt_cantrips = open('assets/text/equipment/wiz_cantrips').read().splitlines()                #Reading wizard cantrips
    print("Reading wizard cantrips...")
    time.sleep(0.01)
    opt_spells = open('assets/text/equipment/wiz_spells').read().splitlines()                #Reading wizard spells
    print("Reading wizard spells...")
    time.sleep(0.01)
    cantrips = 3
    spells = 2
    cho_cantrips = random.choices(opt_cantrips, k=cantrips)
    cho_spells = random.choices(opt_spells, k=spells)
  else:
    pass






  #Randomiser
  # cbw = random.choice(BWs)   # grabbing a random breath weapon for the lovely dragonborn ~
  if cr == 'Dragonborn':
    cda = random.choice(DAs)    # finding a draconic ancestry for the dragonborn
    print("Rummaging through the history books...")
  elif cr != 'Dragonborn':
    cda = " "


  # Finding what breath weapon the dragonborn should have from their cda
  if cda != ' ':
    if cda == 'Fire':
      cbw = 'Breath Weapon (Fire)     -  2d6                          -  1 use per long rest'
    elif cda == 'Frost':
      cbw = 'Breath Weapon (Frost)    -  2d6                          -  1 use per long rest'
    elif cda == 'Acid':
      cbw = 'Breath Weapon (Acid)     -  2d6                          -  1 use per long rest'
    elif cda == 'Poison':
      cbw = 'Breath Weapon (Poison)   -  2d6                          -  1 use per long rest'
    elif cda == 'Lightning':
      cbw = 'Breath Weapon (Lightning) -  2d6                          -  1 use per long rest'
    else:
      pass
  else:
    pass

  # Checking what scale colour to give the dragon born
  if cr == 'Dragonborn':
    print("Polishing your scales...")
    if cda == 'Fire':
      skin_cc = "Red"
    if cda == 'Frost':
      skin_cc = "White"
    if cda == 'Acid':
      skin_cc = "Black"
    if cda == 'Poison':
      skin_cc = "Green"
    if cda == 'Lightning':
      skin_cc = "Bronze"
  else:
    pass



  # Giving the character Languages
  if cr == 'Dwarf':
    Spoken_Languages = random.choices(instaled_languages, weights=(100,100,10,5,10,10,10,10,5,5,5,5,5,5,5,5), k=4)
  if cr == 'Elf':
    Spoken_Languages = random.choices(instaled_languages, weights=(100,10,100,5,10,10,10,10,5,5,5,5,5,5,5,5), k=4)
  if cr == 'Halfling':
    Spoken_Languages = random.choices(instaled_languages, weights=(100,10,10,5,10,10,100,10,5,5,5,5,5,5,5,5), k=4)
  if cr == 'Human':
    Spoken_Languages = random.choices(instaled_languages, weights=(100,30,30,10,30,30,30,30,10,10,10,10,10,10,10,10), k=4)
  if cr == 'Dragonborn':
    Spoken_Languages = random.choices(instaled_languages, weights=(100,10,10,5,10,10,10,10,5,5,100,5,5,5,5,5), k=4)
  if cr == 'Gnome':
    Spoken_Languages = random.choices(instaled_languages, weights=(100,10,10,5,100,10,10,10,5,5,5,5,5,5,5,5), k=4)
  if cr == 'Half-Elf':
    Spoken_Languages = random.choices(instaled_languages, weights=(100,10,10,5,10,10,100,10,5,5,5,5,5,5,5,5), k=4)
  if cr == 'Half-Orc':
    Spoken_Languages = random.choices(instaled_languages, weights=(100,10,100,5,10,10,10,10,5,5,5,5,5,5,5,5), k=4)
  if cr == 'Tiefling':
    Spoken_Languages = random.choices(instaled_languages, weights=(100,10,10,5,10,10,10,10,5,5,5,5,80,5,5,5), k=4)


  # Calculating how tall the player is
  rand_h = random.randint(-1,1)
  print("Seeing how tall you are...")
  if cr == 'Dwarf':
    height = (random.randint(30,50)/10)+(rand_h/10)
  if cr == 'Elf':
    height = (random.randint(30,61)/10)+(rand_h/10)
  if cr == 'Halfling':
    height = (random.randint(28,34)/10)+(rand_h/10)
  if cr == 'Human':
    height = (random.randint(10,100)/10)+(rand_h/10)
  if cr == 'Dragonborn':
    height = (random.randint(30,70)/10)+(rand_h/10)
  if cr == 'Gnome':
    height = (random.randint(30,40)/10)+(rand_h/10)
  if cr == 'Half-Elf':
    height = (random.randint(40,60)/10)+(rand_h/10)
  if cr == 'Half-Orc':
    height = (random.randint(59,64)/10)+(rand_h/10)
  if cr == 'Tiefling':
    height = (random.randint(56,62)/10)+(rand_h/10)



  # Calculating Player GP
  time.sleep(0.01)
  print("Seeing how rich you are...")
  if init_plr_cls == 'Barbarian' or 'Druid':
    plr_gp = random.randint(2,8) * 10
  elif init_plr_cls == 'Bard' or 'Cleric' or 'Fighter' or 'Paladin' or 'Ranger':
    plr_gp = random.randint(5,20) * 10
  elif init_plr_cls == 'Druid':
    plr_gp = random.randint(2,8) * 10
  elif init_plr_cls == 'Monk':
    plr_gp = random.randint(5,20)
  elif init_plr_cls == 'Rogue' or 'Warlock' or 'Wizard':
    plr_gp = random.randint(4,16) * 10
  elif init_plr_cls == 'Sorcerer':
    plr_gp = random.randint(3,12) * 10


  # Allocating initial statuspoint numbers
  print("Rolling weighted dice...")
  i_Stren = random.randint(8,18)
  time.sleep(0.01)
  i_Dexte = random.randint(8,18)
  time.sleep(0.01)
  i_Const = random.randint(8,18)
  time.sleep(0.01)
  i_Intel = random.randint(8,18)
  time.sleep(0.01)
  i_Wisdo = random.randint(8,18)
  time.sleep(0.01)
  i_Chari = random.randint(8,18)
  time.sleep(0.01)


  time.sleep(0.01)
  print("Calculating your modifiers...")
  # ──────────────────────────────────
  # Calculating str based things
  # ────────────────────────────────── Str Modifier
  if cr == 'Dragonborn':
    i_Stren = i_Stren + 2
  elif cr == 'Half-Orc':
    i_Stren = i_Stren + 2
  elif cr == 'Human':
    i_Stren = i_Stren + 1
  else:
    pass
  str_m = (i_Stren - 10) // 2 
  math.trunc(str_m)
  # ──────────────────────────────────
  # Calculating dex based things
  # ────────────────────────────────── Dex Modifier
  if cr == 'Elf':
    i_Dexte = i_Dexte + 2
  elif cr == 'Halfling':
    i_Dexte = i_Dexte + 2
  elif cr == 'Human':
    i_Dexte = i_Dexte + 1
  else:
    pass
  dex_m = (i_Dexte - 10) // 2
  math.trunc(dex_m)
  # ──────────────────────────────────
  # Calculating con based things
  # ────────────────────────────────── Con Modifier
  if cr == 'Dwarf':
    i_Const = i_Const + 2
  elif cr == 'Half-Orc':
    i_Const = i_Const + 1
  elif cr == 'Human':
    i_Const = i_Const + 1
  else:
    pass
  con_m = (i_Const - 10) // 2
  math.trunc(con_m)
  # ──────────────────────────────────
  # Calculating int based things
  # ────────────────────────────────── Int Modifier
  if cr == 'Gnome':
    i_Intel = i_Intel + 2
  elif cr == 'Tiefling':
    i_Intel = i_Intel + 2
  elif cr == 'Human':
    i_Intel = i_Intel + 1
  elif cr == 'Half-Elf':
    i_Intel = i_Intel + 1
  else:
    pass
  int_m = (i_Intel - 10) // 2
  math.trunc(int_m)
  # ──────────────────────────────────
  # Calculating wis based things
  # ────────────────────────────────── Wis Modifier
  if cr == 'Human':
    i_Wisdo = i_Wisdo + 1
  elif cr == 'Half-Elf':
    i_Wisdo = i_Wisdo + 1
  else:
    pass
  wis_m = (i_Wisdo - 10) // 2
  math.trunc(wis_m)
  # ──────────────────────────────────
  # Calculating cha based things
  # ────────────────────────────────── Cha Modifier
  if cr == 'Dragonborn':
    i_Chari = i_Chari + 1
  elif cr == 'Tiefling':
    i_Chari = i_Chari + 1
  elif cr == 'Half-Elf':
    i_Chari = i_Chari + 2
  elif cr == 'Human':
    i_Chari = i_Chari + 1
  else:
    pass
  cha_m = (i_Chari - 10) // 2
  math.trunc(cha_m)
  # ──────────────────────────────────

  # Calculating Racial bonuses
  time.sleep(0.01)
  print("Seeing if your race adds anything to your scores...")
  if cr == 'Dragonborn':
    rabon = "+2 STR, +1 CHA"
  elif cr == 'Dwarf':
    rabon = "+2 CON"
  elif cr == 'Elf':
    rabon = "+2 DEX"
  elif cr == 'Gnome':
    rabon = "+2 INT"
  elif cr == 'Half-Elf':
    rabon = "+2 CHA, +1 INT, +1 WIS"
  elif cr == 'Halfling':
    rabon = "+2 DEX"
  elif cr == 'Half-Orc':
    rabon = "+2 STR, +1 CON"
  elif cr == 'Human':
    rabon = "+1 All Ability Scores"
  elif cr == 'Tiefling':
    rabon = "+2 CHA, +1 INT"



  # Calculating final statuspoints based on race, items, ect.
  f_Stren = i_Stren
  f_Dexte = i_Dexte
  f_Const = i_Const
  f_Intel = i_Intel
  f_Wisdo = i_Wisdo
  f_Chari = i_Chari

  prof_bon = 2

  Stren_save = str_m # + prof_bon    |    I dont know what I was thinking here but this needs to be changed, Saves are dependant on classes in most cases and are not just a blanket addition.
  Dexte_save = dex_m # + prof_bon    |    I dont know what I was thinking here but this needs to be changed, Saves are dependant on classes in most cases and are not just a blanket addition.
  Const_save = con_m # + prof_bon    |    I dont know what I was thinking here but this needs to be changed, Saves are dependant on classes in most cases and are not just a blanket addition.
  Intel_save = int_m # + prof_bon    |    I dont know what I was thinking here but this needs to be changed, Saves are dependant on classes in most cases and are not just a blanket addition.
  Wisdo_save = wis_m # + prof_bon    |    I dont know what I was thinking here but this needs to be changed, Saves are dependant on classes in most cases and are not just a blanket addition.
  Chari_save = cha_m # + prof_bon    |    I dont know what I was thinking here but this needs to be changed, Saves are dependant on classes in most cases and are not just a blanket addition.

  #Finding the classes hit die
  
  if init_plr_cls == "Barbarian":
    chr_hit_die = "d12"
  if init_plr_cls == "Ranger" or "Paladin" or "Fighter":
    chr_hit_die = "d10"
  if init_plr_cls == "Bard" or "Cleric" or "Druid" or "Monk" or "Rogue" or "Warlock":
    chr_hit_die = "d8"
  if init_plr_cls == "Sorcerer" or "Wizard":
    chr_hit_die = "d6"


  # Calculating HP

  """
  This system will only work for level 1 characters
  If I want to generate a character of a higher level I will need to change this system
  """
  if init_plr_cls == "Barbarian":
    chr_HP = con_m + 12
  if init_plr_cls == "Ranger" or "Paladin" or "Fighter":
    chr_HP = con_m + 10
  if init_plr_cls == "Bard" or "Cleric" or "Druid" or "Monk" or "Rogue" or "Warlock":
    chr_HP = con_m + 8
  if init_plr_cls == "Sorcerer" or "Wizard":
    chr_HP = con_m + 6


  # Finding good character traits
  if aogct != 0:

    good_character_traits = open("assets/text/char_details/good_traits", "r")
    goodtraitslist = []

    for line in good_character_traits:
            goodtraitslist.append(line.replace("\n", "\n"))

    good_character_traits.close()

    good_character_traits_options = goodtraitslist #files to choose from in random selection
    rand_valu = []
    amount_of_good_character_traits = aogct

    for i in range(amount_of_good_character_traits):
        rand_gt = random.choice(good_character_traits_options)
        rand_valu.append(rand_gt)    
        good_character_traits_options.remove(rand_gt) # Removes the trait from the list of available ones so there's no double-ups

    gct = "".join(rand_valu).rstrip("\n")

    # Finding bad character traits
    flaw = open("assets/text/char_details/flaws", "r")

    flawslist = []

    for line in flaw:
            flawslist.append(line.replace("\n", "\n"))

    flaw.close()

    flaws_options = flawslist #files to choose from in random selection
    rand_vals = []
    amount_of_flaws = amount_of_good_character_traits*2

    for i in range(amount_of_flaws):
        rand_flaw = random.choice(flaws_options)
        rand_vals.append(rand_flaw)    
        flaws_options.remove(rand_flaw) # Removes the flaw from the list of available ones so there's no double-ups

    Character_flaws = "".join(rand_vals).rstrip("\n")
  elif aogct == 0:
    pass

  """
  The good and bad character traits can be very inbalanced 
  and since they are randomly selected they can contradict each other (blind, deaf, and scared of mirrors)
  """

  print("Making Character sheet...")

  pp = 10 + wis_m
  armor_class = 10 + dex_m

  """
  I want to make a system here that checks ability rolls for more than one 9 or < and then rerolls if needed
  Asking the player if they would like to select which ability to reroll would be nice but they dont get to
  pick which stats are focused on in the first place so that whole system would need a rework.
  """


  print("")
  print("")
  print("")
  # Printing out the character
  print("──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────")
  if gender == 'm':
    print("Name: " + mn + " " + ln)
  else:
    print("Name: " + fn + " " + ln)
  print("──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────")
  if gender == 'm':
    print("Gender: Male")
  else:
    print("Gender: Female")
  if cr == 'Dragonborn':
    print("──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────")
    print("Race: " + cr)
    print("──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────")
    print("Draconic Ancestry: " + str(cda))
    print("──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────")
    print("Breath Weapon: " + str(cbw))
  elif cr != 'Dragonborn':
    print("──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────")
    print("Race: " + cr)
  print("──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────")
  print("Character height: " + str(height))
  print("Character age: " + str(age))
  print("Eye colour: " + (chos_eye_colour))
  print("Initiative: +" + str(dex_m))
  print("Movment speed: 30")
  print("Spoken Languages: " + str(Spoken_Languages))
  print("Hair style: " + str(chr_hair_style))
  print("Hair colour: " + str(chr_hair_colour))
  if cr == 'Dragonborn':
    print("Character Scales: " + skin_cc + ", " + skin_ct)
  else:
    print("Character Skin: " + skin_cc + ", " + skin_ct)
  if give_align == 'y':
    print("Alignment: " + chos_alignment)
  else:
    pass
  print("Class: " + init_plr_cls)
  print("Hit die: " + str(chr_hit_die))
  print("Armor class: " + str(armor_class))
  print("Health: " + str(chr_HP))
  if aogct == 0:
    print("──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────")
  elif aogct != 0:
    print("──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────")
    print("Good Character Traits: ")
    print(gct)
    print("──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────")
    print("Bad Character Traits: ")
    print(Character_flaws)
    print("──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────")
  print("Proficiency Bonus: " + str(prof_bon))
  print("Ability scores:")
  print("Ability        -   Score               -    Modifier           -    Save Modifier")
  print("Strength:      -   "+str(f_Stren)+"                  -    "+str(str_m)+"                  -    "+str(Stren_save))
  print("Dexterity:     -   "+str(f_Dexte)+"                  -    "+str(dex_m)+"                  -    "+str(Dexte_save))
  print("Constitution:  -   "+str(f_Const)+"                  -    "+str(con_m)+"                  -    "+str(Const_save))
  print("Intelligence:  -   "+str(f_Intel)+"                  -    "+str(int_m)+"                  -    "+str(Intel_save))
  print("Wisdom:        -   "+str(f_Wisdo)+"                  -    "+str(wis_m)+"                  -    "+str(Wisdo_save))
  print("Charisma:      -   "+str(f_Chari)+"                  -    "+str(cha_m)+"                  -    "+str(Chari_save))
  print("Racial modifiers: " + str(rabon) + "    " + "These modifiers have already been added")
  print("──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────")
  print("Skill points: ")
  print("Passive Wisdom:   " + str(pp))
  print("Acrobatics:       " + str(dex_m)) 
  print("Animal Handling:  " + str(wis_m)) 
  print("Arcana:           " + str(int_m)) 
  print("Athletics:        " + str(str_m)) 
  print("Deception:        " + str(cha_m)) 
  print("History:          " + str(int_m)) 
  print("Insight:          " + str(wis_m)) 
  print("Intimidation:     " + str(cha_m)) 
  print("Investigation:    " + str(int_m)) 
  print("Medicine:         " + str(wis_m)) 
  print("Nature:           " + str(int_m)) 
  print("Perception:       " + str(wis_m)) 
  print("Performance:      " + str(cha_m)) 
  print("Persuasion:       " + str(cha_m)) 
  print("Religion:         " + str(int_m)) 
  print("Sleight of Hand:  " + str(dex_m)) 
  print("Stealth:          " + str(dex_m)) 
  print("Survival:         " + str(wis_m)) 
  print("──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────")
  print("Lifestyle     -    Price/Day")
  print(str(LsE))
  print("──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────")
  print("Weapons")
  print("Name                     - 	Damage 	                 -     Properties")
  if simple_weapons == '1':
    print(smw1)
    print(smw2)
    print(srw1)
  elif simple_weapons == '0':
    print(mmw1)
    print(mrw1)
  if cda == 'Fire':
    print("Breath Weapon (Fire)     -     2d6                          -  1 use per long rest, Burns creatures  ")
  elif cda == 'Frost':
    print("Breath Weapon (Frost)    -     2d6                          -  1 use per long rest, Freezes creatures")
  print("Items")
  print("Gold = " + str(plr_gp) + " GP")
  if init_plr_cls == 'Wizard':
    print("Cantrips: " + str(cho_cantrips))
    print("Spells: " + str(cho_spells))
  print("──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────")
  print("")
  print("")
  print("")
  print("")


while True:
  generator()
