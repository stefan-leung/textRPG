# print('Why are you running this? It doesn\'t do anything!')

from player import *

class items:
	class potion:
		class small_health_potion:
			name = "Small Health Potion"
			_id = "small_hp_pot"
			price = 150
			size = 1.0

			def use(user:hero=None):
				user.heal(15)


		class medium_health_potion:
			name = "Medium Health Potion"
			_id = "med_hp_pot"
			price = 300
			size = 1.5

			def use(user:hero=None):
				user.heal(30)
		
		class big_health_potion:
			name = "Big Health Potion"
			_id = "big_hp_pot"
			price = 500
			size = 3.5

			def use(user:hero=None):
				user.heal(60)

	class weaponry:
		class projectile:
			class arrow:
				name = "Arrow"
				_id = "arrow"
				price = 5
				size = 1.0
	

	class clothing:
		class leather:
			class jacket:
				name = "Leather Jacket"
				_id = "leather_jacket"
				price = 700
				size = 4
			
			class pants:
				name = "Leather Pants"
				_id = "leather_pants"
				price = 525
				size = 3

			class boots:
				name = "Leather Boots"
				_id = "leather_boots"
				price = 450
				size = 2.5