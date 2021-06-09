

from player import hero
from text import color
from items import items
from importing import main

default_shop_items = [
	items.potion.small_health_potion,
	items.weaponry.projectile.arrow
]

import random

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
	
	def open(self, user:hero=None):
		print(color.bold + color.underline + '\nWelcome to the ' + self.name + '!' + color.stop)
		print(color.dialog(random.choice(self.merchants)) + ' Hello, ' + color.cyanify(user.name) + '! What would you like to buy today?')

		item_string = ''
		for i in self.items:
			item_string += color.cyanify(i.name) + ', '
		
		item_string = item_string[:-2]
		talking = True
		
		while talking:
			print(color.dialog(random.choice(self.merchants)) + ' We have the following items in stock: ' + item_string)
			userInput = input(main.inputtext)

			done = False
			for i in self.items:
				if userInput.lower() == i.name.lower():
					print(color.dialog(random.choice(self.merchants)) + ' You\'d like to buy ' + color.cyanify(i.name) + '? It will cost you ' + color.cyanify(i.price) + ' credits. ' + color.greyify('(Y/N)'))

					userInput2 = input(main.inputtext)

					if 'y' in userInput2.lower():
						buy = True
						user.money -= i.price

						if user.money < 0:
							user.money += i.price
							print(color.red + 'You can\'t afford ' + color.cyanify(i.name) + '!' + color.stop)
					
					else:
						print(color.dialog(random.choice(self.merchants)) + 'Okay...')
				