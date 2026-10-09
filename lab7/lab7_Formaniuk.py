# ПІБ: Форманюк Валерій
# Група: КН-4/1
# Лабораторна робота №7
# Тема: Дослідження AES

from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes


def encrypt_block(key: bytes, block: bytes) -> bytes:
    cipher = Cipher(algorithms.AES(key), modes.ECB())
    encryptor = cipher.encryptor()
    return encryptor.update(block) + encryptor.finalize()

def decrypt_block(key: bytes, ciphertext: bytes) -> bytes:
    cipher = Cipher(algorithms.AES(key), modes.ECB())
    decryptor = cipher.decryptor()
    return decryptor.update(ciphertext) + decryptor.finalize()

def changed_bits(a: bytes, b: bytes) -> int:
    if len(a) != len(b):
        raise ValueError("lengths must match")
    return sum((x ^ y).bit_count() for x, y in zip(a, b))


key = bytes.fromhex("00112233445566778899aabbccddeeff")
block1 = b"MEET AT 10:00!!!"

assert len(key) == 16
assert len(block1) == 16

c1 = encrypt_block(key, block1)

print("BLOCK1:", block1)
print("C1 HEX:", c1.hex())

assert len(c1) == 16

c1_repeat = encrypt_block(key, block1)

assert c1_repeat == c1

print("C1 REPEAT HEX:", c1_repeat.hex())

# Якщо використовувати той самий ключ і той самий блок
# AES повертає однаковий результат шифрування
# Це нормальна властивість AES, а не помилка програми

modified = bytearray(block1)
modified[0] ^= 0x01
block2 = bytes(modified)

assert len(block2) == 16
assert changed_bits(block1, block2) == 1

print("BLOCK1:", block1)
print("BLOCK2:", block2)
print("CHANGED PLAINTEXT BITS:", changed_bits(block1, block2))
c2 = encrypt_block(key, block2)

print("C1 HEX:", c1.hex())
print("C2 HEX:", c2.hex())
print("CHANGED PLAINTEXT BITS:", changed_bits(block1, block2))
print("CHANGED CIPHERTEXT BITS:", changed_bits(c1, c2))

assert c1 != c2

# Після зміни одного біта початкового тексту
# результат шифрування AES сильно змінився
# Це і є лавинний ефект

restored = decrypt_block(key, c1)

assert restored == block1

print("RESTORED:", restored)

# Для розшифрування використовується той самий ключ
# тому що AES є симетричним алгоритмом шифрування

key2 = bytes.fromhex("ffeeddccbbaa99887766554433221100")

c_other_key = encrypt_block(key2, block1)

assert c_other_key != c1

print("OTHER KEY CIPHERTEXT:", c_other_key.hex())

# Якщо змінити ключ AES результат шифрування
# того самого повідомлення також зміниться

