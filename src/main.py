import world
import player

# Fix input() vs raw_input() mess
try: input = raw_input
except NameError: pass

def printHelp():
	print("")
	print("Commands:")
	print("	go	[exit]")
	print("	n/e/s/w")
	print("	l/look")
	print("	l/look	[item/npc]")
	print("	talk	[npc]")
	print("	get	[item]")
	print("	give	[item] [npc]")
	print("	i/inv")
	print("	help")
	print("	quit")

def go(arg):
	if arg == "":
		print("Go where?")
	else:
		world_obj.move(arg)

def look(arg):
	if arg == "":
		world_obj.displayRoom()
	else:
		world_obj.look(arg, player_obj)

def get(arg):
	if arg == "":
		print("Get what?")
	else:
		player_obj.pickUpItem(arg)

def quit():
	print('Goodbye!')
	exit()

def parseCommand(command, arg=""):
	if command == "go": go(arg)
	elif command == "n": go("north")
	elif command == "s": go("south")
	elif command == "e": go("east")
	elif command == "w": go("west")

	elif (command == "l") or (command == "look"): look(arg)

	elif command == "get": get(arg)

	elif (command == "i") or (command == "inv"): player_obj.displayInventory()
	elif command == "help": printHelp()
	
	elif command == "quit": quit()
	else:
		print("...")


name = input("Please enter your name: ")
world_obj = world.World()
player_obj = player.Player(world_obj, name)

print("")
print("Greetings, " + name + "!")
print("Type 'help' for help.")

while(True):
	print("")

	command = input(">> ").split(" ")
	if len(command) == 2:
		parseCommand(command[0], command[1])
	else:
		parseCommand(command[0])
