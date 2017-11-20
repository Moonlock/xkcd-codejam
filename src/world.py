from __future__ import print_function
import string
import random

import items
import npc

# Fix input() vs raw_input() mess
try: input = raw_input
except NameError: pass

class World:

	class Room:
		def __init__(self):
			self.name = ""
			self.desc = ""
			self.exits = []
			self.npcs = []
			self.items = []
			self.isLocked = False

	def __init__(self):
		self.rooms = []
		self.createRooms()

	def move(self, newRoom):
		for exit in self.curRoom.exits:
			if string.find(exit['localName'].lower(), newRoom.lower()) == 0:
				if exit['room'].isLocked:
					print("It's locked.")
					return
				else:
					self.curRoom = exit['room']
					self.displayRoom()
				return
		print("You can't go that way.")

	def displayRoom(self):
		print("")
		print(self.curRoom.name)
		print(self.curRoom.desc)

		self.displayExits()
		self.displayItems()
		self.displayNpcs()

	def displayExits(self):
		print("Exits: ", end="")
		for exit in self.curRoom.exits[:-1]:
			print(exit['localName'] + ", ", end="")
		print(self.curRoom.exits[-1]['localName'] + ".")

	def displayItems(self):
		if not self.curRoom.items:
			return

		print("Items: ", end="")
		self.displayList(self.curRoom.items)

	def displayNpcs(self):
		if not self.curRoom.npcs:
			return

		print("You see: ", end="")
		self.displayList(self.curRoom.npcs)

	def displayList(self, myList):
		for element in myList[:-1]:
			print(element.name + ", ", end="")
		print(myList[-1].name + ".")

	def lookNpc(self, npcName):
		npc = self.getNpc(npcName)
		if npc != None:
			npc.printDescription()
			return True
		return False

	def lookGround(self, itemName):
		item = self.getItem(itemName)
		if item != None:
			item.printDescription()
			return True
		return False

	def getItem(self, itemName):
		for item in self.curRoom.items:
			if string.find(item.name, itemName) == 0:
				return item
		return None

	def removeItem(self, item):
		self.curRoom.items.remove(item)

	def getNpc(self, npcName):
		for npc in self.curRoom.npcs:
			if string.find(npc.name, npcName) == 0:
				return npc
		return None

	def unlockStallman(self):
		self.stallmanHouse.isLocked = False

	def unlockCueball(self):
		self.cueballHouse.isLocked = False

	def createRooms(self):
		meganHouse = self.Room()
		self.stallmanHouse = self.Room()
		self.cueballHouse = self.Room()
		street0_0 = self.Room()
		street0_1 = self.Room()
		street0_2 = self.Room()
		street1_0 = self.Room()
		street1_2 = self.Room()
		street2_0 = self.Room()
		street2_1 = self.Room()
		street2_2 = self.Room()
		street2_3 = self.Room()
		street3_0 = self.Room()
		street3_1 = self.Room()
		street3_2 = self.Room()
		street3_3 = self.Room()
		street4_1 = self.Room()
		street4_2 = self.Room()

		meganHouse.name = "Megan's house"
		meganHouse.desc = "The entire house is filled waist deep in playpen balls.  Megan stands in a corner, throwing balls across the room.  She seems to be sorting them by colour."
		meganHouse.exits.append({"room": street0_0, "localName": "out"})

		self.stallmanHouse.name = "Richard Stallman's house"
		self.stallmanHouse.desc = ""
		self.stallmanHouse.exits.append({"room": street0_1, "localName": "out"})
		self.stallmanHouse.isLocked = True

		self.cueballHouse.name = "Cueball's house"
		self.cueballHouse.desc = "You have finally made it inside.  Congratulations!"
		self.cueballHouse.exits.append({"room": street0_2, "localName": "out"})
		self.cueballHouse.isLocked = True

		street0_0.name = "In front of Megan's house"
		street0_0.desc = "You stand on the street in front of Megan's house."
		street0_0.exits.append({"room": meganHouse, "localName": "house"})
		street0_0.exits.append({"room": street0_1, "localName": "east"})
		street0_0.exits.append({"room": street1_0, "localName": "south"})

		street0_1.name = "In front of Stallman's house"
		street0_1.desc = "You stand on the street in front of Richard Stallman's house."
		street0_1.exits.append({"room": self.stallmanHouse, "localName": "house"})
		street0_1.exits.append({"room": street0_2, "localName": "east"})
		street0_1.exits.append({"room": street0_0, "localName": "west"})
		street0_1.items.append(items.Key())

		street0_2.name = "In front of Cueball's house"
		street0_2.desc = "You stand on the street in front of your house."
		street0_2.exits.append({"room": self.cueballHouse, "localName": "house"})
		street0_2.exits.append({"room": street0_1, "localName": "west"})
		street0_2.exits.append({"room": street1_2, "localName": "south"})

		self.curRoom = street0_2
