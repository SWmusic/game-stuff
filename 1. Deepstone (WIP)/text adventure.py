from sys import exit

import random

# very first scene, hence awakening
def awakening():
    print('\n\n')
    print('-' * 50)
    print("\n\nYou awake. You feel awful. It is pitch black, and you cannot see anything. The sounds of drips ring out around you, drip drip drip. \nFading into your ears, a raspy voice carries out of the darkness.")
    player_1_name = input('\n...\n\n"Well, what do we have here? What is your name, traveler?" ').strip().capitalize()
    if player_1_name == '':
        print('\n\n"The silent type, eh? I will know your name.')
        awakening()
    else:
        print(f'\n"Ah, {player_1_name}. A perfectly sane name. Yes yes, ohh do not be afraid, ye of plenty flesh. \nI am Warl, the Wretched. You are a Minded, are you not? We have not seen one of your ilk in quite some time."')
        choice_1()

# first choice player must make
def choice_1(): 
    choice_1_1 = input("\nWhat will you do? \n[1]: Ask about where you are. \n[2]: Ask more about Warl. \n[3]: Ask about what he meant by Minded. \n[4]: Venture forth. \n[5]: Run. \n[6]: Quit. \n")
    if choice_1_1 == '1':
        print('\n"We are in a secluded part of the Beneath, near the surface world. This is my territory, heh heh. \nHowever, I am afraid that it will not be mine soon. I am succumbing to the Slag you see."')
        print("\nYou've never heard of the Beneath.")
        def choice_1_1a():
            choice_1_1_1 = input("\nWhat will you do? \n[1]: Ask about the slag. \n[2]: go back. \n")
            if choice_1_1_1 == '1':
                print('\n\n"Ohh it is terrible. It is a slow killer, the stone. Ohh the stone. It creeps into you, seeping, crumbling. \nHe he he, soon your mind crumbles. Ooh I feel it, even now. Hahaha" \nSoon his cackling turned into painful coughing.')
                choice_1()
            elif choice_1_1_1 == '2':
                choice_1()
        choice_1_1a()
    elif choice_1_1 == '2':
        print('\n\n"You wish to know more about wretched old me eh? \n I am but an old man now, succumbing to illness, heh heh. \nMy fellow villagers cast me out in fear of my affliction. I may be wretched, but I will not exile my own. Fools." \nYou hear the sound of a man spitting. You hope that it landed nowhere near you.')
        choice_1()
    elif choice_1_1 == '3':
        print('\n\n"Oh, you do not know what a Minded is? Even though you yourself are one?" \n\nYou hear him mutter the word "fool" under his breath while he prepares his next statement with a loud breath in. \n\n"We Fichians were afflicted with a disease you see, the Slag. It spreads inside you, the stone it does. Turns your mind into mere mineral. \nThose deep into infection are called the Mindless. Turns them crazy it does. Me? I am still as sane as they come!" \n\nA cackle floats out into the cavernous space around you.')
        choice_1()
    elif choice_1_1 == '4':
        venture_1()
    elif choice_1_1 == '5':
        print('\nYou turn around and run in the opposite direction of Warl. \n\n"YOU DARE RUN FROM MY HOSPITALITY?" Booms out behind you. \n\nYou run headfirst into the wall of the cavern. \nYou hear quick and heavy thuds behind you, and before you can even use your voice, a hand covered in rock grabs your head and slams it into the cave. \nYou feel a warm liquid roll down your brow, and you vaguely hear the roar of an unearthly creature as you begin to lose consciousness. \n\nYou died.')
        def choice_1_1b(): 
            choice_1_1_2 = input('\nYou are dead. Do you wish to retry from a checkpoint? \n[1]: Yes. \n[2]: No. \n')
            if choice_1_1_2 == '1':
                choice_1()
            elif choice_1_1_2 == '2':
                leaving()
        choice_1_1b()
    elif choice_1_1 == '6':
        leaving()
    else:
        print("Invalid choice.")
        choice_1()

# The quit option.
def leaving():
    print("May you go in peace.")
    exit(0)

# the "inventory".
inventory = []

# leaving the start area
def venture_1():
    print('\nYou bode Warl farewell and begin to turn around to stumble your way through the darkness.')
    print('\nAs you turn, you feel a rocky hand grab your arm. \n\n"Leaving so soon?" \n\n You say you must, as you are not from here. \n\n"But I have not had any to talk to in so long... \nFine. If you are to leave, then at least take this torch."')
    print('\nYou obtained the torch!')
    inventory.insert(0, 'torch')
    venture_2()

# leaving the start area pt. 2
def venture_2():
    choice_2_1 = input('\nWhat will you do? \n[1]: Light the torch and venture forth. \n[2]: Light the torch and throw it at Warl. \n[3]: Light the torch and study your surroundings. \n[4]: Do not light the torch and begin walking. \n[5]: Quit. \n')
    if choice_2_1 == '1':
        print('\n\nYou light the torch. The flames flicker and illuminate your surroundings. You feel the soft crunch of rock dust underneath your feet as you travel forth. \n\n"I will be seeing you..." rings out from the now darkened space behind you. \n\nAfter traveling for some time, you come across a massive space. \nUpon entry, a pile of rocks falls behind you, blocking where you entered from.')
        row_1_houses_scenario()
    
    elif choice_2_1 == '2':
        print('You light the torch, turn around, and throw it at Warl. \n\n"YOU INSOLENT TRASH!" \n\nThe torch bounced harmlessly off of the rocky exterior of Warl. \n\nYou hear him roar in rage. He picks up the torch, and in one leap lands in front of you. \n\nYou try to turn around to run, but by the time your back turns to his monstrous form, a white hot pain shoots through your body. \nThe bottom of the torch is sticking out from your chest. Your chest? \nJust as the question begins to register in your brain, your vision fades to black.')
        choice_2_1_1 = input('\nYou died. \n\nWould you like to try again? \n[1]: Yes. \n[2]: No. \n')
        if choice_2_1_1 == '1':
            venture_2()
        elif choice_2_1_1 == '2':
            leaving()
    elif choice_2_1 == '3':
        print('\nYou light the torch. You examine your surroundings. \nYou notice first how large the space that surrounds you is. The walls of the cavern are pale grey, like slate. \nYou turn to look at the being that woke you. What muscles not converted to stone in his face pulled to form a twisted smile. \n\n"Now you have seen me, eh? I hope my looks certainly live up to my title heh heh." \n\nSurrounding Warl is a drab little camp, complete with a cooking pot and a place for a fire just underneath. \nYou turn and see a large opening completely devoided of light, but it beckons you at the same time.')
        venture_2()
    elif choice_2_1 == '4':
        print('\nYou tuck the torch into your waistband, unlit. You begin walking in a random direction. \nYour foot snags a stray rock on the cavern floor, and you trip and fall. \n\nYou hear Warl softly mutter, "Idiot." and you dust yourself off as you get back up. \n\nYou feel very stupid.')
        venture_2()

    elif choice_2_1 == '5':
        leaving()
    else:
        print('\nInvalid input. Try again.')
        venture_2()

# environmental obstacles
village_1_obstacles = ['first_village_wall_1', 'row_1_house_2_door']
# village 1 scenario
def row_1_houses_scenario():
    print('\nThe flickers from your torch briefly paint warm light over the area, revealing a collection of small houses lined up with a central road straight through the settlement. \nIt did not take long to notice that several corpse shaped rock formations were laying in the vicinity.')
    def choice_3(): 
        choice_3_1 = input("\nWhat do you want to do? \n[1]: Go to the house on the left. \n[2]: Go to the house on the right. \n[3]: Investigate the rocks. \n[4]: Move forward to next row of houses 2/4. \n[5]: Turn around and go back from where you came. \n[6]: Check inventory. \n[7]: Quit. \n")
        if choice_3_1 == '1':
            if 'crimson key' not in inventory:
                print('\n\nYou jangle the doorknob, but the door is locked. \nYou spot a reddish keyhole.')
                choice_3()
            elif 'crimson key' in inventory:
                print('\nYou pushed the crimson key into the reddish lock, and you hear a click. \n\nThe door unlocks. \n\nYou slip the key back into your pocket.')
                print('\n\nYou walk inside the house, and immediately the smell of decay and dust violate your sense of smell. \nOne table sits solitarily in the middle of the room, a thick coat of dust rests on top of it. \nYou notice a door to your right, presumably leading to the only bedroom.')
                def choice_3_1_1_1(): 
                    choice_3_1_1 = input('\n\nWhat would you like to do? \n[1]: Explore the main room. \n[2]: Try the bedroom door. \n[3]: Leave the house. \n[4]: Quit. \n')
                    if choice_3_1_1 == '1':
                        print('\n\nYou walk around the main room. \n\nYou notice some frenzied scratches that lay on the wall. \n\n"Ma. .f S.o.." \nThe rest is too frantic to make head or tail of it. \n\nAs you walk away from the writing, \nyou trip on a hard object on the floor, and you turn and look to see what was in your way. \nA mineral formation in the shape of a hand throws the light of your torch back at you. \n\n... \n\nIs it really just minerals?')
                        choice_3_1_1_1()
            
                    elif choice_3_1_1 == '2':
                        print('\n\nYou walk over to the bedroom door. \nAfter turning the knob, the door gives way easily, creaking on its hinges.')
                        def choice_3_1_1_2():
                            print('\n\nThe room is dark, but you have your torch. \n\nA gruesome scene lays before you. \n\nThe bed had been converted into an odd shrine of sorts, \ndecorated with old candles and various ores and crystals. \nArms and legs coated in stone litter the bed. \nWhat could have even caused this? \n\nYou notice several spheres of agate are lying on the bed.')
                            choice_3_1_2 = input('\n\nWhat would you like to do? \n[1]: Inspect the shrine. \n[2]: Return to the main room. \n[3]: Take an agate sphere. \n[4]: Quit. \n')
                            if choice_3_1_2 == '1':
                                print('\n\nYou walk up to the destroyed bed. \n\nUpon further inspection, you notice a piece of paper lying on the torn sheets. \n\n It reads: \n"The stone, it is awful. I can feel it, \nslowly climbing to my head. It hurts it hurts it hurts it hurts it hurts it hurts i-" \n\n... \n\nThe rest is too faded to read.')
                                choice_3_1_1_2()
                            elif choice_3_1_2 == '2':
                                print('\n\nYou turn around and walk out the door, carefully closing it behind you.')
                                choice_3_1_1_1()
                            
                            elif choice_3_1_2 == '3':
                                if 'agate sphere' not in inventory:
                                    print('\n\nYou slipped one of the agate spheres into your pocket. \nIt was a deep blue color.')
                                    inventory.append('agate sphere')
                                    choice_3_1_1_2()

                                elif 'agate sphere' in inventory:
                                    print("\n\nYou feel uneasy about taking more than one. \n\nYou decide it's for the best that the rest remain on the bed, instead of your pocket.")
                                    choice_3_1_1_2()

                            elif choice_3_1_2 == '4':
                                leaving()
                            else:
                                print('Invalid option.')
                                choice_3_1_1_2()
                        choice_3_1_1_2()
            
                    elif choice_3_1_1 == '3':
                        print('\n\nYou turn around and walk out the door, closing it and locking it behind you. \nAfter all, who would want their home visited?')
                        choice_3()
            
                    elif choice_3_1_1 == '4':
                        leaving()
            
                    else:
                        print('\nInvalid input.')
                        choice_3_1_1_1()
                choice_3_1_1_1()

        elif choice_3_1 == '2':
            if 'row_1_house_2_door' in village_1_obstacles:

                if 'old_pickaxe' not in inventory:
                    print('\n\nThe door is old and boarded. Any ways of opening it have since fallen off. \nIf you had a tool, you might be able to break it down.')
                    choice_3()

                elif 'old_pickaxe' in inventory:
                    print('\n\nThe door is old and boarded up. Any ways of opening it have since been removed. \nIf you had a tool, you might be able to break it down.')
                    def door_remove_1():
                        choice_3_2 = input('\n\nWould you like to use the old pickaxe here? \n[1]: Yes. \n[2]: No.')
                        if choice_3_2 == '1':
                            print('\n\nAfter roughly two minutes of loud thuds and the spraying of splinters, the door gives way. \n\nYou step carefully over the splinters and into the house.')
                            village_1_obstacles.remove('row_1_house_2_door')
                            
                            enter_row_1_house_2()

                        elif choice_3_2 == '2':
                            print('\n\nYou decided against breaking down the door. \nMaybe some things are better left alone.')
                            choice_3()

                        else:
                            print('Invalid input.')
                            door_remove_1()
                    door_remove_1()

            elif 'row_1_house_2_door' not in village_1_obstacles:
                
                print("\n\nYou walk to the house on the right. \nYou step past the remains of the broken door on the ground, and enter the dank building.")
                enter_row_1_house_2()

        elif choice_3_1 == '3':
            print("\n\nYou walk over to an odd-shaped rock formation. \n\nYou look closer... \n\n... \n\nThese aren't rocks... Did these used to be people? \nYou could've sworn you saw the rise and fall of what could've been a chest. \n\nYou start feeling sick.")
            choice_3()

        elif choice_3_1 == '4':
            row_2_houses_scenario()
    
        elif choice_3_1 == '5':
            if 'first_village_wall_1' in village_1_obstacles:
                print("\n\nYou turn to walk back to where you came from, \nbut you see the pile of rocks and remember that you don't have a way to get through them.")
                def wall_1_removal():
                    if 'old_pickaxe' in inventory:
                        choice_3_1_2 = input('\n\nUse pickaxe to break the rocks? \n[1]: Yes. \n[2]: No. \n')
                        if choice_3_1_2 == '1':
                            print('\n\nAfter what seemed like hours, you finally broke the last rock blocking the original entrance.')
                            village_1_obstacles.remove('first_village_wall_1')
                            village_1_to_start()
                    else:
                        print('\n\nYou turn around to face the village once again.')
                        choice_3()
                wall_1_removal()

            else:
                village_1_to_start()

        elif choice_3_1 == '6':
            print(f"\n{inventory}")
            choice_3()
    
        elif choice_3_1 == '7':
            leaving()
    
        else:
            print('Invalid input.')
            row_1_houses_scenario()
    choice_3()

def village_1_to_start():
    choice_3_1_2_1 = input('\n\nWould you like to travel back to where you woke up? \n[1]: Yes. \n[2]: No.')
    if choice_3_1_2_1 == '1':
        print('\n\nYou turn your back to the village, \nwalking towards where you first met Warl. \n\nSoon, the darkness of the cave overtook any sight of the abandonded houses.')
        start_area_scenario()
    else:
        print('\n\nYou turn back to face the village.')
        row_1_houses_scenario()

def start_area_scenario():
    # TODO the revisit of Warl's living area
    placeholder()

def enter_row_1_house_2():
    print('\n\nThe house creaks with age all around you. \nAny furniture was either stolen or destroyed, it seems.')
    def row_1_house_2():
        choice_3_2_1 = input('\n\nWhat do you want to do? \n[1]: Inspect the main room. \n[2]: Leave. \n')
        if choice_3_2_1 == '1':
            if 'crimson_key' not in inventory:
                print("\n\nIt's fairly empty, but as you wave your torch something shiny catches your eye.")
                def inspect_shiny_1():
                    choice_3_2_1_1 = input('\n\nTake a closer look? \n[1]: Yes. \n[2]: No. \n')
                    if choice_3_2_1_1 == '1':
                        print('\n\nYou walk over to the corner of the room, where you spot a crimson key laying on the floor. \n\nObtained the crimson key! \n\nAs you put it in your pocket, you notice that the letter "W" is stamped on the back.')
                        inventory.append('crimson_key')
                        row_1_house_2()
                    elif choice_3_2_1_1 == '2':
                        print("\n\nYou decide that whatever the flash was, it wasn't worth your time.")
                        row_1_house_2()

                inspect_shiny_1()
            else:
                print('\n\nThe room is fairly empty.')
                row_1_house_2()
        elif choice_3_2_1 == '2':
            print('\n\nYou feel it is time to leave. \nYou exit the house, and are now inbetween the first two houses, on the street.')
            row_1_houses_scenario()
        
        else:
            print('Invalid choice.')
            row_1_house_2()
    row_1_house_2()

def row_2_houses_scenario():
    print('\n\nYou walk down the abandoned street. \nThe only sounds in the cave are the soft paddings of your footsteps. \n\nYou have now arrived at the second row of houses.')
    def choice_4():
        choice_4_1 = input('\n\nWhat would you like to do? \n[1]: Go in the house on the left. \n[2]: Go in the house on the right. \n[3]: Look around the area. \n[4]: Go to the first row of houses. \n[5]: Go to the third row of houses. \n[6]: Check inventory. \n[7]: Quit. \n')
        if choice_4_1 == '1':
            print('\n\nYou turn and walk to the house on the left.')
            print("\n\nYou jangle the doorknob, but it's locked. \nYou hear muffled wheezing on the other side of the door. \n\nMaybe it's for the best that it's locked.")
            choice_4()

        elif choice_4_1 == '2':
            print("\n\nYou turn and walk toward the house on the right. \nThere isn't a door, so you step right in.")
            
            def row_2_house_2():
                
                print("\n\nYour torch illuminates an average-sized main room. \nA single painting hangs on the wall. \nPresumably it's a portrait of the family who lived here previously.")
                def row_2_house_2_2(): 
                    choice_4_1_3 = input('\n\nWhat would you like to do? \n[1]: Look around. \n[2]: Go into the bedroom. \n[3]: Inspect the portrait. \n[4]: Leave. \n[5]: Quit. \n')

                    if choice_4_1_3 == '1':
                        print("\n\nYou look around the main room. \n\nDust has been painted onto nearly every surface. \nThe portrait is still staring at you.")
                        row_2_house_2_2()
                        
        
                    elif choice_4_1_3 == '2':
                        if 'medium key' not in inventory:
                            print("\n\nIt's locked. It seems as though there is a medium-sized key that can unlock it.")
                            row_2_house_2_2()
                        elif 'medium key' in inventory:
                            print("\n\nIt's locked. It seems as though there is a medium-sized key that can unlock it.")
                            choice_4_1_3_1 = input("\n\nUse medium key to open the bedroom door? \n[1]: Yes. \n[2]: No. \n")
                            if choice_4_1_3_1 == '1':

                                print('\n\nUsed medium key.')
                                print('\n\nYou turn the key in the lock, and the door opens. \n\nYou step across the threshold into the room.')

                                def row_2_house_1_bedroom():
                                    choice_4_1_3_1_1 = input('\n\nWhat would you like to do? \n[1]: Inspect the room. \n[2]: Leave. \n[3]: Quit. \n')

                                    if choice_4_1_3_1_1 == '1':
                                        print('\n\nThere were clearly signs of people that used to live here. \nA bed for a child sits in the corner, while a large bed dominates the rest of the space. \n\nA body covered in what looked like limestone lay on the main bed, clutching a picture of a child to his chest. \n\nYou feel... \n\n... \n\nsad.')
                                        row_2_house_1_bedroom()
                    
                                    elif choice_4_1_3_1_1 == '2':
                                        print('\n\nYou leave the bedroom. \nThe door closes and locks behind you.')
                                        row_2_house_2_2()
                    
                                    elif choice_4_1_3_1_1 == '3':
                                        leaving()
                    
                                    else:
                                        print('\n\nInvalid input.')
                                        row_2_house_1_bedroom()

                                row_2_house_1_bedroom()

                    elif choice_4_1_3 == '3':
                        print("\n\nYou walk up to the portrait, clouds of dust rise in your footsteps' wake. \n\nUpon closer inspection you notice marks on the wall that indicate something might've been hidden there. \nYou flip the painting around to reveal a medium-sized key.")
                        if 'village_1_medium_key' not in inventory:   
                            print('\n\nObtained the medium-sized key!')
                            inventory.append('medium key')
                            row_2_house_2()
            
                        elif 'medium key' in inventory:
                            print("\n\nYou walk up to the portrait, clouds of dust rise in your footsteps' wake. \n\nUpon closer inspection you notice marks on the wall that indicate something might've been hidden there.")
                            row_2_house_2()
        
                    elif choice_4_1_3 == '4':
                        choice_4()
        
                    elif choice_4_1_3 == '5':
                        leaving()
        
                    else:
                        print('\n\nInvalid option.')
                        row_2_house_2()

                if "medium key" not in inventory:
                    choice_4_1_2 = input('\n\nWhat would you like to do? \n[1]: Look around. \n[2]: Go into the bedroom. \n[3]: Leave. \n[4]: Quit. \n')
                    if choice_4_1_2 == '1':
                        print("\n\nYou look around the main room. \n\nDust has been painted onto nearly every surface. \nThe portrait is still staring at you.")
                        
                        row_2_house_2_2()

                    elif choice_4_1_2 == '2':
                        print("\n\nIt's locked. It seems as though there is a medium-sized key that can unlock it.")
                        row_2_house_2()
    
                    elif choice_4_1_2 == '3':
                        print('\n\nYou walk outside through the missing door.')
                        choice_4()

                    elif choice_4_1_2 == '4':
                        leaving()
    
                    else:
                        print('\n\nInvalid option.')
                        row_2_house_2()
                
                elif "medium key" in inventory:
                    row_2_house_2_2()

            row_2_house_2()

        elif choice_4_1 == '3':
            print('\n\nYou look around. \n\nThe houses are quite drab and rundown. It would seem as if they have not had occupants in a long time. \n\nLittering the streets are more of those odd rock formations. \nSure you are in a cave, but they are quite peculiar. \n\nYou feel a little uneasy.')
            choice_4()

        elif choice_4_1 == '4':
            print('\n\nYou turn and walk to the first row of houses.')
            row_1_houses_scenario()

        
        elif choice_4_1 == '5':
            print("\n\nYou walk towards the third row of houses. \nYour torch highlights some street lamps that appear to have been out of use for quite some time. \nYou see no visible way they could've been powered. \n\nYou have arrived at the third row of houses.")
            row_3_houses_scenario()
        
        elif choice_4_1 == '6':
            print(inventory)
            choice_4()
        
        elif choice_4_1 == '7':
            leaving()
        
        else:
            print('Invalid option.')
            choice_4()
    choice_4()

def row_3_houses_scenario():
    def choice_5():
        choice_5_1 = input("\n\nWhat would you like to do? \n[1]: Go in the house on the left. \n[2]: Go in the house on the right. \n[3]: Go back to the second row of houses. \n[4]: Go to the fourth row of houses. \n[5]: Check inventory \n[6]: Quit \n")
        if choice_5_1 == '1':
            print("\n\nYou turn and walk to the house on the left. \nYou turn the doorknob and the door smoothly opens. \n\nYou step into the house.")
            print("\n\nThe moment your foot crosses the threshold, chills are sent down your spine. \nA terrible feeling is creeping into you. \n\nThis place... \n\n... \n\nhouses something horrible.")
            def choice_5_2(): 
                choice_5_2_1 = input("\n\nWhat would you like to do? \n[1]: Look around. \n[2]: Go into the bedroom. \n[3]: Go outside. \n[4]: Quit. \n")
                if choice_5_2_1 == '1':
                    print("\n\nYou wave your torch. \nYou quickly notice the mold in the corners of the ceilings. \n\nThis house has been devoid of life for a long time. \n\nA broken table sits sadly in the middle of the main room, \nand three chairs are scattered about, some on their sides, and some sitting upright. \n\nA door leading to the bedroom has an odd red mark on it.")
                    choice_5_2()
                
                elif choice_5_2_1 == '2':
                    print("\n\nYou walk to the bedroom door with the odd mark on it. \n\nAs you approach you slow down. \nYou are gradually feeling more nauseous, whatever is behind this door can't be good.")
                    print("\n\nYou turn the knob and walk in. \n\nThe room is completely empty save for a chord hanging from the ceiling. \n\nIf there's nothing in here, what was that feeling for?")
                    def choice_5_2_2():
                        choice_5_2_1_1 = input("\n\nWhat would you like to do? \n[1]: Pull the chord. \n[2]: Leave. \n[3]: Quit. \n")
                        if choice_5_2_1_1 == '1':
                            print("\n\nYou walk over to the center of the room, and you pull the chord hanging from the ceiling. \nA trap door opens and a ladder falls down. \n\nNauseating waves of death and decay emanate from the open hole in the ceiling. \nYou found the source of the bad feeling. \n\nIt definitely is not safe to go up there, but you feel a pull anyways...")
                            def choice_5_2_3():
                                choice_5_2_3_1 = input("\n\nGo up the ladder? \n[1]: Yes. \n[2]: No. \n")
                                if choice_5_2_3_1 == '1':

                                    print("\n\nYou take a shaky breath, steeling your resolve. \n\nEvery possible sense is yelling at you to turn around and never go back, but you push through. \n\nYou have entered the attic.")
                                    def choice_5_2_4():
                                        choice_5_2_4_1 = input("\n\nWhat would you like to do? \n[1]: Examine your surroundings. \n[2]: Go back down. \n[3]: Quit. \n")

                                        if choice_5_2_4_1 == '1':
                                            if 'crimson key' not in inventory:
                                                print("\n\nYou wave the torch around. \nThere is so much dust in the air that the flames of the torch were igniting some of the tiny particles. \n\nThe attic seemed normal until you saw a red crystal-like substance on the floor. \nIt was trailing. \nYour eyes followed the trail, but it went into the dark. \n\nYou walk forward, careful not to step on any while tracing its path. \nThe closer you got the wider the trail became. \nFinally you find it. \nYou feel horrified and awful. \n\nWhat lies before you is the slumped over corpse of a man covered in stone. \nHis chest cavity is open and you see a crystal heart beating slowly and arhythmically. \nSpreading out of the hole in his torso and creeping along the ground and walls is the red crystal substance. \nOther partially crystallized organs are visible as well, \nsimultaneously decaying and being converted into mineral. \n\nThe heart had grown large in its crystallization, to the point that its beats were pushing on the lungs, \nartificially making them pump, resulting in an awful wheezing sound coming from the otherwise still cadaver. \n\nThe light of your torch results in the flash of a darker object inside of the upper chest area.")
                                                def obtain_crimson_key():
                                                    choice_5_2_4_2 = input("\n\nReach into the chest cavity? \n[1]: Yes. \n[2]: No. \n")

                                                    if choice_5_2_4_2 == '1':
                                                        print("\n\nThe thought of putting your hand in there makes you want to vomit, but you begin reaching in anyways. \n\nYou notice a single snail with a shell made of ruby on his shoulder.\n\nYou feel the roughness of the crystals against your hand as you struggle to pull the object out. \nFinally, it gives way, and you accidentally knock the heart out as you pull the key out of his chest. \n\nYou turn and vomit. \nIt takes several minutes to collect yourself. \nIn the meantime, the heart stopped beating and the corpse lay completely still. \n\nYou got a closer look at what you took. \n\nIt's a blood red key with some crystals on it. \n\nObtained the crimson key!")
                                                        inventory.append("crimson key")
                                                        choice_5_2_4()
                                                    
                                                    elif choice_5_2_4_2 == '2':
                                                        print("\n\nYou walk away from the scene, disgusted and shaken. \n\nYou are standing at the foot of the ladder.")
                                                        choice_5_2_4()
                                                    
                                                    else:
                                                        obtain_crimson_key()
                                                obtain_crimson_key()

                                            elif 'crimson key' in inventory:
                                                print("\n\nYou wave the torch around. \nThere is so much dust in the air that the flames of the torch were igniting some of the tiny particles. \nYour eyes fall on the trail again. \n\nYou do not want to see that gruesome scene again.")
                                                choice_5_2_4()

                                        elif choice_5_2_4_1 == '2':
                                            print("\n\nThis feeling washing over you is too overwhelming. \n\nYou decide to climb back down, shutting the attic door once you're off the ladder. \n\nYou are back in the bedroom.")
                                            choice_5_2_2()
                                        
                                        elif choice_5_2_4_1 == '3':
                                            leaving()
                                        
                                        else:
                                            invalid()
                                            choice_5_2_4()
                                    
                                    choice_5_2_4()
                                    
                                elif choice_5_2_3_1 == '2':
                                    print("\n\nYou hesitate, pushing the ladder back up into the ceiling.")
                                    choice_5_2_2()
                                
                                else:
                                    print("\n\nThat isn't an option right now.")
                                    choice_5_2_3()
                            
                            choice_5_2_3()
                        
                        elif choice_5_2_1_1 == '2':
                            print("\n\nYou walk out of the bedroom, back into the main room.")
                            choice_5_2()
                        
                        elif choice_5_2_1_1 == '3':
                            leaving()
                        
                        else:
                            invalid()
                            choice_5_2_2()
                    choice_5_2_2()
                    
                elif choice_5_2_1 == '3':
                    choice_5()

                
                elif choice_5_2_1 == '4':
                    leaving()

                else:
                    print('\n\nInvalid option.')
                    choice_5_2()

            choice_5_2()
        elif choice_5_1 == '2':
            # TODO row 2 house 2 scenario
            placeholder()
            choice_5()
        
        elif choice_5_1 == '3':
            print("\n\nYou turn and walk back to the second row of houses.")
            row_2_houses_scenario()
        
        elif choice_5_1 == '4':
            print("\n\nYou walk to the fourth row of houses. \n\nThe dreariness of the village is weighing on you.")
            row_4_houses_scenario()
            choice_5()
        
        elif choice_5_1 == '5':
            print(inventory)
            choice_5()
        
        elif choice_5_1 == '6':
            leaving()
        
        else:
            invalid()
            choice_5()
        

    choice_5()

def row_4_houses_scenario():
    def choice_6():
        choice_6_ = input("\n\nWhat would you like to do? \n[1]: Go in the house on the left \n[2]: Go in the house on the right \n[3]: Leave the village. [4]: Go to the third row of houses. \n[5]: Check inventory. \n[6]: Quit. \n")
        if choice_6_ == '1':
            # TODO row 4 house 1 scenario
            placeholder()
            choice_6()
        
        elif choice_6_ == '2':
            # TODO row 4 house 2 scenario
            placeholder()
            choice_6()
        
        elif choice_6_ == '3':
            # TODO leaving the village
            placeholder()
            choice_6()
        
        elif choice_6_ == '4':
            print("\n\nYou turn and walk to the third row of houses.")
            row_3_houses_scenario()
        
        elif choice_6_ == '5':
            print(inventory)
            choice_6()
        
        elif choice_6_ == '6':
            leaving()
        
        else:
            invalid()
            choice_6()
    
    choice_6()

def placeholder():
    print("This area isn't finished yet!")


def invalid():
    print("\n\nInvalid input.")
awakening()
