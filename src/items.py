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

class A_loof(Item):
	def __init__(self):
		super(A_loof,self).__init__("A loof","You have no idea what this is, but something tells you it wants to escape your grasp.")

class Sword(Item):
	def __init__(self):
		super(Sword,self).__init__("Sword","A mystical weapon bestowed upon you by Stallman.")
		
class Message(Item):
	def __init__(self):
		super(Message,self).__init__("Message","A message for Bob. Eve might be interested in this.")	

class Reply(Item):
	def __init__(self):
		super(Reply,self).__init__("Reply","A message from Bob to Alice. Eve might want this.")

class Laptop(Item):
	def __init__(self):
		super(Laptop,self).__init__("Laptop","Megan's Laptop. It's covered with stickers.")	

class Kindle(Item):
	def __init__(self):
		super(Kindle,self).__init__("Kindle","Wholly remarkable! An electronic Book.")			

class Lockpicks(Item):
	def __init__(self):
		super(Lockpicks,self).__init__("Lockpicks","Eve gave you these lockpicks. You get the feeling she has plenty.")

class Lint(Item):
	def __init__(self):
		super(Lint,self).__init__("Lint","A bit of lint you found in your pocket. Hopefully someone wants this because its all you have.")	

