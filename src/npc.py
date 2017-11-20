class Npc(object):
	
	def __init__(self):
		self.name = ""
		self.new = True
		self.intro = ""
		self.dialog = ""
		self.declineDialog = ""
		self.acceptDialog = ""
		self.giveDialog = ""
		self.wantedItem = None
		self.returnedItem = None

	def speak(self):
		print (self.intro if self.new else self.dialog)
		self.new = False

	def ReceiveItem(self,givenItem):
		if self.item == givenItem:
			print (self.acceptDialog)
			self.giveItem()
		else:
			print (self.declineDialog)

	def giveItem(self):
		print(self.giveDialog)


class BlackHat(Npc):
	def __init__(self):
		super(BlackHat,self).__init__()
		self.name = "Black Hat"
		self.new = True
		self.intro = ""
		self.dialog = ""
		self.declineDialog = ""
		self.acceptDialog = ""
		self.giveDialog = ""
		self.wantedItem = "Sword"

class BeretGuy(Npc):
	def __init__(self):
		super(BeretGuy,self).__init__()
		self.name = "Beret guy"
		self.new = True
		self.intro = ""
		self.dialog = ""
		self.declineDialog = ""
		self.acceptDialog = ""
		self.giveDialog = ""
		self.wantedItem = "Lint"
		self.returnedItem = "A loof"

class Ponytail(Npc):
	def __init__(self):
		super(Ponytail,self).__init__()
		self.name = "Ponytail"
		self.new = True
		self.intro = ""
		self.dialog = ""
		self.declineDialog = ""
		self.acceptDialog = ""
		self.giveDialog = ""
		self.wantedItem = "A loof"
		self.returnedItem = "Kindle"	

class Megan(Npc):
	def __init__(self):
		super(Megan,self).__init__()
		self.name = "Megan"
		self.new = True
		self.intro = ""
		self.dialog = ""
		self.declineDialog = ""
		self.acceptDialog = ""
		self.giveDialog = ""
		self.wantedItem = "Kindle"
		self.returnedItem = "Laptop"

class Bob(Npc):
	def __init__(self):
		super(Bob,self).__init__()
		self.name = "Bob"
		self.new = True
		self.intro = ""
		self.dialog = ""
		self.declineDialog = ""
		self.acceptDialog = ""
		self.giveDialog = ""
		self.wantedItem = "Message"
		self.returnedItem = "Reply"		

class Alice(Npc):
	def __init__(self):
		super(Alice,self).__init__()
		self.name = "Alice"
		self.new = True
		self.intro = ""
		self.dialog = ""
		self.declineDialog = ""
		self.acceptDialog = ""
		self.giveDialog = ""
		self.wantedItem = "Reply"
		self.returnedItem = "Key"

class Eve(Npc):
	def __init__(self):
		super(Eve,self).__init__()
		self.name = "Eve"
		self.new = True
		self.intro = ""
		self.dialog = ""
		self.declineDialog = ""
		self.acceptDialog = ""
		self.giveDialog = ""
		self.wantedItem = ["Message","Reply"]
		self.returnedItem = "Lockpicks"
