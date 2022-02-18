from graphics import *
from keyboard import *

# Variables
ttop = False
bbot = False
diaf = False

n = 10                  # Число лучей
h = 20                  # Высота объекта
l = (h + 20) * 30       # Расстояние от объекта до линзы
d = (h + 20) * 3 - 10   # Расстояние от линзы до фотоаппарата
f1 = (h + 20) * 3       # Фокусное расстояние линзы
f2 = round(h/2) + 10    # Фокусное расстояние фотоаппарата
r1 = round(h/2) + 10    # Радиус линзы
r2 = round(h/2) + 10    # Радиус объектива
D = round(h/10)         # Диаметр диафарагмы

"""
n = 50
h = 10
l = 900
d = 170
f1 = 300
f2 = 3.93
r1 = 30
r2 = 2
D = 10
"""

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
w = GraphWin("Telescope", 1366, 768, autoflush=True)
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
diaft = Line(Point(l + d, 0), Point(l + d, 350 - round(D / 2)))
diafb = Line(Point(l + d, 350 + round(D / 2)), Point(l + d, 768))

# No lens case
ray0 = Line(Point(10, 350), Point(10 + l + d + f2, 350))
ray0.setOutline("Green")
ray1 = Line(Point(10, 350 - h - 20), Point(10 + l + d + f2, 330 - h + round((l + d + f2) * (h + 20) / (l + d))))
ray1.setOutline("Red")
imag = Line(Point(10 + l + d + f2, 350), Point(10 + l + d + f2, 330 - h + round((l + d + f2) * (h + 20) / (l + d))))
imag.setOutline("Blue")
imag.setWidth(3)

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
            if is_pressed('Enter'):
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
            diaft = Line(Point(l + d, 0), Point(l + d, 350 - round(D / 2)))
            diaft.draw(w)
            diafb = Line(Point(l + d, 350 + round(D / 2)), Point(l + d, 768))
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
        if diaf:
            diaft.undraw()
            diaft.setOutline("Red")
            diaft.draw(w)
            diafb.undraw()
            diafb.setOutline("Red")
            diafb.draw(w)
        obj.undraw()
        obj.setOutline("Red")
        obj.draw(w)
        obj1.undraw()
        obj1.setOutline("Red")
        obj1.draw(w)
        obj2.undraw()
        obj2.setOutline("Red")
        obj2.draw(w)
        obj3.undraw()
        obj3.setOutline("Red")
        obj3.draw(w)
        obj4.undraw()
        obj4.setOutline("Red")
        obj4.draw(w)
        lens.undraw()
        lens.setOutline("Red")
        lens.draw(w)
        lens1.undraw()
        lens1.setOutline("Red")
        lens1.draw(w)
        lens2.undraw()
        lens2.setOutline("Red")
        lens2.draw(w)
        lens3.undraw()
        lens3.setOutline("Red")
        lens3.draw(w)
        lens4.undraw()
        lens4.setOutline("Red")
        lens4.draw(w)
        mat.undraw()
        mat.setOutline("Red")
        mat.draw(w)

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
            if is_pressed('left') or is_pressed('right'):
                if is_pressed('left') and l > 0:
                    l = l - 1
                if is_pressed('right') and l + d + f2 < 1350:
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
                if diaf:
                    diafb.undraw()
                    diaft.undraw()

                # Focusing lens
                lens = Line(Point(10 + l, 350 - r1), Point(10 + l, 350 + r1))
                lens.setOutline("Red")
                lens.draw(w)
                lens1 = Line(Point(l, 360 - r1), Point(10 + l, 350 - r1))
                lens1.setOutline("Red")
                lens1.draw(w)
                lens2 = Line(Point(l + 20, 360 - r1), Point(10 + l, 350 - r1))
                lens2.setOutline("Red")
                lens2.draw(w)
                lens3 = Line(Point(l, 340 + r1), Point(10 + l, 350 + r1))
                lens3.setOutline("Red")
                lens3.draw(w)
                lens4 = Line(Point(l + 20, 340 + r1), Point(10 + l, 350 + r1))
                lens4.setOutline("Red")
                lens4.draw(w)

                # Camera's objective
                obj = Line(Point(l + d + 10, 350 - r2), Point(l + d + 10, 350 + r2))
                obj.setOutline("Red")
                obj.draw(w)
                obj1 = Line(Point(l + d, 360 - r2), Point(l + d + 10, 350 - r2))
                obj1.setOutline("Red")
                obj1.draw(w)
                obj2 = Line(Point(l + d + 20, 360 - r2), Point(l + d + 10, 350 - r2))
                obj2.setOutline("Red")
                obj2.draw(w)
                obj3 = Line(Point(l + d, 340 + r2), Point(l + d + 10, 350 + r2))
                obj3.setOutline("Red")
                obj3.draw(w)
                obj4 = Line(Point(l + d + 20, 340 + r2), Point(l + d + 10, 350 + r2))
                obj4.setOutline("Red")
                obj4.draw(w)

                # Camera's matrix
                mat = Line(Point(10 + l + d + f2, 350 - r2), Point(10 + l + d + f2, 350 + r2))
                mat.setOutline("Red")
                mat.draw(w)

                # Diaphragm
                if diaf:
                    diaft = Line(Point(l + d, 0), Point(l + d, 350 - round(D / 2)))
                    diaft.setOutline("Red")
                    diaft.draw(w)
                    diafb = Line(Point(l + d, 350 + round(D / 2)), Point(l + d, 768))
                    diafb.setOutline("Red")
                    diafb.draw(w)
            if is_pressed('Enter'):
                if diaf:
                    diaft.undraw()
                    diaft.setOutline("Black")
                    diaft.draw(w)
                    diafb.undraw()
                    diafb.setOutline("Black")
                    diafb.draw(w)
                obj.undraw()
                obj.setOutline("Black")
                obj.draw(w)
                obj1.undraw()
                obj1.setOutline("Black")
                obj1.draw(w)
                obj2.undraw()
                obj2.setOutline("Black")
                obj2.draw(w)
                obj3.undraw()
                obj3.setOutline("Black")
                obj3.draw(w)
                obj4.undraw()
                obj4.setOutline("Black")
                obj4.draw(w)
                lens.undraw()
                lens.setOutline("Black")
                lens.draw(w)
                lens1.undraw()
                lens1.setOutline("Black")
                lens1.draw(w)
                lens2.undraw()
                lens2.setOutline("Black")
                lens2.draw(w)
                lens3.undraw()
                lens3.setOutline("Black")
                lens3.draw(w)
                lens4.undraw()
                lens4.setOutline("Black")
                lens4.draw(w)
                mat.undraw()
                mat.setOutline("Black")
                mat.draw(w)
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

    if is_pressed('o'):
        lens.undraw()
        lens1.undraw()
        lens2.undraw()
        lens3.undraw()
        lens4.undraw()
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
        ray0 = Line(Point(10, 350), Point(10 + l + d + f2, 350))
        ray0.setOutline("Green")
        ray0.draw(w)
        ray1 = Line(Point(10, 350 - h - 20),
                    Point(10 + l + d + f2, 330 - h + round((l + d + f2) * (h + 20) / (l + d))))
        ray1.setOutline("Red")
        ray1.draw(w)
        imag = Line(Point(10 + l + d + f2, 350),
                    Point(10 + l + d + f2, 330 - h + round((l + d + f2) * (h + 20) / (l + d))))
        imag.setOutline("Blue")
        imag.setWidth(3)
        imag.draw(w)
        while True:
            if is_pressed('Esc'):
                w.close()
                exit(0)
            if is_pressed('shift + d'):
                if diaf:
                    diaf = False
                    diaft.undraw()
                    diafb.undraw()
                else:
                    diaf = True
                    diaft = Line(Point(l + d, 0), Point(l + d, 350 - round(D / 2)))
                    diaft.draw(w)
                    diafb = Line(Point(l + d, 350 + round(D / 2)), Point(l + d, 768))
                    diafb.draw(w)
            if is_pressed('Enter'):
                ray0.undraw()
                ray1.undraw()
                imag.undraw()
                lens.draw(w)
                lens1.draw(w)
                lens2.draw(w)
                lens3.draw(w)
                lens4.draw(w)
                break
