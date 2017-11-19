class Npc(object):
	
	def __init__(self):
		self.new = True
		self.intro = ""
		self.dialog = ""
		self.acceptItem = ""
		self.giveItem = ""
		self.declineItem = ""
		self.wantedItem = None
		self.returnedItem = None

	def speak(self):
		print (self.intro if self.new else self.dialog)
		self.new = False

	def ReceiveItem(self,givenItem):
		if self.item == givenItem
			print (self.acceptItem)
			self.giveItem()
		else 
			print (self.declineItem)

	def giveItem(self):
		print(self.giveItem)


class BeretGuy(Npc):

	def __init__(self):
		self.intro = ""
		self.dialog = ""
		self.acceptItem = ""
		self.declineItem = ""

	
