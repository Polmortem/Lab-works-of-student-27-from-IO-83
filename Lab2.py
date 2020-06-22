from random import *
from numpy import *

Rcr = 2.16
m = 5  # кількість дослідів
b = 3  # рядки

def show_check():…

def show_norm():…

# 4) Перевірка однорідності дисперсії за критерієм Романовського
while True:
    # Початкові параметри
    x1_min, x1_max = 10, 60
    x2_min, x2_max = -35, 10
    y_min, y_max = -70, 30
    x = [[-1, -1, +1],  # x1
         [-1, +1, -1]]  # x2
    y = [[randint(y_min, y_max) for _ in range(0, m)]
         for _ in range(0, b)]

    # 4) Перевірка однорідності дисперсії за критерієм Романовського
    # 4.1. Знайдемо середнє значення функції відгуку в рядку:
    y_ = [round(sum(y[i]) / len(y[i]), 2) for i in range(0, b)]

    # 4.2. Знайдемо дисперсії по рядках
    sig_y = []
    for i in range(0, b):
        s = 0  # sum
        for j in range(0, m):
            s += (y[i][j] - y_[i]) ** 2
        sig_y.append(round(s / m, 2))

    # 4.3. Обчислимо основне відхилення. 't' means θ (tetha)
    sig_t = round(sqrt((2 * (2 * m - 2)) / (m * (m - 4))), 2)

    # 4.4. Обчислимо Fuv
    Fuv = [round(sig_y[0] / sig_y[1], 2),  # Fuv_1
           round(sig_y[2] / sig_y[0], 2),  # Fuv_2
           round(sig_y[2] / sig_y[1], 2)]  # Fuv_3

    # 4.5 θuv. 'T' means θ (Tetha)
    Tuv = [round(((m - 2) / m) * Fuv[i], 2) for i in range(0, b)]

    # 4.6 Ruv
    Ruv = [round(abs(Tuv[i] - 1) / sig_t, 2) for i in range(b)]

    # 4.7 Перевірка
    R = [Ruv[i] < Rcr for i in range(b)]
    if R[0] and R[1] and R[2]:
        show_check()
        break
    else:
        print("Збільшуємо кількість дослідів.", "-" * 23, sep="\n")
        m += 1

# 5) Розрахунок нормованих коефіцієнтів рівняння регресії
mx = [round(sum(x[i]) / b, 2) for i in range(2)]
my = round(sum(y_) / b, 2)
a = [round((x[0][0] ** 2 + x[0][1] ** 2 + x[0][2] ** 2) / b, 2),
     round((x[0][0] * x[1][0] + x[0][1] * x[1][1] + x[0][2] * x[1][2]) / b, 2),
     round((x[1][0] ** 2 + x[1][1] ** 2 + x[1][2] ** 2) / b, 2)]
a11 = round((x[0][0] * y_[0] + x[0][1] * y_[1] + x[0][2] * y_[2]) / b, 2)
a22 = round((x[1][0] * y_[0] + x[1][1] * y_[1] + x[1][2] * y_[2]) / b, 2)

# Розв'яжемо систему лінійних рівнянь
matrix = array([[1,      mx[0], mx[1]],
                [mx[0],  a[0],  a[1]],
                [mx[1],  a[1],  a[2]]])
vector = array([my, a11, a22])
solve = linalg.solve(matrix, vector)

# 6) Натуралізація коефіціентів
dx1, dx2 = fabs(x1_max - x1_min) / 2, fabs(x2_max - x2_min) / 2
x10, x20 = (x1_max + x1_min) / 2, (x2_max + x2_min) / 2
a0 = round(solve[0] - solve[1] * x10 / dx1 - solve[2] * x20 / dx2, 2)
a1 = round(solve[1] / dx1, 2)
a2 = round(solve[2] / dx2, 2)

show_norm()
