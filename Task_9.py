"""
9. Дано двозначне число. Знайти суму і добуток його цифр.
Скорий Євген 141
"""

def number():
    a = float(input("Введіть двозначне число = "))
    if a > 9 and a < 100:
        b = a//10
        c = a%10
    else:
        print("Помилка : число повинне бути двозначне")

    sum = int(b + c)
    prod = int(b * c)
    return "сума = " + str(sum) + "\nдобуток = " + str(prod)


print(number())