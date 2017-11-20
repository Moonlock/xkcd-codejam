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
	print("	use	[item]")
	print("	give	[item] [npc]")
	print("	i/inv")
	print("	help")
	print("	quit")

def go(exit):
	if exit == "":
		print("Go where?")
	else:
		world_obj.move(exit)

def look(target):
	if target == "":
		world_obj.displayRoom()
	else:
		player_obj.look(target)

def talkTo(npc):
	if npc == "":
		print("Talk to whom?")
	else:
		world_obj.talkTo(npc)

def get(item):
	if item == "":
		print("Get what?")
	else:
		player_obj.pickUpItem(item)

def use(arg):
	if arg == "":
		print("Use what?")
	else:
		player_obj.use(arg)

def give(item, npc):
	if item == "":
		print("Give what?")
	elif npc == "":
		print("Give to whom?")
	else:
		player_obj.give(item, npc)

def quit():
	print('Goodbye!')
	exit()

def parseCommand(command, arg1="", arg2=""):
	if command == "go": go(arg1)
	elif command == "n": go("north")
	elif command == "s": go("south")
	elif command == "e": go("east")
	elif command == "w": go("west")

	elif (command == "l") or (command == "look"): look(arg1)
	elif command == "talk": talkTo(arg1)
	elif (command == "i") or (command == "inv"): player_obj.displayInventory()
	elif command == "get": get(arg1)
	elif command == "give": give(arg1, arg2)
	elif command == "use": use(arg1)

	elif command == "help": printHelp()
	elif command == "quit": quit()
	else:
		print("...")

def getArg(command, argNum):
	if(len(command) > argNum):
		return command[argNum]
	return ""

world_obj = world.World()
player_obj = player.Player(world_obj)

print("")
print("Welcome to an xkcd adventure.")
print("Type 'help' for a list of commands.")

while(True):
	print("")

	command = input(">> ").split(" ")
	parseCommand(command[0], getArg(command, 1), getArg(command, 2))
