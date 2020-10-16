from keyboard import *
while True:
    if is_pressed('a'):
        break

    # Input:
    # print("Количество лучей:")
    # n = round(int(input()) / 2)
    # print("Высота объекта:")
    # h = int(input())
    # print("Расстояние от объекта до линзы:")
    # l = int(input())
    # print("Расстояние от линзы до фотоаппарата:")
    # d = int(input())
    # print("Фокусное расстояние линзы:")
    # f1 = int(input())
    # print("Фокусное расстояние объектива:")
    # f2 = int(input())
    # print("Радиус линзы:")
    # r1 = int(input())
    # print("Радиус объектива:")
    # r2 = int(input())
    # print("Диаметр отверстия:")
    # D = int(input())

    if is_pressed('z') or is_pressed('x'):
        if is_pressed('z'):
            l = l - 20
        if is_pressed('x'):
            l = l + 20
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

        # Diafragm
        diaft = Line(Point(l + d, 350 - r1), Point(l + d, 350 - round(D / 2)))
        diaft.draw(w)
        diafb = Line(Point(l + d, 350 + round(D / 2)), Point(l + d, 350 + r1))
        diafb.draw(w)