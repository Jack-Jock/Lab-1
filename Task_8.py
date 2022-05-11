"""
Відомо, що X кг цукерок коштують A гривень. Визначити, скільки коштує 1 кг і Y кг цих же
цукерок
Скорий Євген 141
"""

def candy():
    print("Введіть число, яке не дорівнюе 0")
    x = float(input("Введіть X кг = "))
    a = float(input("Введіть A грн = "))
    y = float(input("Введіть Y кг = "))
    kg = float((1 * a) / x)
    cost = float((y * a) / x)
    return "d(Вартість за 1кг = " + str(kg) + "\nВартість за y кг = " + str(cost)

print(candy())