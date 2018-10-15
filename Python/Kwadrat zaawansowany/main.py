import turtle
import time
kwadraty = int(input("Wpisz liczbe kwadratow: "))
dlugosc = 50
rogi = 20
t = turtle.Pen()
t.pensize(10) #pogrubia szerokość śladu żółwia
for i in range(1, kwadraty+1):
    for x in range(1, 5):
        t.forward(dlugosc*i)
        t.up()
        t.forward(rogi*i)
        t.left(90)
        t.forward(rogi*i)
        t.down()
    t.right(90)
    t.up()
    t.forward(50)
    t.left(90)
    t.backward(dlugosc/2)
    t.down()

time.sleep(3)