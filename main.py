print("\n \n If you are an explorer on repl.it, running this takes a bit more work.  First, type this into the command box below (Next to the red arrow)    python3 -m poetry install      After this is completely finished, type this command to run it      python3 main.py     Type the commands word for word. \n \n")


import pgzrun
import pygame
from random import randint
import time

WIDTH = 600
HEIGHT = 600
apple = Actor("apple")
pineapple = Actor("pineapple")
orange = Actor("orange")
end = Actor("end")

t0 = time.time()

x = -1

timer = 60

def draw():
    screen.clear()
    apple.draw()
    pineapple.draw()
    orange.draw()

def place_apple():
    apple.x = randint(10, 500)
    apple.y = randint(10, 400)

def place_pineapple():
    pineapple.x = randint(20, 550)
    pineapple.y = randint(30, 400)

def place_orange():
    orange.x = randint(20, 600)
    orange.y = randint(30, 400)


def on_mouse_down(pos):
    if apple.collidepoint(pos):
        if timer > 0:
          print("Good Shot!")
          global x
          global y
          x = x + 1
          y = x + 1
          print(y)
          place_apple()
    elif pineapple.collidepoint(pos):
        if timer > 0:
          print("Good Shot!")
          x = x + 2
          y = x + 1
          print(y)
          place_pineapple()
    elif orange.collidepoint(pos):
        if timer > 0:
          print("Better Luck Next Time!")
          x = x - 3
          y = x + 1
          print(y)
          place_orange()


def delay():
    clock.schedule_unique(place_apple, 0.5)
    clock.schedule_unique(place_pineapple, 0.5)
    clock.schedule_unique(place_orange, 0.6)
         
       


clock.schedule_interval(delay, 1)

#def timerless():
#    global timer
#    timersaid = False
#    if timer == 0 and timersaid == False:
#        gameover = True
#        timersaid = True
#        print("Game Over")
#    else:
#        timer -= 1
#        print(timer)
#        clock.schedule_interval(delay, 1)
#        clock.schedule_interval(timerless, 1)

#timerless()




pgzrun.go()
