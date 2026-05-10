'''
Sierra Andreason
IS 303 - A02
Quest Recommender

Goal: Suggest a quest type based on player level and class.

Decision Logic: Different quests for level ranges (1-10, 11-25, 26+), 
modified by class (warrior, mage, rogue, healer, bard)

Inputs:
 - Player's Name (input)
 - Player's Class (input)
 - Player's Level (integer)

Processes: 
 - Verify player's level first, then class
 - Recommend a Quest based on level and class

Outputs:
 - Print player's Name, Class, Level
 - Quest type + Encouraging Message
 - Print an error if any input reads invalid
'''
player_name = input("What is your character's name? ").capitalize()
player_class = input("What is your class's name? ").lower()
raw_level = input("What is your player level? ").strip()

if raw_level.isdigit():
  player_level = int(raw_level)
else: 
  print("Error! Player level must be a whole number! ")
if player_class == "warrior":
    if 1<= player_level <=10:
     print("Recommended Quest:Aid the Wounded Blue Lady ")
#Why is there an error here?? 
    elif 11<= player_level <=25:
     print("Recommended Quest:Fight the Rebel Army ")

    elif player_level >= 26:
     print("Recommended Quest:Conquer the Mystic Jade Dragon ")

    else: print("Error! Enter player level as a whole number. ")

elif player_class == "mage":
    if 1<= player_level <=10:
     print("Recommended Quest:Discovering the Arcane Arts ")

    elif 11<= player_level <=25:
     print("Recommended Quest:James and the Ancient Potion Brewery ")

    elif player_level >= 26:
     print("Recommended Quest:Overcoming Khizan's Tower ")
     #error here too

    else: print("Error! Enter player level as a whole number. ")

elif player_class == "rogue":
    if 1<= player_level <=10:
     print("Recommended Quest: What's a Little Money? ")

    elif 11<= player_level <=25:
     print("Recommended Quest:The Five-for-Nine knife deal ")
     #error again

    elif player_level >= 26:
     print("Recommended Quest:The Assasination of Emporor Zul ")

    else: print("Error! Enter player level as a whole number. ")

elif player_class == "healer":
    if 1<= player_level <=10:
     print("Recommended Quest:The Upper Hand of the Underdog ")

    elif 11<= player_level <=25:
     print("Recommended Quest:Half-Damage Dealt; Double-Damage Given ")

    elif player_level >= 26:
     print("Recommended Quest:The Rise and Fall of the Heijong Army ")

    else: print("Error! Enter player level as a whole number. ")

elif player_class == "bard":
    if 1<= player_level <=10:
     print("Recommended Quest:Persuading the Governor's Daughter ")

    elif 11<= player_level <=25:
     print("Recommended Quest:Avoiding the Syren's Call ")

    elif player_level >= 26:
     print("Recommended Quest:Whisked Away on a Whiskey Day ")

    else: print("Error! Enter player level as a whole number. ")

else: print("Error. Please input a valid entry! ")

print(f"{player_name} the level {player_level} {player_class.capitalize()}, is on the Quest of a Lifetime! \nGo forth, venture, conquer! ")