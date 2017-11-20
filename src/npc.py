import player
import items

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
		if self.wanteditem == givenItem.name:
			print (self.acceptDialog)
			self.removeItem()
			self.giveItem()
		else:
			print (self.declineDialog)

	def giveItem(self):
		print(self.giveDialog)
		player.ReceiveItem(self.returnedItem)


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
		self.returnedItem = items.A_loof()

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
		self.returnedItem = items.Kindle()

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
		self.returnedItem = items.Laptop()

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
		self.returnedItem = items.Reply()	

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
		self.returnedItem = items.Key()

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
		self.wantedItem = ["Message", "Reply"]
		self.returnedItem = items.Lockpicks()

class Stallman(Npc):
	def __init__(self):
		super(Stallman,self).__init__()
		self.name = "Stallman"
		self.intro = ""
		self.dialog = ""
		self.declineDialog = ""
		self.acceptDialog = ""
		self.giveDialog = ""
		self.wantedItem = []
		self.returnedItem = items.Sword()
