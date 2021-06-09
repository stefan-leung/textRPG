print("""								,-.
							   ("O_)
							  / `-/
							 /-. /
							/   )
						   /   /  
			  _		   /-. /
			 (_)"-._	 /   )
			   "-._ "-'""( )/	
				   "-/"-._" `. 
					/	 "-.'._
				   /\	   /-._"-._
	_,---...__	/  ) _,-"/	"-(_)
___<__(|) _   ""-/  / /   /
 '  `----' ""-.   \/ /   /
			   )  ] /   /
	   ____..-'   //   /					 )
   ,-""	  __.,'/   /   ___				    /,
  /	,--""/  / /   /,-""   \"\"\"-.		     ,'/
 [	(	/  / /   /  ,.---,_   `._   _,-','
  \	`-./  / /   /  /	   `-._  \"\"\" ,-'
   `-._  /  / /   /_,'			""--"
	   "/  / /   /"		 
	   /  / /   /
	  /  / /   /	TextRPG
	 /  |,'   /  
	:   /	/
	[  /   ,'   Stefan Leung & Robin Eriksson
	| /  ,'
	|/,-'
	|'""")


from text import color, icons
from importing import main
from player import *
from npc import *


main.debug()

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
	def __init__(self, name:str, class_item:user_class):
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

	
class base_class:
	warrior = user_class(name="Warrior", basehp=100, basedef=75, basedmg=125, basespd=80, emoji='⚔️ ') # melee
	wizard = user_class(name="Wizard", basehp=125, basedef=50, basedmg=110, basespd=100, emoji='✨ ') # support
	goblin = user_class(name="Goblin", basehp=75, basedef=25, basedmg=150, basespd=110, emoji='👺 ') # brute force
	ranger = user_class(name="Ranger", basehp=75, basedef =35, basedmg=125, basespd=115, emoji='🏹 ') # ranged
	scout = user_class(name= "Scout", basehp=70, basedef=30, basedmg=125, basespd=125, emoji='👟') # stealth


print('Choose your name.')
userName = input(main.inputtext)

main.up(2)
print('Choose your name - ' + color.cyan + userName + color.stop)
print('Choose your class ' + color.greyify('(Warrior, Wizard, Goblin, Ranger, Scout)'))
userInput = input(main.inputtext)

user_classes = {
	"warrior": hero(name=userName, class_item=base_class.warrior, money=0),
	"wizard": hero(name=userName,class_item=base_class.wizard, money=0),
	"goblin": hero(name=userName, class_item=base_class.goblin, money=0),
	"ranger": hero(name=userName, class_item=base_class.ranger, money=0),
	"scout": hero(name=userName, class_item=base_class.scout, money=0)
}

character = user_classes[userInput.lower()]

main.up(2)
print('Choose your class - ' + color.cyan + character.c.emoji + ' ' +character.c.name + color.stop + (' ' * 62))

character.c.printstats()

town_store = shop(name="Town Store", merchants=["Merchant John"])
town_store.open(character)