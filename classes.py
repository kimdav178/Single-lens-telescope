from graphics import *
from keyboard import *


class Parameters:
    def __init__(self):
        self.n = 50
        self.h = 300
        self.l = 1000
        self.d = 200
        self.f1 = 400
        self.f2 = 100
        self.r1 = 300
        self.r2 = 300
        self.D = 100
        self.diaf = False
        self.ttop = False
        self.bbot = False


class Rays:
    def __init__(self, parameters):
        self.ray = []
        self.ray2 = []
        self.ray3 = []
        self.tg = []
        self.tg2 = []
        self.y2 = []
        self.y3 = []
        self.y4 = []
        self.diaphragmed = []
        for j in range(-parameters.n, parameters.n + 1):
            self.y2.append(round(350 + j * parameters.r1 / parameters.n))
            self.ray.append(Line(Point(10, 330 - parameters.h),
                                 Point(parameters.l + 10, self.y2[j + parameters.n])))
            self.ray[j + parameters.n].setOutline("red")
            self.tg.append((330 - parameters.h - self.y2[j + parameters.n]) / parameters.l)
            self.y3.append(350 - round(parameters.f1 * self.tg[j + parameters.n]) - round(
                (350 - self.y2[j + parameters.n] - parameters.f1 * self.tg[j + parameters.n]) * (
                        parameters.f1 - parameters.d) / parameters.f1))
            self.tg2.append((self.y3[j + parameters.n] - self.y2[j + parameters.n]) / parameters.d)
            if (350 - self.y3[j + parameters.n] + 10 * self.tg2[j + parameters.n] <= parameters.D / 2 and self.y3[
                j + parameters.n] <= 350) or (
                    self.y3[j + parameters.n] - 10 * self.tg2[j + parameters.n] - 350 <= parameters.D / 2 and self.y3[
                j + parameters.n] >= 350) or (not parameters.diaf):
                self.diaphragmed.append(False)
                self.ray2.append(Line(Point(parameters.l + 10, self.y2[j + parameters.n]),
                                      Point(parameters.l + parameters.d + 10, self.y3[j + parameters.n])))
                self.ray2[j + parameters.n].setOutline("red")
                self.y4.append(350 + round(parameters.f2 * self.tg2[j + parameters.n]))
                self.ray3.append(Line(Point(parameters.l + parameters.d + 10, self.y3[j + parameters.n]),
                                      Point(parameters.l + parameters.d + parameters.f2 + 10,
                                            self.y4[j + parameters.n])))
                self.ray3[j + parameters.n].setOutline("red")
            else:
                self.diaphragmed.append(True)
                self.ray2.append(Line(Point(parameters.l + 10, self.y2[j + parameters.n]),
                                      Point(parameters.l + parameters.d,
                                            self.y3[j + parameters.n] - 10 * self.tg2[j + parameters.n])))
                self.ray2[j + parameters.n].setOutline("red")

        for j in range(-parameters.n, parameters.n + 1):
            self.y2.append(round(350 + j * parameters.r1 / parameters.n))
            self.ray.append(Line(Point(10, 350),
                                 Point(parameters.l + 10, self.y2[j + 3 * parameters.n + 1])))
            self.ray[j + 3 * parameters.n + 1].setOutline("green")
            self.tg.append((350 - self.y2[j + 3 * parameters.n + 1]) / parameters.l)
            self.y3.append(350 - round(parameters.f1 * self.tg[j + 3 * parameters.n + 1]) - round(
                (350 - self.y2[j + 3 * parameters.n + 1] - parameters.f1 * self.tg[j + 3 * parameters.n + 1]) * (
                        parameters.f1 - parameters.d) / parameters.f1))
            self.tg2.append((self.y3[j + 3 * parameters.n + 1] - self.y2[
                j + 3 * parameters.n + 1]) / parameters.d)
            if (350 - self.y3[j + 3 * parameters.n + 1] + 10 * self.tg2[
                j + 3 * parameters.n + 1] <= parameters.D / 2 and self.y3[j + 3 * parameters.n + 1] <= 350) or (
                    self.y3[j + 3 * parameters.n + 1] - 10 * self.tg2[
                j + 3 * parameters.n + 1] - 350 <= parameters.D / 2 and self.y3[j + 3 * parameters.n + 1] >= 350) or (
                    not parameters.diaf):
                self.diaphragmed.append(False)
                self.ray2.append(Line(Point(parameters.l + 10, self.y2[j + 3 * parameters.n + 1]),
                                      Point(parameters.l + parameters.d + 10,
                                            self.y3[j + 3 * parameters.n + 1])))
                self.ray2[j + 3 * parameters.n + 1].setOutline("green")
                self.y4.append(350 + round(parameters.f2 * self.tg2[j + 3 * parameters.n + 1]))
                self.ray3.append(Line(
                    Point(parameters.l + parameters.d + 10, self.y3[j + 3 * parameters.n + 1]),
                    Point(parameters.l + parameters.d + parameters.f2 + 10, self.y4[j + 3 * parameters.n + 1])))
                self.ray3[j + 3 * parameters.n + 1].setOutline("green")
            else:
                self.diaphragmed.append(True)
                self.ray2.append(Line(Point(parameters.l + 10, self.y2[j + 3 * parameters.n + 1]),
                                      Point(parameters.l + parameters.d,
                                            self.y3[j + 3 * parameters.n + 1] - 10 * self.tg2[
                                                j + 3 * parameters.n + 1])))
                self.ray2[j + 3 * parameters.n + 1].setOutline("green")


class Arrow:
    def __init__(self, parameters):
        self.arrow = Line(Point(10, 340 - parameters.h), Point(10, 340))
        self.arrow.setOutline("Blue")
        self.top = Line(Point(10, 340 - parameters.h), Point(10, 330 - parameters.h))
        self.top.setOutline("Red")


class Lens:
    def __init__(self, parameters):
        self.lens = Line(Point(10 + parameters.l, 350 - parameters.r1), Point(10 + parameters.l, 350 + parameters.r1))
        self.lens1 = Line(Point(parameters.l, 360 - parameters.r1), Point(10 + parameters.l, 350 - parameters.r1))
        self.lens2 = Line(Point(parameters.l + 20, 360 - parameters.r1), Point(10 + parameters.l, 350 - parameters.r1))
        self.lens3 = Line(Point(parameters.l, 340 + parameters.r1), Point(10 + parameters.l, 350 + parameters.r1))
        self.lens4 = Line(Point(parameters.l + 20, 340 + parameters.r1), Point(10 + parameters.l, 350 + parameters.r1))


class Objective:
    def __init__(self, parameters):
        self.obj = Line(Point(parameters.l + parameters.d + 10, 350 - parameters.r2),
                        Point(parameters.l + parameters.d + 10, 350 + parameters.r2))
        self.obj1 = Line(Point(parameters.l + parameters.d, 360 - parameters.r2),
                         Point(parameters.l + parameters.d + 10, 350 - parameters.r2))
        self.obj2 = Line(Point(parameters.l + parameters.d + 20, 360 - parameters.r2),
                         Point(parameters.l + parameters.d + 10, 350 - parameters.r2))
        self.obj3 = Line(Point(parameters.l + parameters.d, 340 + parameters.r2),
                         Point(parameters.l + parameters.d + 10, 350 + parameters.r2))
        self.obj4 = Line(Point(parameters.l + parameters.d + 20, 340 + parameters.r2),
                         Point(parameters.l + parameters.d + 10, 350 + parameters.r2))


class Matrix:
    def __init__(self, parameters):
        self.mat = Line(Point(10 + parameters.l + parameters.d + parameters.f2, 350 - parameters.r2),
                        Point(10 + parameters.l + parameters.d + parameters.f2, 350 + parameters.r2))


class Diaphragm:
    def __init__(self, parameters):
        self.diaft = Line(Point(parameters.l + parameters.d, 350 - parameters.r1),
                          Point(parameters.l + parameters.d, 350 - round(parameters.D / 2)))
        self.diafb = Line(Point(parameters.l + parameters.d, 350 + round(parameters.D / 2)),
                          Point(parameters.l + parameters.d, 350 + parameters.r1))


w = GraphWin("Telescope", 1368, 720)
w.setBackground("white")
p = Parameters()
r = Rays(p)

a = Arrow(p)
bottom = Line(Point(10, 340), Point(10, 350))
bottom.setOutline("Green")
bottom.draw(w)
a.arrow.draw(w)
a.top.draw(w)

l = Lens(p)
l.lens.draw(w)
l.lens1.draw(w)
l.lens2.draw(w)
l.lens3.draw(w)
l.lens4.draw(w)

o = Objective(p)
o.obj.draw(w)
o.obj1.draw(w)
o.obj2.draw(w)
o.obj3.draw(w)
o.obj4.draw(w)

m = Matrix(p)
m.mat.draw(w)
d = Diaphragm(p)
moa = Line(Point(0, 350), Point(1368, 350))
moa.draw(w)

# Main loop
while True:
    Line(Point(0, 0), Point(1, 1)).draw(w)
    if is_pressed('Esc'):
        w.close()
        exit(0)

    if is_pressed('h'):
        a.arrow.undraw()
        a.arrow.setOutline("Red")
        a.arrow.draw(w)
        if p.ttop:
            p.ttop = False
            for j in range(-p.n, p.n + 1):
                if is_pressed('Esc'):
                    w.close()
                    exit(0)
                r.ray[j + p.n].undraw()
                r.ray2[j + p.n].undraw()
                r.ray3[j + p.n].undraw()
        if p.bbot:
            p.bbot = False
            for j in range(-p.n, p.n + 1):
                if is_pressed('Esc'):
                    w.close()
                    exit(0)
                r.ray[j + 3 * p.n + 1].undraw()
                r.ray2[j + 3 * p.n + 1].undraw()
                r.ray3[j + 3 * p.n + 1].undraw()
        while True:
            if is_pressed(KEY_UP) and p.h < 339:
                a.arrow.undraw()
                a.top.undraw()
                p.h = p.h + 1
                a.arrow.draw(w)
                a.top.draw(w)
            if is_pressed(KEY_DOWN) and p.h > 1:
                a.arrow.undraw()
                a.top.undraw()
                p.h = p.h - 1
                a.arrow.draw(w)
                a.top.draw(w)
            if is_pressed('Esc'):
                a.arrow.undraw()
                a.arrow.setOutline("Blue")
                a.arrow.draw(w)
                break

    if is_pressed('shift + d'):
        if p.diaf:
            p.diaf = False
            d.diaft.undraw()
            d.diafb.undraw()
            if p.ttop:
                for j in range(-p.n, p.n + 1):
                    if is_pressed('Esc'):
                        w.close()
                        exit(0)
                    r.ray2[j + p.n].undraw()
                    r.ray3[j + p.n].undraw()
                    r.ray2[j + p.n].draw(w)
                    r.ray3[j + p.n].draw(w)
            if p.bbot:
                for j in range(-p.n, p.n + 1):
                    if is_pressed('Esc'):
                        w.close()
                        exit(0)
                    r.ray2[j + 3 * p.n + 1].undraw()
                    r.ray3[j + 3 * p.n + 1].undraw()
                    r.ray2[j + 3 * p.n + 1].draw(w)
                    r.ray3[j + 3 * p.n + 1].draw(w)
        else:
            p.diaf = True
            d.diaft.draw(w)
            d.diafb.draw(w)
            if p.ttop:
                for j in range(-p.n, p.n + 1):
                    if is_pressed('Esc'):
                        w.close()
                        exit(0)
                    r.ray2[j + p.n].undraw()
                    r.ray3[j + p.n].undraw()
                    if r.diaphragmed[j + p.n]:
                        r.ray2[j + p.n].draw(w)
                        r.ray3[j + p.n].draw(w)
                    else:
                        r.ray2[j + p.n].draw(w)
            if p.bbot:
                for j in range(-p.n, p.n + 1):
                    if is_pressed('Esc'):
                        w.close()
                        exit(0)
                    r.ray2[j + 3 * p.n + 1].undraw()
                    r.ray3[j + 3 * p.n + 1].undraw()
                    if r.diaphragmed[j + 3 * p.n + 1]:
                        r.ray2[j + 3 * p.n + 1].draw(w)
                        r.ray3[j + 3 * p.n + 1].draw(w)
                    else:
                        r.ray2[j + 3 * p.n + 1].draw(w)

    if is_pressed('l'):
        if p.ttop:
            p.ttop = False
            for j in range(-p.n, p.n + 1):
                if is_pressed('Esc'):
                    w.close()
                    exit(0)
                r.ray[j + p.n].undraw()
                r.ray2[j + p.n].undraw()
                r.ray3[j + p.n].undraw()
        if p.bbot:
            p.bbot = False
            for j in range(-p.n, p.n + 1):
                if is_pressed('Esc'):
                    w.close()
                    exit(0)
                r.ray[j + 3 * p.n + 1].undraw()
                r.ray2[j + 3 * p.n + 1].undraw()
                r.ray3[j + 3 * p.n + 1].undraw()
        while True:
            if is_pressed('Esc'):
                w.close()
                exit(0)
            if is_pressed('left') or is_pressed('right'):
                if is_pressed('left') and p.l > 0:
                    p.l = p.l - 1
                if is_pressed('right') and p.l + p.d + p.f2 < 1350:
                    p.l = p.l + 1
                l.lens.undraw()
                l.lens1.undraw()
                l.lens2.undraw()
                l.lens3.undraw()
                l.lens4.undraw()
                o.obj.undraw()
                o.obj1.undraw()
                o.obj2.undraw()
                o.obj3.undraw()
                o.obj4.undraw()
                m.mat.undraw()
                if p.diaf:
                    d.diafb.undraw()
                    d.diaft.undraw()
                l.lens.draw(w)
                l.lens1.draw(w)
                l.lens2.draw(w)
                l.lens3.draw(w)
                l.lens4.draw(w)
                o.obj.draw(w)
                o.obj1.draw(w)
                o.obj2.draw(w)
                o.obj3.draw(w)
                o.obj4.draw(w)
                m.mat.draw(w)

                if p.diaf:
                    d.diaft.draw(w)
                    d.diafb.draw(w)
            if is_pressed('l'):
                break

    if is_pressed('t'):
        if not p.ttop:
            p.ttop = True
            for j in range(-p.n, p.n + 1):
                if is_pressed('Esc'):
                    w.close()
                    exit(0)
                r.ray[j + p.n].draw(w)
                if r.diaphragmed[j + p.n]:
                    r.ray2[j + p.n].draw(w)
                    r.ray3[j + p.n].draw(w)
                else:
                    r.ray2[j + p.n].draw(w)
        else:
            p.ttop = False
            for j in range(-p.n, p.n + 1):
                if is_pressed('Esc'):
                    w.close()
                    exit(0)
                r.ray[j + p.n].undraw()
                r.ray2[j + p.n].undraw()
                r.ray3[j + p.n].undraw()

    if is_pressed('b'):
        if not p.bbot:
            p.bbot = True
            for j in range(-p.n, p.n + 1):
                if is_pressed('Esc'):
                    w.close()
                    exit(0)
                r.ray[j + 3 * p.n + 1].draw(w)
                if r.diaphragmed[j + 3 * p.n + 1]:
                    r.ray2[j + 3 * p.n + 1].draw(w)
                    r.ray3[j + 3 * p.n + 1].draw(w)
                else:
                    r.ray2[j + 3 * p.n + 1].draw(w)
        else:
            p.bbot = False
            for j in range(-p.n, p.n + 1):
                if is_pressed('Esc'):
                    w.close()
                    exit(0)
                r.ray[j + 3 * p.n + 1].undraw()
                r.ray2[j + 3 * p.n + 1].undraw()
                r.ray3[j + 3 * p.n + 1].undraw()
