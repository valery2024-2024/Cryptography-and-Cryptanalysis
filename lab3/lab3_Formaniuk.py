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
