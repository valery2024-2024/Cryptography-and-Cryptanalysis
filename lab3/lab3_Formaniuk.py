# ПІБ: Форманюк Валерій Володимирович
# Група: КН-4/1
# Лабораторна робота №3
# Тема: Шифри Цезаря та афінний шифр

from math import gcd
# Частина 1. Шифр Цезаря

def caesar_encrypt(text: str, shift: int) -> str:
    result = ""
    shift = shift % 26

    for char in text:
        if "A" <= char <= "Z":
            x = ord(char) - ord("A")
            y = (x + shift) % 26
            result += chr(y + ord("A"))
        else:
            result += char

    return result

def caesar_decrypt(text: str, shift: int) -> str:
    result = ""
    shift = shift % 26

    for char in text:
        if "A" <= char <= "Z":
            y = ord(char) - ord("A")
            x = (y - shift) % 26
            result += chr(x + ord("A"))
        else:
            result += char

    return result

# Частина 2. Перевірка affine-ключа

def is_valid_affine_key(a: int) -> bool:
    return gcd(a, 26) == 1

# Частина 3. Афінний шифр

def affine_encrypt(text: str, a: int, b: int) -> str:
    if not is_valid_affine_key(a):
        raise ValueError("Некоректний affine-ключ a")

    result = ""
    b = b % 26

    for char in text:
        if "A" <= char <= "Z":
            x = ord(char) - ord("A")
            y = (a * x + b) % 26
            result += chr(y + ord("A"))
        else:
            result += char

    return result

def affine_decrypt(text: str, a: int, b: int) -> str:
    if not is_valid_affine_key(a):
        raise ValueError("Некоректний affine-ключ a")

    result = ""
    b = b % 26
    inverse_a = pow(a, -1, 26)

    for char in text:
        if "A" <= char <= "Z":
            y = ord(char) - ord("A")
            x = (inverse_a * (y - b)) % 26
            result += chr(x + ord("A"))
        else:
            result += char

    return result

print("Частина 1. Шифр Цезаря")

text = "HELLO"
shift = 3

encrypted = caesar_encrypt(text, shift)
decrypted = caesar_decrypt(encrypted, shift)

print("Початковий текст:", text)
print("Shift:", shift)
print("Зашифрований текст:", encrypted)
print("Розшифрований текст:", decrypted)

test_text = "ATTACK AT DAWN!"
test_encrypted = caesar_encrypt(test_text, 7)
test_decrypted = caesar_decrypt(test_encrypted, 7)

print("\nДодаткова перевірка:")
print("Початковий текст:", test_text)
print("Зашифрований текст:", test_encrypted)
print("Розшифрований текст:", test_decrypted)

print("\nЧастина 2. Перевірка affine-ключа")

print("a = 5:", is_valid_affine_key(5))
print("a = 13:", is_valid_affine_key(13))
print("a = 2:", is_valid_affine_key(2))

print("\nЧастина 3. Афінний шифр")

affine_text = "HELLO"
a = 5
b = 8

affine_encrypted = affine_encrypt(affine_text, a, b)
affine_decrypted = affine_decrypt(affine_encrypted, a, b)

print("Початковий текст:", affine_text)
print("Ключ a =", a)
print("Ключ b =", b)
print("Зашифрований текст:", affine_encrypted)
print("Розшифрований текст:", affine_decrypted)
