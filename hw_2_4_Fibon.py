num = 0
rez_n = 0
rez_0 = 1
while num <= 0 or ostat != 0:
    num = float(input("Введите номер Числа Фибоначчи n = "))
    ostat = num % 1  # остаток от деления
    if ostat != 0:  # проверка целое число или нет
        print("Значение должно быть целым числом!")
    if num <= 0:  # проверяем на ввод числа больше 0
        print("Значение должно быть больше 0!")
num = int(num)
for i in range(0, num+1):  # Считаем число ряда Фибоначи
    rez_n = rez_n + rez_0
    rez_0 = rez_n - rez_0
print("Номер Числа Фибоначчи n = ", num, " равен ", rez_0)