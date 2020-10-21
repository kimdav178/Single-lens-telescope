from keyboard import *
from graphics import *

n = 200
line = Line(Point(100, 100), Point(100, n))
# Window settings
w = GraphWin("Telescope", 1368, 720)
w.setBackground("white")
line.draw(w)

arr = []
for i in range(5):
    arr.append(Line(Point(i*100, i*50), Point(100 + i*100, 100+i*100)))

arr.draw(w)

while True:
    if is_pressed('Esc'):
        w.close()
        exit(0)
    if is_pressed('left'):
        line.move(10, 0)
        print(line.getCenter())

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