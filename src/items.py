class Item(object):

	def __init__(self, name, desc):
		self.name = name
		self.desc = desc

	def use(self, world):
		print("You can't use that here.")

	def ShowDesc(self):
		print (self.desc)

class Key(Item):
	def __init__(self):
		super(Key, self).__init__("key", "Alice told you this was her public key, but it's just a physical key.")

	def use(self, world):
		if(world.curRoom.name == "In front of Stallman's house"):
			world.unlockStallman()
			print("You unlock the door.")
		else:
			print("You can't use that here.")