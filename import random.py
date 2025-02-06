import random

# @python.coder_

import pyautogui as pg

import time

animal=('monkey','donkey','dog')

time.sleep(8)

for i in range(500):
 a=random.choice(animal)
pg.write("You are a"+a)
pg.press("Enter")