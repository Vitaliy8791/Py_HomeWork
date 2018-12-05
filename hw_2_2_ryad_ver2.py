num_begin = ""
num_finish = ""
rezult = 0
ostat = 1
while num_begin == "" or num_begin < 0:
    num_begin = ""
    num_begin = input("Введите целое число начала ряда натуральных чисел:  ")
    if num_begin == "":  # проверяем на пустой ввдод (Enter)
        continue
    num_begin = float(num_begin)
    if num_begin < 0:  # проверяем на ввод отрицательного числа
        print("Значение должно быть больше или равно 0!")
        continue
    ostat = num_begin % 1  # остаток от деления
while num_finish == "" or num_finish < num_begin:
    num_finish = ""
    num_finish = input("Введите целое число конца ряда натуральных чисел:  ")
    if num_finish == "":  # проверяем на пустой ввдод (Enter)
        continue
    num_finish = float(num_finish)
    if num_finish < num_begin:  # проверяем чтобы вводимое число было не меньше начала ряда
        print("Значение должно быть больше или равно числу начала ряда!")
        continue
    if int(num_begin) == int(num_finish):
       print("Натуральное число не попало в выбранный диаппазон")
if int(num_begin) != int(num_finish) or ostat == 0:
    print("Начало ряда - ", num_begin)
    print("Конец ряда - ", num_finish)
    if ostat != 0:  # округление к следующему ближайшему натуральному числу
        num_begin = int(num_begin) + 1
    num_finish = int(num_finish)
    num_begin = int(num_begin)
    for i in range(num_begin, num_finish + 1):  # считаем результат
        rezult = i + rezult
        i += 1
    print("Сумма натуральных чисел выбранного ряда = ", rezult)
