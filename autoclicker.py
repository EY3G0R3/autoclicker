import pynput
import time
from pynput.mouse import Button, Controller

mouse = Controller()

print ("Current position: " + str(mouse.position))

mouse.position = (250, 600)

while True:
	if mouse.position[0] < 700:
		mouse.click(Button.left, 1)
	time.sleep(0.01)