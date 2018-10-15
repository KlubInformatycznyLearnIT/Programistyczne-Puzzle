import turtle
import time
dlugosc = 50
rogi = 20
t = turtle.Pen()
t.pensize(10) #pogrubia szerokość śladu żółwia

for x in range(1, 5):
    t.forward(dlugosc)
    t.up()
    t.forward(rogi)
    t.left(90)
    t.forward(rogi)
    t.down()


time.sleep(3)