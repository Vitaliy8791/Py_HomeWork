a = ""
while a == "" or a == "0":
    a = input("Введите число а (не равное 0): ")
a = float(a)
b = float(input("Введите число b: "))
c = float(input("Введите число c: "))

# Формируем выражение если b < 0 и a != 0
if b < 0 < c and a != 0:
    print("{}(X**2){}x+{}=0".format(a, b, c))  # Формируем выражение если c > 0
elif b < 0 and c < 0 and a != 0:
    print("{}(X**2){}x{}=0".format(a, b, c))  # Формируем выражение если c < 0
# Формируем выражение если b < 0 и a == 0
elif b < 0 < c and a == 0:
    print("{}x+{}=0".format(b, c))  # Формируем выражение если b < 0 и c > 0
elif b < 0 and c < 0 and a == 0:
    print("{}x{}=0".format(b, c))   # Формируем выражение если b < 0 и c < 0
# Формируем выражение если b < 0 и c == 0 и a != 0
elif b < 0 and a != 0 and c == 0:
    print("{}(X**2){}x=0".format(a, b))
# Формируем выражение если b > 0 и c == 0 и a == 0
if a == 0 and c == 0:
    print(b, "x=0")

#  Формируем выражение если b > 0 и a != 0
if b > 0 and c > 0 and a != 0:
    print("{}(X**2)+{}x+{}=0".format(a, b, c))  # Формируем выражение если c > 0
elif b > 0 > c and a != 0:
    print("{}(X**2)+{}x{}=0".format(a, b, c))  # Формируем выражение если c < 0
# Формируем выражение если b > 0 и a == 0
elif b > 0 < c and a == 0:
    print("{}x+{}=0".format(b, c))  # Формируем выражение если b > 0 и c > 0
elif b > 0 > c and a == 0:
    print("{}x{}=0".format(b, c))   # Формируем выражение если b > 0 и c < 0
# Формируем выражение если b > 0 и c == 0 и a != 0
elif b > 0 and a != 0 and c == 0:
    print("{}(X**2)+{}x=0".format(a, b))
#  Формируем выражение если b == 0 и c == 0
elif b == 0 and c == 0:
    print(a, "(x**2)=0")

#  Считаем дискриминант
diskr = b**2 - 4*a*c
print("Дискриминант равен ", diskr)
#  Рассчитываем корни уравнения
x1 = (-b + diskr**(1/2))/(2*a)
x2 = (-b - diskr**(1/2))/(2*a)

if diskr < 0:
    print("Уравнение имеет комплексные корни:\n x1 = ", x1, "\n x2 = ", x2)
elif diskr == 0:
    print("Уравнение имеет один корень: \n", "x = ", x1)
else:
    print("Корни уравнения:\n x1 = ", x1, "\n x2 = ", x2)

