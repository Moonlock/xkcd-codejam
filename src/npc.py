import player
import items

class Npc(object):
	
	def __init__(self):
		self.name = ""
		self.new = True
		self.intro = ""
		self.dialog = ""
		self.declineDialog = "'I don't need that.'"
		self.acceptDialog = ""
		self.giveDialog = ""
		self.wantedItem = None
		self.returnedItem = None

	def speak(self, player):
		print(self.name + ":")
		print (self.intro if self.new else self.dialog)
		self.new = False

	def receiveItem(self, givenItem, player):
		print(self.name + ":")
		if self.wantedItem.lower() == givenItem.name.lower():
			print (self.acceptDialog)
			self.respondToItem(player)
			return True

		print (self.declineDialog)
		return False

	def respondToItem(self, player):
		print(self.giveDialog)
		player.receiveItem(self.returnedItem)
		print(self.name + " gave you a " + self.returnedItem.name)


class BlackHat(Npc):
	def __init__(self):
		super(BlackHat,self).__init__()
		self.name = "BlackHat"
		self.intro = "'You wouldn't happen to have an extra pair of pruning shears, would you?  \nThe grand opening of the space elevator is today.'"
		self.dialog = "'I need something sharp to cut the space elevator.'"
		self.acceptDialog = "'Ah, this is perfect!  Thank you.'"
		self.giveDialog = "'You need to set the volume from command line?  \n'osascript -e \"set volume output volume 100\"'.\n" + \
						  "My girlfriend showed me that trick when she hacked into a guy's computer because he was tailgating me.'"
		self.wantedItem = "Sword"

	def respondToItem(self, player):
		print(self.giveDialog)
		player.receiveInfo()

class BeretGuy(Npc):
	def __init__(self):
		super(BeretGuy,self).__init__()
		self.name = "BeretGuy"
		self.intro = "'Did you know that the chances of a random object being a scone are about one in six?'"
		self.dialog = "'The chances of a random object being a scone are about one in six.'"
		self.acceptDialog = "'Is this a scone?  I love scones!'"
		self.giveDialog = "'Here, take this.  I have plenty.'"
		self.wantedItem = "Lint"
		self.returnedItem = items.A_loof()

class Ponytail(Npc):
	def __init__(self):
		super(Ponytail,self).__init__()
		self.name = "Ponytail"
		self.intro = "'The airline lost my luggage, so I'm missing all sorts of necessities.'"
		self.dialog = "'Do you by any chance have an extra loofa?'"
		self.acceptDialog = "'Hey, thanks!  I needed- Oh.  I thought this was a loofa.'"
		self.giveDialog = "'Here, have this anyways.'"
		self.wantedItem = "loof"
		self.returnedItem = items.Kindle()

class Megan(Npc):
	def __init__(self):
		super(Megan,self).__init__()
		self.name = "Megan"
		self.intro = "'I wish I had a Hitchhiker's Guide to the Galaxy.'"
		self.dialog = "'I wish I had a Hitchhiker's Guide to the Galaxy.'"
		self.acceptDialog = "'Eh, close enough.  Thanks.'"
		self.giveDialog = "'You can borrow my laptop, but don't spill anything on it.'"
		self.wantedItem = "Kindle"
		self.returnedItem = items.Laptop()

class Bob(Npc):
	def __init__(self):
		super(Bob,self).__init__()
		self.name = "Bob"
		self.intro = "'Alice and I are trying to organize a surprise party for Eve.'"
		self.dialog = "'It's been really hard setting this up without Eve finding out.'"
		self.acceptDialog = "'Oh, is this a message from Alice?'"
		self.giveDialog = "'Could you give her this reply for me?'"
		self.wantedItem = "Message"
		self.returnedItem = items.Reply()	

class Alice(Npc):
	def __init__(self):
		super(Alice,self).__init__()
		self.name = "Alice"
		self.intro = "'Hey, could you deliver this super-secret message to Bob for me?'"
		self.dialog = "'I'd give it to Bob myself, but I don't want Eve to know we're communicating.'"
		self.acceptDialog = "'So you managed to deliver the message without Eve noticing?  Thanks!'"
		self.giveDialog = "'You seem like a trustworthy person.  Here, have my public key.'"
		self.wantedItem = "Reply"
		self.returnedItem = items.Key()

	def speak(self, player):
		print(self.name + ":")
		if self.new:
			print(self.intro)
			message = items.Message()
			player.receiveItem(message)
			print(self.name + " gave you a " + message.name)
			self.new = False
		else:
			print(self.dialog)

class Eve(Npc):
	def __init__(self):
		super(Eve,self).__init__()
		self.name = "Eve"
		self.intro = "'I think Bob is cheating on me.  Could help me find some proof?'"
		self.dialog = "'If only I could intercept one of their messages...'"
		self.acceptDialog = "'Thanks, now I can get to the bottom of this.'"
		self.giveDialog = "'Here, have my favourite set of lockpicks.'"
		self.returnedItem = items.Lockpicks()

	def receiveItem(self, givenItem, player):
		print(self.name + ":")
		if givenItem.name.lower() == "message" or givenItem.name.lower() == "reply":
			print (self.acceptDialog)
			self.respondToItem(player)
			return True

		print (self.declineDialog)
		return False

class Stallman(Npc):
	def __init__(self):
		super(Stallman,self).__init__()
		self.name = "Stallman"
		self.intro = "'HALT, Microsoft lackey!  Free software shall live on forever!'"
		self.dialog = "'Free software will carry on!  For a GNU dawn!'"
		self.returnedItem = items.Sword()
		self.gaveSword = False

	def speak(self, player):
		print(self.name + ":")
		if self.new:
			print(self.intro)
			self.new = False
		elif not self.gaveSword:
			print("'Oh, you're not with Microsoft?'")
			print("'Take this, you'll need it to defend yourself against the RIAA and MPAA.'")
			sword = items.Sword()
			player.receiveItem(sword)
			print(self.name + " gave you a " + sword.name)
			self.gaveSword = True;
		else:
			print(self.dialog)
