from gpiozero import LED
from time import sleep
led = LED(25)
f = open("words.log")
t= f.read()
print(t)
#for line in f:
    # parse input, assign values to variables
if t.find("ON THE LIGHT"):
	print("Hey\n");
	while True:
    		led.on()
    		sleep(1)    
    		led.off()    
    		sleep(1)
elif t.find("OFF THE LIGHT"):
 	led.off()

f.close()
