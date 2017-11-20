class Npc(object):
	
	def __init__(self):
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


class BeretGuy(Npc):

	def __init__(self):
		self.intro = ""
		self.dialog = ""
		self.acceptItem = ""
		self.declineItem = ""

	
