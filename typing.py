'''simulates keyboard presses. To other applications it will seem that a human is typing.'''

from pynput.keyboard import Key, Controller
import time

def type_now(string):
    time.sleep(3)
    keyboard = Controller()
    for char in string:
        if char == '\n':
            keyboard.press(Key.enter)
            keyboard.release(Key.enter)
        else:   
            keyboard.press(char)
            keyboard.release(char)
            time.sleep(0.12)

