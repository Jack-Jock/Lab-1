"""
3. Дано два ненульових числа. Знайти суму, різницю, добуток і частку їх квадратів.
    Скорий Євген 141
"""

def square():
    print("Введіть не нульові числа")
    a = float(input("Введіть A = "))
    b = float(input("Введіть B = "))
    if a != 0:
        c = a * a
    else:
        print("Помилка : число дорівнює 0")
    if b != 0:
        d = b * b
    else:
        print("Помилка : число дорівнює 0")
    sum = float(c + d)
    dif = float(c - d)
    prod = float(c * d)
    fract = float(c / d)
    return "сума = " + str(sum) + "\nрізниця =" + str(dif) + "\nдобуток = " + str(prod) + "\nчастка = " + str(fract)

print(square())