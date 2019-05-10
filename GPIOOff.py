from gpiozero import LED
from time import sleep
led = LED(25)
f = open("hi.txt")
t= f.read()
print(t)
led.on()
sleep(1)
#for line in f:
    # parse input, assign values to variables
if t.find("OFF THE LIGHT"):
	print("Hey\n");
	#while True: 
    		#sleep(1)
	led.off()
	sleep(5)

f.close()