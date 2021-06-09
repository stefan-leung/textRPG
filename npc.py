print('Why are you running this? It doesn\'t do anything!')

from player import hero
from text import color
from items import items
from importing import main

default_shop_items = [
	items.potion.small_health_potion,
	items.weaponry.projectile.arrow
]

import random

class money:
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

class shop:
	def __init__(self, 
			name:str=None, 
			items:list=default_shop_items, 
			merchants:list=["Bob"],
			tax:float=1.0):

		self.name = name
		self.items = default_shop_items
		self.merchants = merchants
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
			userInput = input(main.inputtext)

			if userInput.lower() == 'exit':
				if len(self.merchants) > 1:
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
								print(color.red + 'You can\'t afford ' + color.cyanify(i.name) + '!' + color.stop)
							
							else:
								merchant_talk(self.merchants, ' You bought 1 '  + color.cyanify(i.name) + '! Will that be all?')
						
						else:
							merchant_talk(self.merchants, ' Okay...')
				