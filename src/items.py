class Item(object):

	def __init__(self, name, desc):
		self.name = name
		self.desc = desc

	def use(self, world):
		print("You can't use that here.")

	def printDescription(self):
		print (self.desc)

class Key(Item):
	def __init__(self):
		super(Key, self).__init__("key", "Alice told you this was her public key, but it's just a physical key.")

	def use(self, world):
		if(world.curRoom.name == "In front of Stallman's house"):
			world.unlockStallman()
		else:
			print("You can't use that here.")

class A_loof(Item):
	def __init__(self):
		super(A_loof,self).__init__("loof","You have no idea what this is, but something tells you it wants to escape your grasp.")

class Sword(Item):
	def __init__(self):
		super(Sword,self).__init__("sword","A mystical weapon bestowed upon you by Stallman.")
		
class Message(Item):
	def __init__(self):
		super(Message,self).__init__("message","A message for Bob. Eve might be interested in this.")

class Reply(Item):
	def __init__(self):
		super(Reply,self).__init__("reply","A message from Bob to Alice. Eve might want this.")

class Laptop(Item):
	def __init__(self):
		super(Laptop,self).__init__("laptop","Megan's Laptop. It's covered with stickers.")	

	def use(self, world):
		if(world.curRoom.name == "In front of Cueball's apartment"):
			world.unlockCueball()
		else:
			print("You can't use that here.")

class Kindle(Item):
	def __init__(self):
		super(Kindle,self).__init__("Kindle","A wholly remarkable electronic Book.")			

class Lockpicks(Item):
	def __init__(self):
		super(Lockpicks,self).__init__("lockpicks","Eve gave you these lockpicks. You get the feeling she has plenty.")
	def use(self, world):
		if(world.curRoom.name == "In front of Stallman's house"):
			world.unlockStallman()
			print("You pick the lock to Stallman's door.  You hope he won't mind.")
		else:
			print("You can't use that here.")

class Lint(Item):
	def __init__(self):
		super(Lint,self).__init__("lint","A bit of lint you found in your pocket. Hopefully someone wants this because its all you have.")	
