import time
import usb_hid
from adafruit_hid.keycode import Keycode
from adafruit_hid.keyboard import Keyboard
import board
import digitalio


btn1_pin = board.GP16
btn2_pin = board.GP15
btn3_pin = board.GP17
btn4_pin = board.GP14

btn1 = digitalio.DigitalInOut(btn1_pin)
btn1.direction = digitalio.Direction.INPUT
btn1.pull = digitalio.Pull.DOWN

btn2 = digitalio.DigitalInOut(btn2_pin)
btn2.direction = digitalio.Direction.INPUT
btn2.pull = digitalio.Pull.DOWN

btn3 = digitalio.DigitalInOut(btn3_pin)
btn3.direction = digitalio.Direction.INPUT
btn3.pull = digitalio.Pull.DOWN

btn4 = digitalio.DigitalInOut(btn4_pin)
btn4.direction = digitalio.Direction.INPUT
btn4.pull = digitalio.Pull.DOWN

keyboard = Keyboard(usb_hid.devices)

while True:
    if btn1.value:
        keyboard.press(Keycode.CONTROL, Keycode.F7)
        keyboard.release(Keycode.CONTROL, Keycode.F7)
        print("bt1")
        time.sleep(0.1)
    if btn2.value:
        keyboard.press(Keycode.CONTROL, Keycode.F8)
        keyboard.release(Keycode.CONTROL, Keycode.F8)
        print("bt2")
        time.sleep(0.1)
    if btn3.value:
        keyboard.press(Keycode.CONTROL, Keycode.F9)
        keyboard.release(Keycode.CONTROL, Keycode.F9)
        print("bt3")
        time.sleep(0.1)
    if btn4.value:
        keyboard.press(Keycode.CONTROL, Keycode.F10)
        keyboard.release(Keycode.CONTROL, Keycode.F10)
        print("bt4")
        time.sleep(0.1)
