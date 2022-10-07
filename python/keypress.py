from pynput.keyboard import Key, Controller
import time

keyboard = Controller()

key = 't'

text = "https://youtube.com"

# keyboard.press(key)
# keyboard.release(key)

def shortcut(k1, k2):
    keyboard.press(k1)
    keyboard.press(k2)
    keyboard.release(k2)
    keyboard.release(k1)

keyboard.press(Key.cmd)
keyboard.release(Key.cmd)

"""
shortcut(Key.alt, Key.tab)
shortcut(Key.ctrl, "t")

time.sleep(0.5)
for char in text:
    keyboard.press(char)
    keyboard.release(char)
    time.sleep(0.12)

keyboard.press(Key.enter)
keyboard.release(Key.enter)
"""
