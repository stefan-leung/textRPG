# coding: utf-8

import sys, time, random

inventory = []

class color:
	grey = '\033[90m'
	red = '\033[91m'
	green = '\033[92m'
	yellow = '\033[93m'
	blue = '\033[94m'
	purple = '\033[95m'
	cyan = '\033[96m'

	stop = '\033[0m'
	bold = '\033[1m'
	underline = '\033[4m'

	greybg = '\033[100m'
	redbg = '\033[101m'
	greenbg = '\033[102m'
	yellowbg = '\033[103m'
	bluebg = '\033[104m'
	pinkbg = '\033[105m'
	cyanbg = '\033[106m'

	def cyanify(in_in):
		return(color.cyan + str(in_in) + color.stop)
	def greyify(in_in):
		return(color.grey + str(in_in) + color.stop)

	def dialog(dialog):
		return(color.yellow + '[' + str(dialog) + ']' + color.stop)

class icons:
	heart = '❤️ '
	shield = '🛡 '
	sword = '🗡 '
	speed = '🌀 '

class user_class:
	def __init__(self, name:str, basehp:int, basedef:int, basedmg:int, basespd:int, emoji:str):
		self.name = name
		self.basehp = basehp
		self.basedef = basedef
		self.basedmg = basedmg
		self.basespd = basespd
		self.emoji = emoji

	def printstats(self):
		print(color.purple + self.name + '\'s Stats - ' + self.emoji + color.stop)
		print(icons.heart + ' Base HP: ' + color.cyanify(self.basehp))
		print(icons.shield + ' Base Defense: ' + color.cyanify(self.basedef))
		print(icons.sword + ' Base Damage: ' + color.cyanify(self.basedmg))
		print(icons.speed + ' Base Attack Speed: ' + color.cyanify(self.basespd))

class main:
	inputtext = color.stop + color.bold + '> ' + color.stop
	def up(amount: int = 1):
		for i in range(0, amount):
			sys.stdout.write("\033[F")

	def debug():
		print(color.blue)
		print("[Debugging Information]")
		print('Current Time: ' + time.asctime() + ' ' + time.strftime("%z", time.gmtime()))
		print('Operating System: ' + sys.platform) 	# OS
		print('Python Version: ' + sys.version)		# Python Version
		print(color.stop)

class hero:
	def __init__(self, name:str=None, class_item:user_class=None):
		self.name = name
		self.c = class_item
		self.hp = class_item.basehp
		self.maxhp = class_item.basehp
		self.defense = class_item.basedef
		self.dmg = class_item.basedmg
		self.speed = class_item.basespd

	def heal(self, amount:int):
		self.hp += amount
		if self.hp > self.maxhp:
			self.hp = self.maxhp

	def damage(self, amount:int):
		self.hp -= amount
		if self.hp <= 0:
			self.hp = 0
			print('You died')

default_shop_items = [
	items.potion.small_health_potion,
	items.weaponry.projectile.arrow
]

class other:
	def __init__(self, coins:int=0):
		self.money = coins

	def lose(self, amount:int):
		self.money -= amount

		if self.money < 0:
			self.money += amount
			print(color.red + 'You can\'t afford this item!' + color.stop)

			return(False)

		else:
			return(True)

	def gain(self, amount:int):
		self.money += amount

def merchant_talk(merchants:list, text:str):
	print(color.dialog(random.choice(merchants)) + text)

c = other()

class shop:
	def __init__(self,
			name:str=None,
			items:list=default_shop_items,
			merchants:list=["Bob"],
			_inv:list=None,
			tax:float=1.0):

		self.name = name
		self.items = items
		self.merchants = merchants
		self.inv = _inv
		self.tax = tax # Out of 100

	def open(self, user:hero=None, money:int=None):
		print(color.bold + color.underline + '\nWelcome to the ' + self.name + '!' + color.stop)

		merchant_talk(self.merchants, ' Hello, ' + color.cyanify(user.name) + '! What would you like to buy today?')

		item_string = ''
		for i in self.items:
			item_string += color.cyanify(i.name) + ', '

		item_string = item_string[:-2]
		talking = True

		while talking:
			merchant_talk(self.merchants, ' We have the following items in stock: ' + item_string + color.greyify(' (Exit)'))
			print(color.greyify('You have ') + color.cyanify(money) + color.greyify(' credits.'))
			userInput = input(main.inputtext)

			if userInput.lower() == 'exit':
				if len(self.merchants) <= 1:
					merchant_talk(self.merchants, ' Thanks for doing buisness with me!')
				else:
					merchant_talk(self.merchants, ' Thanks for doing buisness with us!')

				talking = False

			else:
				for i in self.items:
					if userInput.lower() == i.name.lower():
						merchant_talk(self.merchants, ' You\'d like to buy ' + color.cyanify(i.name) + '? It will cost you ' + color.cyanify(i.price) + ' credits. ' + color.greyify('(Y/N)'))

						userInput2 = input(main.inputtext)

						if 'y' in userInput2.lower():
							money -= i.price

							if money < 0:
								money += i.price
								print(color.red + 'You can\'t afford ' + color.cyanify(i.name) + color.red + '!' + color.stop)

							else:
								merchant_talk(self.merchants, ' You bought 1 '  + color.cyanify(i.name) + '! Will that be all?')
								inventory.append(i)

						else:
							merchant_talk(self.merchants, ' Okay...')




class menu:
	def __init__(self, user:hero):
		self.user = user
	
	def open(self, location:str='Undefined', near:list=None, first:bool=False):
		a = ''
		for i in near:
			a += color.cyanify(i.name) + ', '
		
		if first:
			print(color.bold + color.underline + '\nWelcome to '  + color.cyanify(location) + color.bold + color.underline + ', ' + color.cyanify(self.user.name + ' the ' + self.user.c.name) + color.bold + color.underline + '!' + color.stop)
			print('You can go into ' + a[:-2] + '. ' + color.greyify('(Save, Inventory, Purse)'))

		else:
			print('\nYou are at ' + color.cyanify(location) + '. You can go into ' + a[:-2] + '. ' + color.greyify('(Save, Inventory, Purse)'))
	
		toGo = input(main.inputtext)
		if toGo.lower() in ['save', 'inv', 'purse']:
			if toGo.lower() == 'save':
				print('Coming Soon™')
			elif toGo.lower() == 'inv':
				print('Inventory?')
			elif toGo.lower() == 'purse':
				print('Money?')

		else:
			for i in near:
				if toGo.lower() == i.name.lower():
					print('OK SURE GO INTO ' + i.name.upper())



print('''
							  	 ,-.
							    ("O_)
							   / `-/
							  /-. /
							 /   )
						    /   /
			  _		       /-. /
			 (_)"-._	  /   )
			   "-._  "-'""( )/
				   "-/"-._" `.
					/	 "-.'._
				   /\	   /-._"-._
      _,---...__  ./  ) _,-"/	"-(_)
___<__(|) _   ""-/  / /   /
 '  `----' ""-.   \/ /   /
			   )  ] /   /
	   ____..-'   //   /					 )
   ,-""	  __.,'/   /   ___				    /,
  /	,--""/  / /   /,-""   """-.		     ,'/
 [	(	/  / /   /  ,.---,_   `._   _,-','
  \	`-./  / /   /  /	   `-._  """ ,-'
   `-._  /  / /   /_,'			""--"
	   "/  / /   /"
	   /  / /   /
	  /  / /   /	TextRPG
	 /  |,'   /
	:   /	/
	[  /   ,'   Stefan Leung & Robin Eriksson
	| /  ,'
	|/,-'
	|\'''')


main.debug()


class base_class:
	warrior = user_class(name="Warrior", basehp=100, basedef=75, basedmg=125, basespd=80, emoji='⚔️ ') # melee
	wizard = user_class(name="Wizard", basehp=125, basedef=50, basedmg=110, basespd=100, emoji='✨ ') # support
	goblin = user_class(name="Goblin", basehp=75, basedef=25, basedmg=150, basespd=110, emoji='👺 ') # brute force
	ranger = user_class(name="Ranger", basehp=75, basedef =35, basedmg=125, basespd=115, emoji='🏹 ') # ranged
	scout = user_class(name="Scout", basehp=70, basedef=30, basedmg=125, basespd=125, emoji='👟') # stealth


print('Choose your name')
userName = input(main.inputtext)

main.up(2)
print('Choose your name - ' + color.cyan + userName + color.stop)
print('Choose your class ' + color.greyify('(Warrior, Wizard, Goblin, Ranger, Scout)'))
userInput = input(main.inputtext)

user_classes = {
	"warrior": hero(name=userName, class_item=base_class.warrior),
	"wizard": hero(name=userName, class_item=base_class.wizard),
	"goblin": hero(name=userName, class_item=base_class.goblin),
	"ranger": hero(name=userName, class_item=base_class.ranger),
	"scout": hero(name=userName, class_item=base_class.scout)
}

character = user_classes[userInput.lower()]
mainmenu = menu(user=character)

main.up(2)
print('Choose your class - ' + color.cyan + character.c.emoji + ' ' +character.c.name + color.stop + (' ' * 62))

character.c.printstats()
c.money = 1000


_town_store = shop(name="Town Store", merchants=["Merchant John"])
# _town_store.open(character, money=c.money)

clothing_item = [items.clothing.leather.jacket, items.clothing.leather.pants, items.clothing.leather.boots]
_clothes_shop = shop(name="Clothes Shop", items=clothing_item, merchants=["Leather Worker", "Merchant Bob"])
# _clothes_shop.open(character, money=c.money)

mainmenu.open(location='Little Town', near=[_town_store, _clothes_shop], first=True)