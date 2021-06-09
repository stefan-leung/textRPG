from text import color
import sys, time
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