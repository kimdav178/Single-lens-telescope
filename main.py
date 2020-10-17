from graphics import *
from keyboard import *

# Variables
ttop = False
bbot = False
diaf = False
n = 50
h = 300
l = 1000
d = 200
f1 = 400
f2 = 100
r1 = 300
r2 = 300
D = 100
ray = []
ray2 = []
ray3 = []
tg = []
tg2 = []
y2 = []
y3 = []
y4 = []
for i in range(4 * n + 2):
    ray.append(Line(Point(0, 0), Point(1, 1)))
    ray2.append(Line(Point(0, 0), Point(1, 1)))
    ray3.append(Line(Point(0, 0), Point(1, 1)))
    tg.append(1.0)
    tg2.append(1.0)
    y2.append(1.0)
    y3.append(1.0)
    y4.append(1.0)

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
obj2 = Line(Point(l + d + 20, 360 - r2), Point(l + d + 10, 350 - r2))
obj2.draw(w)
obj3 = Line(Point(l + d, 340 + r2), Point(l + d + 10, 350 + r2))
obj3.draw(w)
obj4 = Line(Point(l + d + 20, 340 + r2), Point(l + d + 10, 350 + r2))
obj4.draw(w)

# Camera's matrix
mat = Line(Point(10 + l + d + f2, 350 - r2), Point(10 + l + d + f2, 350 + r2))
mat.draw(w)

# Diaphragm
diaft = Line(Point(l + d, 350 - r1), Point(l + d, 350 - round(D / 2)))
diafb = Line(Point(l + d, 350 + round(D / 2)), Point(l + d, 350 + r1))

# Main loop
while True:
    Line(Point(0, 0), Point(1, 1)).draw(w)
    if is_pressed('Esc'):
        w.close()
        exit(0)

    if is_pressed('h'):
        arrow.undraw()
        arrow.setOutline("Red")
        arrow.draw(w)
        if ttop:
            ttop = False
            for j in range(-n, n + 1):
                if is_pressed('Esc'):
                    w.close()
                    exit(0)
                ray[j + n].undraw()
                ray2[j + n].undraw()
                ray3[j + n].undraw()
        if bbot:
            bbot = False
            for j in range(-n, n + 1):
                if is_pressed('Esc'):
                    w.close()
                    exit(0)
                ray[j + 3 * n + 1].undraw()
                ray2[j + 3 * n + 1].undraw()
                ray3[j + 3 * n + 1].undraw()
        while True:
            if is_pressed('Esc'):
                w.close()
                exit(0)
            if is_pressed(KEY_UP) and h < 339:
                arrow.undraw()
                top.undraw()
                h = h + 1
                top = Line(Point(10, 340 - h), Point(10, 330 - h))
                arrow = Line(Point(10, 340 - h), Point(10, 340))
                arrow.setOutline("Red")
                top.setOutline("Red")
                arrow.draw(w)
                top.draw(w)
            if is_pressed(KEY_DOWN) and h > 1:
                arrow.undraw()
                top.undraw()
                h = h - 1
                top = Line(Point(10, 340 - h), Point(10, 330 - h))
                arrow = Line(Point(10, 340 - h), Point(10, 340))
                arrow.setOutline("Red")
                top.setOutline("Red")
                arrow.draw(w)
                top.draw(w)
            if is_pressed('h'):
                arrow.undraw()
                arrow.setOutline("Blue")
                arrow.draw(w)
                break

    if is_pressed('shift + d'):
        if diaf:
            diaf = False
            diaft.undraw()
            diafb.undraw()
            if ttop:
                for j in range(-n, n + 1):
                    if is_pressed('Esc'):
                        w.close()
                        exit(0)
                    ray2[j + n].undraw()
                    ray3[j + n].undraw()
                    ray2[j + n] = Line(Point(l + 10, y2[j + n]), Point(l + d + 10, y3[j + n]))
                    ray2[j + n].setOutline("red")
                    ray2[j + n].draw(w)
                    y4[j + n] = 350 + round(f2 * tg2[j + n])
                    ray3[j + n] = Line(Point(l + d + 10, y3[j + n]), Point(l + d + f2 + 10, y4[j + n]))
                    ray3[j + n].setOutline("red")
                    ray3[j + n].draw(w)
            if bbot:
                for j in range(-n, n + 1):
                    if is_pressed('Esc'):
                        w.close()
                        exit(0)
                    ray2[j + 3 * n + 1].undraw()
                    ray3[j + 3 * n + 1].undraw()
                    ray2[j + 3 * n + 1] = Line(Point(l + 10, y2[j + 3 * n + 1]), Point(l + d + 10, y3[j + 3 * n + 1]))
                    ray2[j + 3 * n + 1].setOutline("green")
                    ray2[j + 3 * n + 1].draw(w)
                    y4[j + 3 * n + 1] = 350 + round(f2 * tg2[j + 3 * n + 1])
                    ray3[j + 3 * n + 1] = Line(Point(l + d + 10, y3[j + 3 * n + 1]),
                                               Point(l + d + f2 + 10, y4[j + 3 * n + 1]))
                    ray3[j + 3 * n + 1].setOutline("green")
                    ray3[j + 3 * n + 1].draw(w)
        else:
            diaf = True
            diaft = Line(Point(l + d, 350 - r1), Point(l + d, 350 - round(D / 2)))
            diaft.draw(w)
            diafb = Line(Point(l + d, 350 + round(D / 2)), Point(l + d, 350 + r1))
            diafb.draw(w)
            if ttop:
                for j in range(-n, n + 1):
                    if is_pressed('Esc'):
                        w.close()
                        exit(0)
                    ray2[j + n].undraw()
                    ray3[j + n].undraw()
                    y2[j + n] = round(350 + j * r1 / n)
                    tg[j + n] = (330 - h - y2[j + n]) / l
                    y3[j + n] = 350 - round(f1 * tg[j + n]) - round((350 - y2[j + n] - f1 * tg[j + n]) * (f1 - d) / f1)
                    tg2[j + n] = (y3[j + n] - y2[j + n]) / d
                    if (350 - y3[j + n] + 10 * tg2[j + n] <= D / 2 and y3[j + n] <= 350) or (
                            y3[j + n] - 10 * tg2[j + n] - 350 <= D / 2 and y3[j + n] >= 350) or (not diaf):
                        ray2[j + n] = Line(Point(l + 10, y2[j + n]), Point(l + d + 10, y3[j + n]))
                        ray2[j + n].setOutline("red")
                        ray2[j + n].draw(w)
                        y4[j + n] = 350 + round(f2 * tg2[j + n])
                        ray3[j + n] = Line(Point(l + d + 10, y3[j + n]), Point(l + d + f2 + 10, y4[j + n]))
                        ray3[j + n].setOutline("red")
                        ray3[j + n].draw(w)
                    else:
                        ray2[j + n] = Line(Point(l + 10, y2[j + n]), Point(l + d, y3[j + n] - 10 * tg2[j + n]))
                        ray2[j + n].setOutline("red")
                        ray2[j + n].draw(w)
            if bbot:
                for j in range(-n, n + 1):
                    if is_pressed('Esc'):
                        w.close()
                        exit(0)
                    ray2[j + 3 * n + 1].undraw()
                    ray3[j + 3 * n + 1].undraw()
                    y2[j + 3 * n + 1] = round(350 + j * r1 / n)
                    tg[j + 3 * n + 1] = (350 - y2[j + 3 * n + 1]) / l
                    y3[j + 3 * n + 1] = 350 - round(f1 * tg[j + 3 * n + 1]) - round(
                        (350 - y2[j + 3 * n + 1] - f1 * tg[j + 3 * n + 1]) * (f1 - d) / f1)
                    tg2[j + 3 * n + 1] = (y3[j + 3 * n + 1] - y2[j + 3 * n + 1]) / d
                    if (350 - y3[j + 3 * n + 1] + 10 * tg2[j + 3 * n + 1] <= D / 2 and y3[j + 3 * n + 1] <= 350) or (
                            y3[j + 3 * n + 1] - 10 * tg2[j + 3 * n + 1] - 350 <= D / 2 and y3[
                        j + 3 * n + 1] >= 350) or (not diaf):
                        ray2[j + 3 * n + 1] = Line(Point(l + 10, y2[j + 3 * n + 1]),
                                                   Point(l + d + 10, y3[j + 3 * n + 1]))
                        ray2[j + 3 * n + 1].setOutline("green")
                        ray2[j + 3 * n + 1].draw(w)
                        y4[j + 3 * n + 1] = 350 + round(f2 * tg2[j + 3 * n + 1])
                        ray3[j + 3 * n + 1] = Line(Point(l + d + 10, y3[j + 3 * n + 1]),
                                                   Point(l + d + f2 + 10, y4[j + 3 * n + 1]))
                        ray3[j + 3 * n + 1].setOutline("green")
                        ray3[j + 3 * n + 1].draw(w)
                    else:
                        ray2[j + 3 * n + 1] = Line(Point(l + 10, y2[j + 3 * n + 1]),
                                                   Point(l + d, y3[j + 3 * n + 1] - 10 * tg2[j + 3 * n + 1]))
                        ray2[j + 3 * n + 1].setOutline("green")
                        ray2[j + 3 * n + 1].draw(w)

    if is_pressed('l'):
        if ttop:
            ttop = False
            for j in range(-n, n + 1):
                if is_pressed('Esc'):
                    w.close()
                    exit(0)
                ray[j + n].undraw()
                ray2[j + n].undraw()
                ray3[j + n].undraw()
        if bbot:
            bbot = False
            for j in range(-n, n + 1):
                if is_pressed('Esc'):
                    w.close()
                    exit(0)
                ray[j + 3 * n + 1].undraw()
                ray2[j + 3 * n + 1].undraw()
                ray3[j + 3 * n + 1].undraw()
        while True:
            if is_pressed('z') or is_pressed('x'):
                if is_pressed('z') and l > 0:
                    l = l - 1
                if is_pressed('x') and l + d + f2 < 1350:
                    l = l + 1
                lens.undraw()
                lens1.undraw()
                lens2.undraw()
                lens3.undraw()
                lens4.undraw()
                obj.undraw()
                obj1.undraw()
                obj2.undraw()
                obj3.undraw()
                obj4.undraw()
                mat.undraw()
                diafb.undraw()
                diaft.undraw()

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
                obj2 = Line(Point(l + d + 20, 360 - r2), Point(l + d + 10, 350 - r2))
                obj2.draw(w)
                obj3 = Line(Point(l + d, 340 + r2), Point(l + d + 10, 350 + r2))
                obj3.draw(w)
                obj4 = Line(Point(l + d + 20, 340 + r2), Point(l + d + 10, 350 + r2))
                obj4.draw(w)

                # Camera's matrix
                mat = Line(Point(10 + l + d + f2, 350 - r2), Point(10 + l + d + f2, 350 + r2))
                mat.draw(w)

                # Diaphragm
                diaft = Line(Point(l + d, 350 - r1), Point(l + d, 350 - round(D / 2)))
                diaft.draw(w)
                diafb = Line(Point(l + d, 350 + round(D / 2)), Point(l + d, 350 + r1))
                diafb.draw(w)
            if is_pressed('l'):
                break

    if is_pressed('t'):
        if not ttop:
            ttop = True
            for j in range(-n, n + 1):
                if is_pressed('Esc'):
                    w.close()
                    exit(0)
                y2[j + n] = round(350 + j * r1 / n)
                ray[j + n] = Line(Point(10, 330 - h), Point(l + 10, y2[j + n]))
                ray[j + n].setOutline("red")
                ray[j + n].draw(w)
                tg[j + n] = (330 - h - y2[j + n]) / l
                y3[j + n] = 350 - round(f1 * tg[j + n]) - round((350 - y2[j + n] - f1 * tg[j + n]) * (f1 - d) / f1)
                tg2[j + n] = (y3[j + n] - y2[j + n]) / d
                if (350 - y3[j + n] + 10 * tg2[j + n] <= D / 2 and y3[j + n] <= 350) or (
                        y3[j + n] - 10 * tg2[j + n] - 350 <= D / 2 and y3[j + n] >= 350) or (not diaf):
                    ray2[j + n] = Line(Point(l + 10, y2[j + n]), Point(l + d + 10, y3[j + n]))
                    ray2[j + n].setOutline("red")
                    ray2[j + n].draw(w)
                    y4[j + n] = 350 + round(f2 * tg2[j + n])
                    ray3[j + n] = Line(Point(l + d + 10, y3[j + n]), Point(l + d + f2 + 10, y4[j + n]))
                    ray3[j + n].setOutline("red")
                    ray3[j + n].draw(w)
                else:
                    ray2[j + n] = Line(Point(l + 10, y2[j + n]), Point(l + d, y3[j + n] - 10 * tg2[j + n]))
                    ray2[j + n].setOutline("red")
                    ray2[j + n].draw(w)
        else:
            ttop = False
            for j in range(-n, n + 1):
                if is_pressed('Esc'):
                    w.close()
                    exit(0)
                ray[j + n].undraw()
                ray2[j + n].undraw()
                ray3[j + n].undraw()

    if is_pressed('b'):
        if not bbot:
            bbot = True
            for j in range(-n, n + 1):
                if is_pressed('Esc'):
                    w.close()
                    exit(0)
                y2[j + 3 * n + 1] = round(350 + j * r1 / n)
                ray[j + 3 * n + 1] = Line(Point(10, 350), Point(l + 10, y2[j + 3 * n + 1]))
                ray[j + 3 * n + 1].setOutline("green")
                ray[j + 3 * n + 1].draw(w)
                tg[j + 3 * n + 1] = (350 - y2[j + 3 * n + 1]) / l
                y3[j + 3 * n + 1] = 350 - round(f1 * tg[j + 3 * n + 1]) - round(
                    (350 - y2[j + 3 * n + 1] - f1 * tg[j + 3 * n + 1]) * (f1 - d) / f1)
                tg2[j + 3 * n + 1] = (y3[j + 3 * n + 1] - y2[j + 3 * n + 1]) / d
                if (350 - y3[j + 3 * n + 1] + 10 * tg2[j + 3 * n + 1] <= D / 2 and y3[j + 3 * n + 1] <= 350) or (
                        y3[j + 3 * n + 1] - 10 * tg2[j + 3 * n + 1] - 350 <= D / 2 and y3[j + 3 * n + 1] >= 350) or (
                not diaf):
                    ray2[j + 3 * n + 1] = Line(Point(l + 10, y2[j + 3 * n + 1]), Point(l + d + 10, y3[j + 3 * n + 1]))
                    ray2[j + 3 * n + 1].setOutline("green")
                    ray2[j + 3 * n + 1].draw(w)
                    y4[j + 3 * n + 1] = 350 + round(f2 * tg2[j + 3 * n + 1])
                    ray3[j + 3 * n + 1] = Line(Point(l + d + 10, y3[j + 3 * n + 1]),
                                               Point(l + d + f2 + 10, y4[j + 3 * n + 1]))
                    ray3[j + 3 * n + 1].setOutline("green")
                    ray3[j + 3 * n + 1].draw(w)
                else:
                    ray2[j + 3 * n + 1] = Line(Point(l + 10, y2[j + 3 * n + 1]),
                                               Point(l + d, y3[j + 3 * n + 1] - 10 * tg2[j + 3 * n + 1]))
                    ray2[j + 3 * n + 1].setOutline("green")
                    ray2[j + 3 * n + 1].draw(w)
        else:
            bbot = False
            for j in range(-n, n + 1):
                if is_pressed('Esc'):
                    w.close()
                    exit(0)
                ray[j + 3 * n + 1].undraw()
                ray2[j + 3 * n + 1].undraw()
                ray3[j + 3 * n + 1].undraw()
