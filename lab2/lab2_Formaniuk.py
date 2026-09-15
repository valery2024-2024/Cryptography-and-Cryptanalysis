# Форманюк Валерій Володимирович
# Група: КН-4/1
# Лабораторна робота №2
# Тема: Модульна арифметика в криптографії

import math
# Частина 2. Обов'язкові функції

def are_coprime(a: int, b: int) -> bool:
    return math.gcd(a, b) == 1

def mod_pow(base: int, exponent: int, modulus: int) -> int:
    return pow(base, exponent, modulus)

def mod_inverse(a: int, modulus: int) -> int | None:
    for x in range(1, modulus):
        if (a * x) % modulus == 1:
            return x

    return None

# Частина 1. Остача, НСД і взаємна простота

print("Частина 1. Остача, НСД і взаємна простота")

print("17 % 5 =", 17 % 5)
print("-3 % 26 =", -3 % 26)
print("1001 % 26 =", 1001 % 26)

print("\nНСД для заданих пар:")

print("gcd(18, 24) =", math.gcd(18, 24))
print("gcd(15, 26) =", math.gcd(15, 26))
print("gcd(13, 26) =", math.gcd(13, 26))

print("\nПеревірка взаємної простоти:")

print("18 і 24:", are_coprime(18, 24))
print("15 і 26:", are_coprime(15, 26))
print("13 і 26:", are_coprime(13, 26))

# Частина 3. Обернені елементи modulo 26

print("\nЧастина 3. Обернені елементи modulo 26:")

inverse_5 = mod_inverse(5, 26)
inverse_7 = mod_inverse(7, 26)
inverse_13 = mod_inverse(13, 26)

print("Обернений елемент для 5:", inverse_5)
print("Обернений елемент для 7:", inverse_7)
print("Обернений елемент для 13:", inverse_13)

if inverse_5 is not None:
    print("Перевірка для 5:", (5 * inverse_5) % 26)

if inverse_7 is not None:
    print("Перевірка для 7:", (7 * inverse_7) % 26)

# Частина 4. Модульне піднесення до степеня

print("\nЧастина 4. Модульне піднесення до степеня:")

result_1 = mod_pow(7, 13, 20)
result_2 = mod_pow(2, 100, 17)

print("7^13 mod 20 =", result_1)
print("2^100 mod 17 =", result_2)   

# Частина 5. Невелика збірна задача

print("\nЧастина 5. Невелика збірна задача:")

x = 19
a = 5
b = 8
n = 26

y = (a * x + b) % n

print("Початкове x =", x)
print("a =", a)
print("b =", b)
print("n =", n)
print("y =", y)

inverse_a = mod_inverse(a, n)

print("Обернений елемент для a =", inverse_a)

x_restored = (inverse_a * (y - b)) % n

print("Відновлене x =", x_restored)

assert x_restored == x

print("x успішно відновлено")

# Частина 6. Самоперевірки

print("\nЧастина 6. Самоперевірки:")

assert are_coprime(15, 26) is True
assert are_coprime(13, 26) is False
assert mod_pow(7, 13, 20) == 7
assert mod_inverse(5, 26) == 21
assert mod_inverse(13, 26) is None

print("Усі самоперевірки пройдено успішно")

print("LAB2_OK")
