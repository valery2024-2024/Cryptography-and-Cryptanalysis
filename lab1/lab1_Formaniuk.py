# Форманюк Валерій Володимирович
# Група: КН-4/1
# Лабораторна робота №1
# Тема: Байти, Hex, Base64 і XOR

import base64

# Частина 3. Обов'язкові функції
def to_hex(data: bytes) -> str:
    return data.hex()
def from_hex(value: str) -> bytes:
    return bytes.fromhex(value)
def to_base64(data: bytes) -> str:
    encoded = base64.b64encode(data)
    return encoded.decode("ascii")
def from_base64(value: str) -> bytes:
    return base64.b64decode(value)
def xor_bytes(data: bytes, key: bytes) -> bytes:
    if len(data) != len(key):
        raise ValueError("data і key повинні мати однакову довжину")
    return bytes(a ^ b for a, b in zip(data, key))

# Частина 1. Текст, bytes і Hex
text = "СТО Rivne 2026"
print("Початковий текст:", text)
data = text.encode("utf-8")
print("Bytes:", data)
print("Кількість символів:", len(text))
print("Кількість байтів:", len(data))
hex_value = data.hex()
print("Hex:", hex_value)
restored_bytes = bytes.fromhex(hex_value)
print("Відновлені bytes:", restored_bytes)
restored_text = restored_bytes.decode("utf-8")
print("Відновлений текст:", restored_text)
assert restored_text == text

# Частина 2. Base64
base64_encoded = base64.b64encode(data)
print("\nBase64:", base64_encoded.decode("ascii"))
base64_decoded = base64.b64decode(base64_encoded)
print("Bytes після Base64 декодування:", base64_decoded)
base64_restored_text = base64_decoded.decode("utf-8")
print("Текст після Base64 декодування:", base64_restored_text)
assert base64_restored_text == text

print("\nПеревірка функцій:")
test_data = b"abc"
print("to_hex:", to_hex(test_data))
print("from_hex:", from_hex(to_hex(test_data)))
print("to_base64:", to_base64(test_data))
print("from_base64:", from_base64(to_base64(test_data)))

# Частина 4. XOR над послідовністю байтів

print("\nЧастина 4. XOR:")
data = b"HELLO"
key = bytes([3, 1, 4, 1, 5])
xor_result = xor_bytes(data, key)
print("Початкові дані:", data)
print("Ключ:", key)
print("Результат XOR у Hex:", xor_result.hex())
restored_data = xor_bytes(xor_result, key)
print("Відновлені дані:", restored_data)
assert restored_data == b"HELLO"
try:
    xor_bytes(b"ABC", b"XY")
except ValueError:
    print("ValueError успішно перевірено")
# Частина 5. Робота з невеликим файлом

print("\nЧастина 5. Робота з файлами:")

input_text = """Це лабораторна робота №1.
Я працюю з bytes, Hex і Base64.
Також вивчаю операцію XOR.
СТО Rivne 2026.
"""
# Створення початкового текстового файла
with open("lab1_input.txt", "w", encoding="utf-8") as file:
    file.write(input_text)
print("Файл lab1_input.txt створено")
# Читання початкового файла як bytes
with open("lab1_input.txt", "rb") as file:
    original_bytes = file.read()
print("Початкові bytes прочитано")
# Кодування bytes у Base64
encoded_bytes = base64.b64encode(original_bytes)
# Запис Base64 у файл
with open("lab1_encoded.txt", "wb") as file:
    file.write(encoded_bytes)
print("Файл lab1_encoded.txt створено")
# Читання Base64 з файла
with open("lab1_encoded.txt", "rb") as file:
    encoded_from_file = file.read()
# Декодування Base64 назад у bytes
decoded_bytes = base64.b64decode(encoded_from_file)
# Запис відновлених bytes у новий файл
with open("lab1_restored.txt", "wb") as file:
    file.write(decoded_bytes)
print("Файл lab1_restored.txt створено")
# Перевірка, що початкові та відновлені bytes однакові
assert original_bytes == decoded_bytes
print("Початковий і відновлений файли однакові")   
# Частина 6. Самоперевірки

print("\nЧастина 6. Самоперевірки:")
assert from_hex(to_hex(b"abc")) == b"abc"
sample = "Привіт 123".encode("utf-8")
assert from_base64(to_base64(sample)) == sample
data = b"HELLO"
key = bytes([3, 1, 4, 1, 5])
assert xor_bytes(xor_bytes(data, key), key) == data
print("Усі три самоперевірки пройдено успішно")

# Частина 7. Коротке пояснення Base64
BASE64_EXPLANATION = """
Base64 не є шифруванням, тому що він лише змінює представлення даних.
Для використання Base64 не потрібен секретний ключ.
Будь-яка людина може стандартними засобами декодувати Base64 назад.
Тому Base64 не забезпечує конфіденційність даних.
"""
print("\nЧастина 7. Пояснення Base64:")
print(BASE64_EXPLANATION)
print("LAB1_OK")
