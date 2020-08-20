#Import adafruit motorkit
from adafruit_motorkit import MotorKit
kit = MotorKit()
#import adafruit stepper kit
from adafruit_motor import stepper
#import date and time
from datetime import datetime
#import time to pause, so we don't check so often
import time

while True:
	#wait minute between time checks, reduces checks
	time.sleep(60)
	#set a variable to current time
	now = datetime.now()
	#Organize current time and remove excess date info 
	current_hour = now.strftime("%H: %M")
	print (current_hour)
	#On to the motor stuff

	if current_hour == "07: 00":
		print ("Motor moving!")
		#First loop moves motor forward 100 steps, next loop resets it
		for i in range(0,100):
			i=i+1
			kit.stepper1.onestep(direction=stepper.BACKWARD, style=stepper.DOUBLE)
		for i in range(0,100):
			i=i+1
			kit.stepper1.onestep(style=stepper.DOUBLE)
		#releases motor so it's not pulling power
		kit.stepper1.release()
	else:
		print ("Not 7!")
