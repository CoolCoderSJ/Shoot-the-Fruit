import pgzrun
from random import randint
WIDTH = 800
HEIGHT = 800
apple = Actor("apple")
pineapple = Actor("pineapple")
redball = Actor("redball")
x = -1

def draw():
    screen.clear()
    apple.draw()
    pineapple.draw()

def place_apple():
    apple.x = randint(10, 600)
    apple.y = randint(10, 800)

def place_pineapple():
    pineapple.x = randint(20, 700)
    pineapple.y = randint(30, 600)

def on_mouse_down(pos):
    if apple.collidepoint(pos):
        print("Good Shot!")
        global x
        global y
        x = x + 1
        y = x + 1
        print(y)
        place_apple()
    elif pineapple.collidepoint(pos):
        print("Good Shot!")
        x = x + 2
        y = x + 1
        print(y)
        place_pineapple()
    elif print("Better Luck Next Time!"):
        place_apple()


    
pgzrun.go()
