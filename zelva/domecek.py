from math import sqrt
from random import randint
from turtle import forward, left, right, exitonclick

def domecek(a):
    c = sqrt(2 * a**2)
    left(90)
    forward(a)
    right(90)
    forward(a)
    right(135)
    forward(c)
    left(135)
    forward(a)
    left(90)
    forward(a)
    left(45)
    forward(c/2)
    left(90)
    forward(c/2)
    left(90)
    forward(c)
    
for i in range(5):
    domecek(randint(30, 50))
    right(36)

exitonclick()