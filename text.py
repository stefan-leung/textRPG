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
	