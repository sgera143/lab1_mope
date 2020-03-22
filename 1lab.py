import math
import random

while True:
    try:
        a_0 = int(input("Введіть значення a_0: "))
        a_1 = int(input("Введіть значення a_1: "))
        a_2 = int(input("Введіть значення a_2: "))
        a_3 = int(input("Введіть значення a_3: "))
        n = int(input("Введіть діапазон чисел: "))
        break
    except (NameError, ValueError):
        print("Виникла помилка, спробуйте ще раз")

y = [0] * 8

x_1 = [0] * 8
x_2 = [0] * 8
x_3 = [0] * 8

for i in range(8):
    x_1[i] = round(random.random() * 20, 2)
    x_2[i] = round(random.random() * 20, 2)
    x_3[i] = round(random.random() * 20, 2)
    y[i] = round(a_0 + a_1 * x_1[i] + a_2 * x_2[i] + a_3 * x_3[i], 2)

x_01 = round((max(x_1) + min(x_1)) / 2, 2)
x_02 = round((max(x_2) + min(x_2)) / 2, 2)
x_03 = round((max(x_3) + min(x_3)) / 2, 2)

dx_1 = round(x_01 - min(x_1), 2)
dx_2 = round(x_02 - min(x_2), 2)
dx_3 = round(x_03 - min(x_3), 2)

Xn_1 = [round((x_1[i] - x_01) / dx_1, 2) for i in range(8)]
Xn_2 = [round((x_2[i] - x_02) / dx_2, 2) for i in range(8)]
Xn_3 = [round((x_3[i] - x_03) / dx_3, 2) for i in range(8)]

Yet = a_0 + a_1 * x_01 + a_2 * x_02 + a_3 * x_03
print()

for i in range(8):
    print('{:<5} {:<5} {:<5} {:<5} {:<5} {:<8} {:<8} {:<8}'.format(i + 1, x_1[i], x_2[i], x_3[i], y[i], round(Xn_1[i], 2), round(Xn_2[i], 2), round(Xn_3[i], 2)))

print()
print('{:<5} {:<5} {:<5} {:<5}'.format("x0", x_01, x_02, x_03))
print('{:<5} {:<5} {:<5} {:<5}'.format("dx", dx_1, dx_2, dx_3))
print("\na_0 = %s\na_1 = %s\na_2 = %s\na_3 = %s"%(a_0, a_1, a_2, a_3))
print("\nYet = ", Yet)
print("min(f) = " + str(min(y)))

print("\nTочка плану, що задовольняє заданому критерію оптимальності:")
for i in range(8):
    if y[i] == min(y):
        print('{:<5} {:<5} {:<5} {:<5} {:<5} {:<8} {:<8} {:<8}'.format(i + 1, x_1[i], x_2[i], x_3[i], y[i], round(Xn_1[i], 4), round(Xn_2[i], 4), round(Xn_3[i], 4)))

Yser = round(sum(y) / 8, 2)
Y2 = [0] * 8

for i in range(8):
    Y2[i] = math.pow(y[i] - Yser, 2)

print("\nmax(Y-Yser)^2 = " + str(round(max(Y2), 2)))
print()