from text import color, icons

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


class hero:
	def __init__(self, name:str=None, class_item:user_class=None, money:int=None):
		self.name = name
		self.c = class_item
		self.hp = class_item.basehp
		self.maxhp = class_item.basehp
		self.defense = class_item.basedef
		self.dmg = class_item.basedmg
		self.speed = class_item.basespd
		self.money = money
	
	def heal(self, amount:int):
		self.hp += amount
		if self.hp > self.maxhp:
			self.hp = self.maxhp
	
	def damage(self, amount:int):
		self.hp -= amount
		if self.hp <= 0:
			self.hp = 0
			print('You died')

	'''
	class money:
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
	'''