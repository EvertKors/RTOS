import time
import RPi.GPIO as gpio
gpio.setmode(gpio.BCM)
gpio.setup(4, gpio.IN)

read = 0
state = True
print time.time()
milis = int(round(time.time() * 1000))
while True:
    # Get the current state
    r = bool(gpio.input(4))
    # Check if state changed
    d = state ^ r
    if d:
    	state = not state
	read+=1

    if read >= 1000000:
        break
milis = int(round(time.time() * 1000)) - milis

print time.time()
print("milis", milis)

