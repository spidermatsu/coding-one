# random walker
from turtle import *
import turtle as t
import random


#array of options
turns = [right, left]


  # infinite loop
while True:
    #walker makes random choice from array and turns to that direction 90 degrees
    random.choice(turns)(90)
    #walker steps forward 5 steps in given direction
    forward(5)

    