from pynput import mouse, keyboard
from pynput.mouse import Button, Controller, Listener
import time

mousey = Controller()
listener = Listener()

def simpleClicker():
    time.sleep(10)
    mousey.click(Button.left, 500)

do = True
while do == True:
    print(mousey.position)
    if listener.on_click() is False:
        do = False
