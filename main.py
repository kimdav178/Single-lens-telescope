# def clos(w):
#    w.close()


# def bbbot(x):
#    x = True


from graphics import *
from keyboard import *

# Variables
ttop = True
bbot = True
mai = True
# y1 = int(input())
# h = int(input())

print("Количество лучей:")
n = round(int(input()) / 2)
print("Высота объекта:")
h = int(input())
print("Расстояние от объекта до линзы:")
l = int(input())
print("Расстояние от линзы до фотоаппарата:")
d = int(input())
print("Фокусное расстояние линзы:")
f1 = int(input())
print("Фокусное расстояние объектива:")
f2 = int(input())
print("Радиус линзы:")
r1 = int(input())
print("Радиус объектива:")
r2 = int(input())

# Window settings
w = GraphWin("Telescope", 1368, 720)
w.setBackground("white")

# Main optical axis
moa = Line(Point(0, 350), Point(1368, 350))
moa.draw(w)

# Object arrow
arrow = Line(Point(10, 340 - h), Point(10, 340))
arrow.setOutline("Blue")
arrow.draw(w)

# Bottom of the object is green
bottom = Line(Point(10, 340), Point(10, 350))
bottom.setOutline("Green")
bottom.draw(w)

# Top of the object is red
top = Line(Point(10, 340 - h), Point(10, 330 - h))
top.setOutline("Red")
top.draw(w)

# Focusing lens
lens = Line(Point(10 + l, 350 - r1), Point(10 + l, 350 + r1))
lens.draw(w)
lens1 = Line(Point(l, 360 - r1), Point(10 + l, 350 - r1))
lens1.draw(w)
lens2 = Line(Point(l + 20, 360 - r1), Point(10 + l, 350 - r1))
lens2.draw(w)
lens3 = Line(Point(l, 340 + r1), Point(10 + l, 350 + r1))
lens3.draw(w)
lens4 = Line(Point(l + 20, 340 + r1), Point(10 + l, 350 + r1))
lens4.draw(w)

# Camera's objective
obj = Line(Point(l + d + 10, 350 - r2), Point(l + d + 10, 350 + r2))
obj.draw(w)
obj1 = Line(Point(l + d, 360 - r2), Point(l + d + 10, 350 - r2))
obj1.draw(w)
obj2 = Line(Point(l + d + 10, 360 - r2), Point(1200, 350 - r2))
obj2.draw(w)
obj3 = Line(Point(l + d - 10, 340 + r2), Point(1200, 350 + r2))
obj3.draw(w)
obj4 = Line(Point(l + d + 20, 340 + r2), Point(l + d + 10, 350 + r2))
obj4.draw(w)

# Camera's matrix
mat = Line(Point(10 + l + d + f2, 350 - r2), Point(10 + l + d + f2, 350 + r2))
mat.draw(w)

# Keyboard
# add_hotkey('esc', lambda: clos(w))
# add_hotkey('<KeyPress-Up>', lambda: bbbot(ttop))
# add_hotkey('b', lambda: bbbot(bbot))
# on_press_key('<KeyPress-Up>', callback=ttop, suppress=True)
# on_press_key('b', callback=bbot, suppress=True)
# on_press_key('q', callback=mai, suppress=False)

# Graphics
while mai:
    if is_pressed('t'):
        ttop = True
    if is_pressed('b'):
        bbot = True
    if ttop:
        for j in range(-n, n):
            # y2[j] = j*150/n
            y2 = round(350 + j * r1 / n)
            ray = Line(Point(10, 330 - h), Point(l + 10, y2))
            ray.setOutline("red")
            ray.draw(w)
            tg = (330 - h - y2) / l
            y3 = 350 - f1 * tg - round((350 - y2 - f1 * tg) * f1/(f1+d))
            ray2 = Line(Point(l + 10, y2), Point(l + d + 10, y3))
            ray2.setOutline("red")
            ray2.draw(w)
            tg2 = (y3 - y2) / f2
            y4 = round(350 + f2 * tg2)
            ray3 = Line(Point(l + d + 10, y3), Point(l + d + f2 + 10, y4))
            ray3.setOutline("red")
            ray3.draw(w)
    if not bbot:
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
            tg2 = (y3 - y2) / 100
            y4 = round(350 + 100 * tg2)
            ray3 = Line(Point(1200, y3), Point(1300, y4))
            ray3.setOutline("green")
            ray3.draw(w)
    if is_pressed('q'):
        mai = False
        w.close()
    w.getMouse()
    w.close()
