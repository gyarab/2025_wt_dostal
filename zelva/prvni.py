from math import sqrt
from random import randint
from turtle import forward, left, right, exitonclick

def domecek(a):
    c = sqrt(2) * 2
    forward(a)
    left(90)
    forward(a)
    left(90)
    forward(a)
    left(90)
    forward(a)
    left(90)
    forward(a)

for i in range(10):
    domecek(randint(30, 50))
    right(36)


exitonclick()