from __future__ import print_function
import string

import npc
import items

# Fix input() vs raw_input() mess
try: input = raw_input
except NameError: pass

class Player:

	def __init__(self, world):
		self.world = world

		self.items = [items.Lint()]

	def displayInventory(self):
		print("")
		if not self.items:
			print("You have no items.")
			return

		print("You have: ", end="")
		for item in self.items[:-1]:
			print(item.name + ", ", end="")
		print(self.items[-1].name + ".")

	def look(self, targetName):
		if self.world.lookGround(targetName) == True:
			return
		if self.lookInventory(targetName) == True:
			return

		print("That is not here.")

	def receiveItem(self, item):
		item = self.items.append(item)

	def use(self, itemName):
		item = self.getItem(itemName)
		if item is None:
			print("You don't have that.")
			return False

		item.use(self.world)
		return True

	def getItem(self, itemName):
		for item in self.items:
			if string.find(item.name.lower(), itemName.lower()) == 0:
				return item
		return None

	def lookInventory(self, itemName):
		item = self.getItem(itemName)
		if item is not None:
			item.printDescription()
			return True
		return False

	def give(self,itemName,npcName):
		item = self.getItem(itemName)
		if item is None:
			print("You don't have that item to give.")
			return

		npc = self.world.getNpc(npcName)
		if npc is None:
			print("That person isn't here.")
			return

		if npc.receiveItem(item, self):
			self.items.remove(item)

	def talkTo(self, npcName):
		npc = self.world.getNpc(npcName)
		if npc is not None:
			npc.speak(self)
		else:
			print("That person is not here.")

	def receiveInfo(self):
		self.world.hasInfo = True
