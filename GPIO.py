from gpiozero import LED
from time import sleep
led = LED(25)
f = open("words.log")
for line in f:
    # parse input, assign values to variables
    if "ON THE LIGHT" in f:
		while True:
    		led.on()
    		sleep(1)    
    		led.off()    
    		sleep(1)
    else if "OFF THE LIGHT" in f:
    		led.off()

f.close()