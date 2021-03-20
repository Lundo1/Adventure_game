#Get users name.
name = input("Please enter your name: ")

def woods():
	print(f"\n{name.title()}...{name.title()}...{name.upper()}! You awake suddenly.... your head is pounding and there is dried blood on your forehead."
	"\nNot sure of where you are, you slowly get to your feet, still a little wobbly and confused."
	"\n'Where am I'...you say to yourself.")
	print(f"\nThe fogginess of your mind begins to clear and you realize it is dark and cold"
	"\nYou look around and see where you are, but everything is foreign to you."
	"\nYou do see a cave to the left.\nOption 1 - Explore cave: "
	"\nOption 2 - Go deeper into the woods you woke up in: ")
	next_room = input(" 1 or 2: ")
	if next_room == '1':
		cave()
	elif next_room == '2':
		woods_deep()

def cave():
	print(f"\nAs you enter the cave you see the remains of an old camp, and manage to find some flint and steel hidden in an old satchel.")
	print("You get a fire started and begin to feel a little better.")
	print("You begin to explore the cave a bit more and realize you are not the only inhabitant.")
	print("Down one of the caves tunnels, you see a bear sleeping. Behind the bear is a old door.")
	print("What do you do?")
	print("Option 1 - Try to sneak past the bear as quietly as you can."
		"\nOption 2 - Try and kill the bear for some much needed food.")
	next_room = input("1 or 2: ")
	if next_room == '1':
		abandoned_mine()
	elif next_room == '2':
		print(f"You try your best to attack the bear and kill it, but the bear awoke from his sleep and with one swipe of his massive paw, dissemboweled you.")
		print(f"Sorry {name.title()} you have died.\n")
		game_over()
	

def woods_deep():
	print("Looking around the woods a bit more, you notice something.")
	print("Off to the right hidden in some tall grass you find a dead body.")
	print("Examining the body a little more you realize it is clutching a note in his left hand.")
	print("Carefully uncrumpling the note, you begin to read. Some is unreadable due to blood.")
#Follow the swamp to find a tomb, in the tomb you will find a treasure greater than any other!!
	print('The note says " Follow t-- swam- -- fi-d a tomb in the t-m- you wi-- find  a t-eas-r- greater --an an- -th-r"')
	print("What do you do now?")
	print("Option 1 - Try to make your way through the swamp.")
	print("Option 2 - You see something under the body that catches your eye, move the body?")
	next_room = input(" 1 or 2: ")
	if next_room == '1':
		print("You have made a terrible mistake... trying to make your way through the swamp,"
			" you got bit by a poisonous snake and died.")
		game_over()
	elif next_room == '2':
		secret_door()


def abandoned_mine():
	print("\n\tAs you sneak past the bear and make your way to the door, you test the door to see if it is unlocked and it is."
		"\nYou push the door open as quietly as you can, but it makes a loud creak. The bear wakes up and is in a furious rage"
		"\nfrustrated that someone has disturbed his sleep. He starts charging you! You rip the door open the rest of the way and slam it shut."
		"\nJust as the door slams shut you hear a loud thud as the bear crashes into the door. You can hear the bear let out a loud roar"
		"\non the other side. Shaking in fear,you take a few moments to gather your wits. As you do, you take some time to scan your surroundings."
		"\n'Looks like an old abandoned mine.' You can see carts and rail systems throughout the tunnels. You obviously can't go back the same"
		"\nway, so you decide to follow the tracks and see where they lead.")
	print("\tAfter a few hours of wondering around, you realize that this place is massive and complex. Tired and hungry you start to worry"
		"\nyou may die down here.")
	print("Option 1 - Continue wondering around the mines and hope you find your way out.")
	print("Option 2 - You stop to take a rest and get some sleep, hoping it will renew your strength so you can get out of here alive.")
	next_room = input("1 or 2: ")
	if next_room == '1':
		print("\tAfter wondering around for what seems like an eternity you are tired and frustrated. You take one more step and trip over a wire."
			"\n'What is that doing here' you think to yourself. Before you could finish your thought, you see some debris falling from a hole in"
			"\nthe ceiling. The debris covers you from head to toe. As you try to figure out what it is, you are bitten and stung all over your body."
			"\nYour vision begins to fade, as you realize the debris was a mound of venemous snakes, scorpions and centipedes that are now crawling"
			"\nall over you. Everything goes black.")
		game_over()
	elif next_room == '2':
		print("\tDeciding to take a break, you find an empty cart and lay down inside and take a nap. You are awakened suddenly by something you heard."
			"\nNot sure of what it was you continue listening........ eventually you hear it again. Coming from deeper in the mine, you hear someone scream."
			"\nHEEEEEEELLLLLLPPPP MEEEEEEE")
		underground_tomb()


def bandits_hideout():
	print("You have made it to the bandits_hideout.")
#
def underground_tomb():
	print("\tAs you head deeper into the labrynth to check out the screams you heard, you hear some voices in the distance"
		"\nYou quietly head closer and closer to the voices when you come to what looks like a hideout."
		"\nSitting in front of you gathered around a small fire are 3 shaggy men cooking a few rats."
		"\nYou also notice in the distance that there are 2 other men guarding a door."
		"\n'What would they be guarding down here,' you thought to yourself.")
	print("Option 1 - Try to create a distraction and slip around the strangers.")
	print("Option 2 - Ask them what they are guarding and why they are down here. ")
	print("Option 3 - Head back the way you came and check out the deeper part of the labrynth.")
	next_room_1 = input("1 or 2 or 3: ")
	if next_room_1 == '1':
		deep_tomb()
	elif next_room_1 == '2':
		print("\tAs you step out into the light and greet the strangers... you startle them and they jump to their feet and draw their weapons.")
		print("One is holding a sword, and the other has a bow and arrow.")
		print("One of them says, 'You should not have come here. Now you are going to die.'")
		print("You turn and try to run, but an arrow hits you square in the back and you fall to the ground.")
		print("The last thing you remember is one of the strangers leaning over you saying, 'Looks like you will taste really good'")
		print("Sorry you have died")
		game_over()
	elif next_room_1 == '3':
		print("\tYou decided it's not worth confronting or trying to sneak past those men, so you head back the way you came and begin"
			"\nexploring a little more. 'How am I going to get out of here?' you think to yourself.' A few moments later you see another door"
			"\nat the end of the tunnel. You make your way over to it and push it open. It's so old it just falls off the hinges and hits the"
			"\nground with a loud thud. Looking at the door a little closer you realize that even though old, the craftmanship is beautiful.")
		dungeon()


def treasure_room():
	print("\tLooking around you find mountains and mountains of treasure from golden statues, coins, and gems to tapestries, scrolls, and paintings."
		"\nAmazed, you realize this has to be one of the greatest historical finds of all time."
		"\nYou take a few more steps towards the treasure and you feel one of the floor tiles sink into the ground and then you hear"
		"\na click."
		"\nSounded like another trap!"
		"\nWhat do you do?")
	print("Option 1 - Just keep moving, and hope it was nothing. ")
	print("Option 2 - Look to see if you can gather some items to counter balance your weight and hopefully you can step of of this tile you are standing on.")
	print("Option 3 - Jump off as quickly as you can")
	next_room = input("1, 2 or 3: ")
	if next_room == '1':
		print("\tAs you take your weight off of the tile you were standing on, a golden statue depicting a god of some sorts begins shooting flames directly at you."
			"\nUnable to react quick enough, the flames engulf you.")
		game_over()
	elif next_room == '2':
		print("\tLooking around you see a few smaller statues that are made entirly of gold... doing your best to make sure you dont take any weight off of the trap,"
			"\nyou get manage to get the statue onto the same tile you are standing on and slowly take your foot off of the trap... nothing happens. That was close"
			"\nIf i get out of here alive it will be a miracle.")
		treasure_room_2()
	elif next_room == '3':
		print("\tAs quickly as you can you try to jump off of the plate and land a few feet way, as you do you trip and fall and as you land you realize you activated"
			"anyther trap. Unable to catch yourself you fall over and from both the previous area and the one you are at, a torrent of fire engulfs you as you are"
			"burned alive.")
		game_over()

def treasure_room_2():
	print("\tAs you walk through the treasure room, you do your best to avoid any more traps."
		"\nand you continue looking around at the vast amount of gold and weatlh sitting in front of you. You imagine what you could buy with such wealth."
		"\nas you walk around a large mountain of gold, further down the hall you see another door."
		"\nThe inscription over the door says:"
		"\n\nSalvation lies within"
		"\nA spoken word unseals me"
		 "\nit starts with T"
		 "\nhalfway between twins"
		 "\nthe next character lies"
		 "\nSpeak the phrase"
		 "\nand walk through the final of doorways")
	#The answer to this is kind of simple, but will probably stump a lot of people. Start out by lovating the two capital t's
	#Draw a line between them, and what ever letter falls in the middle of that line is your next letter. 
	#Then you find the next letter that matches the one you just found and draw another line to it and whatever is in the middle of that is the next letter
	#So on and so on until you find the word.... should be THRESHOLD 
	print("")
	print(" ___________________ ")
	print("|       V | V       |")
	print("|         |         |")
	print("|    E  B | R  P    |")     
	print("|         |         |")
	print("| f  P   S| N  k  N |")       
	print("|         |         |")
	print("| T  h   y| E  B  C |")       
	print("|         |         |")
	print("| S  f  ()|()  k  I |")        
	print("|         |         |")
	print("| I  O  H | R  H  G |")       
	print("|         |         |")
	print("| G  A  L | D  L  A |")        
	print("|         |         |")
	print("| g  h  c | O  T  y |")
	print("|         |         |")        
	print("| c  U  m | g  C  U |")   
	print("|___________________|")

	print("\tYou take your time to ponder the puzzle, and after a while you think you have solved it. The word is?")
	active = True
	while active:
		next_room = input("What word do you speak: ")
		if next_room.lower() == 'threshold':
			print("As you utter the word 'threshold' the door slowely begins to open. ")
			print("You have finished the game!! congrats! Would you like to play again?")
			play_again = input("y/n")
			if play_again == 'y':
				woods()
			else:
				print("Thanks for playing")
			break
		else:
			print("Nothing happens")
			continue
			
#Emilys contribution!
def dungeon():
	print("After admiring the craftmanship of the door, you look up into a dark, cold room. The only light visible in the room"
		"\nare two burning lanterns enclosing a large list of numbers on the wall. The list shows."
		"\n\n\t1"
		"\n\t11"
		"\n\t21"
		"\n\t1211"
		"\n\t111221"
		"\n\t312211")
	print("\n\n\tBelow the list of numbers lies 8 indentions in the wall with rotating circular stones. Numbers 1-9 are etched into each"
		"\nstone like a turning dial. After the dial is a small square stone that says push to enter. 'This looks like a combination lock' you think to yourself. 'I must have to finish the sequence below,'"
		"\n but how? Looking closer, you notice a small inscription above the set of numbers barely visible in the lanter light that reads:"
		"\nIntelligence alone cannot set one free. To think outside of oneself lies the key to freedom.")
	print("\n\t'Well that was helpful,' you mutter. After studying the list for what seemed like hours, you come to the realization that this"
		"\nsequence bears no mathematical pattern. 'Okay I think I got it...' you say to the thick air. You begin rolling each stone to it's"
		"\nappropriate place.")

	active = True
	while active:
		next_room = input('The next set of numbers in the sequence is: ')
		if next_room == '13112221':
			print("As you enter the number and push the button to enter it, the door opens which leads to a spiral staircase.")
			fake_burial_room()
			break
		else:
			print("Nothing happens")
			continue



	


def secret_door():
	print("\nAfter moving the body out of the way, you realize there are some rotted boards covering what looks like a well."
		"\nAs you lower yourself down the now shallow well, you enter a vast tunnel system. Upon examining"
		"\n one of the walls you notice some strange markings."
		"\nLooks like the depiction of a ritual!"
		"\nPeople gathered around what appears to be their leader, roasting a human over an open flame and then carving out the heart and eating it."
		"\nJust as you are turning to leave you hear, 'HEEEEEEELLLLLLPPPP MEEEEEEE' coming from deep within the labrinth."
		"\nWhat do you do?"
		"\nOption 1 - Travel deeper into the labrynth and try to find the source of the screams."
		"\nOption 2 - Go back out the way you came!")
	next_room = input(" 1 or 2: ")
	if next_room == '1':
		underground_tomb()
	if next_room == '2':
		print("Hearing that scream gave you a really bad feeling about this place. You decide to leave. As you are on your way out,"
				"\nyou feel something under your feet shift a little, followed by the sound of something snapping."
				"\n'It must have been a booby trap.' You begin running as fast as you can to the exit, but before you get there, the ceiling "
				"\nbegins to collapse...as the rocks fall you are crushed by the cave-in.")
		print("Sorry You have died")
		game_over()

def deep_tomb():
	print("Looking around for anything you could use as a distraction, you see an empty glass bottle partly burried in the dirt."
		"\nyou dig it up and head back to the area the strangers were. Once there, you hurl the bottle as far away from the door"
		"\nthey are guarding as you can. Startled by the breaking bottle, the 5 men look at each other and then say 'Lets check it out.'"
		"\nAnother one says, 'Maybe it is a nice tasty human and we can have a nice meal for once."
		"\nAll 5 of the men draw their weapons and head to the source of the sound. As they do, you carefully duck behind a few barrels"
		"\nand manage to stay hidden. Choosing your timing carefully, you stealthily make your way to the massive doors and head in."
		"\nSurprised by how easy that was, you lock the doors with a massive wooden brace laying on the other side, sealing yourself inside."
		"\n'No turning back now,' you whisper as you lift your eyes and survey the room you are standing in.")
	print("You behold a large stone door that has been locked and sealed. Surrounding it are two large stone statues of gods." 
		"\nDirectly in front of each statue is a stone table with a strange scale sitting on each. Each scale has a pin."
		"\nOn top of the tables are nine keys."
		"\nOn the wall it states: Eight of the keys are false and one is real."
		"\nThe false keys weigh more than the real key. Picking the wrong key will surely kill you."
		"\nWhen you place keys on the scales then remove the pin it will reveal if either side is heavier."
		"\nOnce it has determined which is heavier, it locks into place making it unuseable.")
	#Solution - Break keys into 3 sets of 3. Weigh 2 of the 3 groups, doesnt matter which one. 
	#You will have 1 of 2 outcomes 
	#1 They will be equal... which means the key is in the unweighed group.
	#2 One group is heavier than the other - key is in the lighter group cuz real key is light
	#Then with the three remaining keys you repeat the process on the second scale which tells you the correct key.
	print("You think to yourself, 'I only have 2 scales which means I only have 2 chances to find the right key."
		"\nHow can i do this... I need to think for a bit.'"
		"\nAfter thinking for a while you finally think you have figured it out.")
	print("You split the keys up into 3 groups, and weight groups 1 and 2.")
	print("The scale reveals both groups are the same weight")
	print("That means that the real key must be in group: ")
	active = True 
	while active:
		key_guess = input("1 or 2 or 3: ")
		if key_guess == '1':
			print(f"Sorry that is not correct please try again:")
			continue	
		elif key_guess == '2':
			print(f"Sorry that is not correct please try again: ")
			continue
		elif key_guess == '3':
			deep_tomb_2()
			return key_guess

def deep_tomb_2():
	print("'That makes sense because the key we want is lighter than the rest. Now I have 3 keys left and one more scale, what do I do now?'"
	"\nThinking a bit more you realize you can just repeat the process again to find the correct key."
	"\nYou look down at the keys in your hand and see keys #1, #3 and #7. One of these has to be it."
	"\nHurrying over to the second scale you put keys #1 and #7 on it to check their weight. The scale indicates that key #1"
	"\nis slightly heavier. That means that the correct key is key #: ")

	key_guess = input("1 or 3 or 7: ")
	if key_guess == '1':
		print("Grabbing key #1 you head over to the door and put the key into the lock and turn it. As soon as you turn the key"
			"\nyou know you have guessed wrong. The floor beneath you gives out and you are sliding down a long tube... a few seconds later"
			"\nyou exit into a very dark and cold room. The chute you exited out of seals shut. As you begin feeling around"
			"\nfor a door, or anything that can help, you hear a hissing noise. It is beginning to get hard to breathe. You realize that the hissing is"
			"\nthe oxygen leaving the room. You frantically begin trying to find an exit but to no avail. Your vision flickers, and you collapse"
			"\nnever to take another breath."
			"\nGAME OVER")
	elif key_guess == '2':
		print("Grabbing key #3 you head over to the door and put the key into the lock and turn it. As soon as you turn the key"
			"\nyou know you have guessed wrong. The floor beneath you gives out and you are sliding down a long tube... a few seconds later"
			"\nyou exit into a very dark and cold room. The chute you exited out of seals shut. As you begin feeling around"
			"\nfor a door, or anything that can help, you hear a hissing noise. It is beginning to get hard to breathe. You realize that the hissing is"
			"\nthe oxygen leaving the room. You frantically begin trying to find an exit but to no avail. Your vision flickers, and you collapse"
			"\nnever to take another breath."
			"\nGAME OVER")
	elif key_guess == '7':
		print("Grabbing key #7 you head over to the door and put the key in the lock and turn it. You hear a hissing and an audible click."
			"\nThe door opens with a whoosh of air and inside is a staircase heading down into another room.")
		fake_burial_room()

def fake_burial_room():
	print("As you descend the spiral stairs it opens up into a large cavern. In the middle of the cavern is a sarcophagus surrounded by what appears"
		"\nto be various gifts, coins, and jewlery, and a large table with shackels coming from the 4 corners. You step a little closer and realize the"
		"\ntable is covered in blood stains... 'Looks like they used this table for sacrifices to whomever is in this sarcophagus.' Looking around you see"
		"\nmore gold and jewlery.'Maybe this is the treasure that note was talking about' you think to yourself. You begin stuffing your pockets with as much as they can hold.")
	print("What do you do \nOption 1 - Open the sarcophagus and see who is inside")
	print("Option 2 - Look closer at the blood stained table.")
	next_room = input("1 or 2: ")
	if next_room == '1':
		print("You walk up to the sarcophagus and begin trying to open it... the lid is extremely heavy. You put your feet on the blood-stained table"
			"\nto gain some leverage and push with all your might. The lid slowly begins to slide a little. You give one more shove and the lid comes"
			"\ncrashing to the floor with a loud thud. As you look inside you see a mountain of treasure. 'How am I going to get all of this out of here?"
			"\nYou reach into the sarcophagus to pick up a beautiful necklace. As soon as your fingers touch the exquisitely crafted gold necklace, you feel"
			"\na cold chill run over you... you hear a loud blood curdling cream that makes you cover your ears. But the sound doenst diminish at all."
			"\nThe scream ends and a voice says.... 'WHOOOOO DARESSSS DISTURBBB MYYY SLEEEEEP??'"
			"\n'This sarcophagus has been cursed for centuries and all who have tried to find my treasure have perished. Your fate will be the same!'"
			"\nThe room suddenly goes silent and fear overwhelms you. You turn to run but as you turn, an invisible force seems to take hold of you."
			"\nIt lifts you into the air, and you begin to float closer and closer to the blood-stained table. With every muscle you twist and turn, but"
			"\nto no avail... the iron grip of the invisible entity slams you down onto the table. You hit the table and your head crashes down and bounces"
			"\noff its rock hard surface. Dizzy and disoriented, you look down and then up to realize the shackles have somehow been fastened around your hands and"
			"\nfeet. Suddenly, you see a dagger floating through the air which stops with its blade two feet above your heart."
			"\nYou pull as hard as you can against the shackels with the fear of death looming over your head. The dagger slowly begins moving closer and closer to your flesh."
			"\nYou scream and thrash your body with no regard as the dagger slowly enters your body.... it begins cutting and sawing through ribs"
			"\nFor some reason your body goes numb and you cant feel a thing as you watch the dagger cutting a hole in your body. Blood is flowing off"
			"\nthe edge of the table. You stare at the open hole in your chest and see your heart beating 'thump thump.... thump thump... thump thump."
			"\nA ghostly figure appears standing over you. It looks down at you and says 'Thank you for your sacrfice. It has been far too long since an unsuspecting soul"
			"\nhas wandered in here in search of my treasure.' He reaches into your chest and his fingers wrap around your heart. He begins tearing it out."
			"\nAs he does, blood squirts everywhere. 'Is this real?'' you think to yourself. 'How am i still alive?' You continue staring as you try to figure out what"
			"\nis going on. You look back at the figure as he raises your heart above his head with both hands and says, 'Tankahamun is the great power that overpowers the powers."
			"\nTankahamun is a sacred image. The most sacred image of sacred images of the great one. Whom he finds in his way, him he devours bit by bit."
			"\nAs soon as the ritual is complete he brings your heart down to his mouth and takes a massive bite! Again he looks at you with his blood-"
			"\nstained face and says,'Feel the pain Tankahamun felt and be free from the prison of your body!' Just as he finished, an explosion of pain"
			"\nerupts from your chest. You feel extremely weak as your vison fades into black.")
		game_over()
	elif next_room == '2':
		print("You walk over to the blood-stained table and inspect it. Looks like this is probably where they killed whomever is in this sarcophagus. "
			"\nThere is an inscription on the table you cannot understand, but you brush off the dust to look at it a bit better. As you brush over "
			"\none of the markings you realize it moved a little. Stopping, you rest your hand on the weird marking and press. As you press the marking, you hear"
			"\nan audible grinding noise coming from the wall on the farthest side of the cavern. Walking over, you notice a small doorway has been opened.")
		treasure_room()


def game_over():
	print("GAME OVER")
	play_again = input("y / n: ")
	if play_again == 'y':
		woods()
	

#Start Story line! DO NOT REMOVE!
woods()