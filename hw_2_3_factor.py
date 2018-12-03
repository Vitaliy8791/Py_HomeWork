num = -1
rez = 1
ostat = 1
while num < 0 or ostat != 0:
    num = float(input("Введите значение факториала n! = "))
    ostat = num % 1  # остаток от деления
    if ostat != 0:  # проверка целое число или нет
        print("Значение должно быть целым числом!")
    if num < 0:  # проверяем на ввод отрицательного числа
        print("Значение должно быть больше или равно 0!")
num = int(num)
for i in range(1, num+1):  # Считаем факториал
    rez = rez * i
print("Факториал ", num, "! = ", rez)