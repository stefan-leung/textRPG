

from player import hero
from text import color

from items import items

default_shop_items = [
	items.potion.small_health_potion,
	items.weaponry.projectile.arrow
]

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
		print(color.bold + 'Welcome to the ' + self.name + '!' + color.stop)
		for i in self.items:
			print(i)