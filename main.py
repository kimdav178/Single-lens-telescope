def clos(w):
    w.close()

def bbbot(x):
    x = True

from graphics import *
from keyboard import *

# Variables
n = int(input())
# y1 = int(input())
# h = int(input())
ttop = False
bbot = False
mai = True

# Main objects
w = GraphWin("Telescope", 1368, 720)
w.setBackground("white")
# Main optical axis
moa = Line(Point(0, 350), Point(1368, 350))
moa.draw(w)
# Object arrow
arrow = Line(Point(10, 330), Point(10, 270))
arrow.setOutline("Blue")
arrow.draw(w)
# Bottom of the object is green
bottom = Line(Point(10, 330), Point(10, 350))
bottom.setOutline("Green")
bottom.draw(w)
# Top of the object is red
top = Line(Point(10, 250), Point(10, 271))
top.setOutline("Red")
top.draw(w)
# Focusing lens
lens = Line(Point(1000, 200), Point(1000, 500))
lens.draw(w)
# Camera's objective
obj = Line(Point(1200, 200), Point(1200, 500))
obj.draw(w)
# Camera's matrix
mat = Line(Point(1300, 200), Point(1300, 500))
mat.draw(w)

# Keyboard
#add_hotkey('esc', lambda: clos(w))
#add_hotkey('t', lambda: bbbot(ttop))
#add_hotkey('b', lambda: bbbot(bbot))
# on_press_key('t', callback=ttop, suppress=True)
# on_press_key('b', callback=bbot, suppress=True)
# on_press_key('q', callback=mai, suppress=False)

# Graphics
while mai:
    if is_pressed('t'):
        for j in range(-n, n):
            # y2[j] = j*150/n
            y2 = round(350 + j * 150 / n)
            ray = Line(Point(10, 250), Point(1000, y2))
            ray.setOutline("red")
            ray.draw(w)
            tg = (250 - y2) / 990
            y3 = 350 - 300 * tg - round((350 - y2 - 300 * tg) * 0, 6)  # F1 = 300, 0,6 = F1/(F1+d)
            ray2 = Line(Point(1000, y2), Point(1200, y3))
            ray2.setOutline("red")
            ray2.draw(w)
            tg2 = (y2 - y3) / 100
            y4 = round(350 + 100 * tg2)
            ray3 = Line(Point(1200, y3), Point(1300, y4))
            ray3.setOutline("red")
            ray3.draw(w)
    if is_pressed('b'):
        for j in range(-n, n):
            # y2[j] = j*150/n
            y2 = round(350 + j * 150 / n)
            ray = Line(Point(10, 350), Point(1000, y2))
            ray.setOutline("green")
            ray.draw(w)
            tg = (350 - y2) / 990
            y3 = 350 - 300 * tg - round((350 - y2 - 300 * tg) * 0, 6)  # F1 = 300, 0,6 = F1/(F1+d)
            ray2 = Line(Point(1000, y2), Point(1200, y3))
            ray2.setOutline("green")
            ray2.draw(w)
            tg2 = (y2 - y3) / 100
            y4 = round(350 + 100 * tg2)
            ray3 = Line(Point(1200, y3), Point(1300, y4))
            ray3.setOutline("green")
            ray3.draw(w)
    if is_pressed('Esc'):
        mai = False
        w.close()
    w.getMouse()
    w.close()