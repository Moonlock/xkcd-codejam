from __future__ import print_function
import string

# Fix input() vs raw_input() mess
try: input = raw_input
except NameError: pass

class Player:

	def __init__(self, world):
		self.world = world

		self.items = []

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
		if self.world.lookNpc(targetName) == True:
			return
		if self.world.lookGround(targetName) == True:
			return
		if self.lookInventory(targetName) == True:
			return

		print("That is not here.")

	def pickUpItem(self, itemName):
		item = self.world.getItem(itemName)
		if item is not None:
			self.items.append(item)
			self.items = sorted(self.items, key=lambda k: k.name)
			self.world.removeItem(item)
			print("You pick up the " + item.name + ".")
		else:
			print("That is not here.")

	def use(self, itemName):
		item = self.getItem(itemName)
		if item is None:
			print("You don't have that.")
			return False

		item.use(self.world)
		return True

	def getItem(self, itemName):
		for item in self.items:
			if string.find(item.name, itemName) == 0:
				return item
		return None

	def removeItem(self, item):
		self.items.remove(item)

	def lookInventory(self, itemName):
		item = self.getItem(itemName)
		if item is not None:
			item.printDescription()
			return True
		return False