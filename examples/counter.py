
from machine import SPI, Pin

from hV_Screen import Screen
from hV_Fonts import Font

import time

spi = SPI(0, 8_000_000, sck=Pin(18), mosi=Pin(19), miso=Pin(16))

myScreen = Screen(
    #pico spi pins
    spi, cs = 17,
    #display control pins
    reset = 11, dc = 12, busy = 13,
    #display resolution
    screenW = 416, screenH = 240)
    
myScreen.begin()
myScreen.regenerate()
myScreen.setOrientation(3)
myScreen.selectFont(2)

#clear existing text
myScreen.setFontSolid(True)

count = 0

while(1):
    myScreen.gText(10, 10, str(count))
    count += 1
    time.sleep(1)
    myScreen.flush()
