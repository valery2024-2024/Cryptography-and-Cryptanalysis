# ПІБ: Форманюк Валерій
# Група: КН-4/1
# Лабораторна робота №8
# Тема: Режими ECB, CBC і CTR

from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes

def encrypt(key: bytes, mode, data: bytes) -> bytes:
    cipher = Cipher(algorithms.AES(key), mode)
    encryptor = cipher.encryptor()
    return encryptor.update(data) + encryptor.finalize()

def decrypt(key: bytes, mode, data: bytes) -> bytes:
    cipher = Cipher(algorithms.AES(key), mode)
    decryptor = cipher.decryptor()
    return decryptor.update(data) + decryptor.finalize()

def split_blocks(data: bytes, size: int = 16):
    return [data[i:i + size] for i in range(0, len(data), size)]


def print_blocks(label: str, data: bytes):
    print(label)
    for i, part in enumerate(split_blocks(data), start=1):
        print(f"  block {i}: {part.hex()}")

key = bytes.fromhex("00112233445566778899aabbccddeeff")

iv1 = bytes.fromhex("000102030405060708090a0b0c0d0e0f")
iv2 = bytes.fromhex("101112131415161718191a1b1c1d1e1f")

counter1 = bytes.fromhex("202122232425262728292a2b2c2d2e2f")
counter2 = bytes.fromhex("303132333435363738393a3b3c3d3e3f")

block = b"0123456789ABCDEF"
plaintext = block * 3

assert len(block) == 16
assert len(plaintext) == 48

print_blocks("PLAINTEXT", plaintext)

p_blocks = split_blocks(plaintext)

assert p_blocks[0] == p_blocks[1] == p_blocks[2]

ecb_ciphertext = encrypt(key, modes.ECB(), plaintext)

print_blocks("ECB", ecb_ciphertext)

ecb_blocks = split_blocks(ecb_ciphertext)

assert ecb_blocks[0] == ecb_blocks[1] == ecb_blocks[2]

# У режимі ECB кожен блок шифрується окремо
# Тому три однакові блоки plaintext дають три однакові блоки ciphertext
# Це недолік ECB тому що повтори в повідомленні залишаються помітними

cbc_ciphertext = encrypt(key, modes.CBC(iv1), plaintext)

print_blocks("CBC", cbc_ciphertext)

cbc_blocks = split_blocks(cbc_ciphertext)

assert len(set(cbc_blocks)) > 1

# У режимі CBC блоки пов'язані між собою
# тому однакові блоки plaintext дають різні результати
# IV використовується як початкове значення для першого блока
# Завдяки IV перший блок не шифрується незалежно від попереднього контексту

cbc_with_other_iv = encrypt(key, modes.CBC(iv2), plaintext)

assert cbc_with_other_iv != cbc_ciphertext

print_blocks("CBC WITH OTHER IV", cbc_with_other_iv)

# Зміна IV впливає на результат шифрування CBC
# навіть якщо ключ і початкове повідомлення залишаються однаковими
# IV не є другим секретним ключем

ctr_ciphertext = encrypt(key, modes.CTR(counter1), plaintext)

print_blocks("CTR", ctr_ciphertext)

ctr_blocks = split_blocks(ctr_ciphertext)

assert len(set(ctr_blocks)) > 1

# У режимі CTR для кожного блока змінюється значення лічильника.
# Тому однакові блоки plaintext дають різні блоки ciphertext.

ctr_with_other_counter = encrypt(key, modes.CTR(counter2), plaintext)

assert ctr_with_other_counter != ctr_ciphertext

print_blocks("CTR WITH OTHER COUNTER", ctr_with_other_counter)

# Якщо змінити початкове значення лічильника CTR
# результат шифрування того самого повідомлення зміниться
# Повторно використовувати той самий counter з тим самим ключем небезпечно

# Перевірка розшифрування трьох режимів AES

ecb_restored = decrypt(key, modes.ECB(), ecb_ciphertext)
cbc_restored = decrypt(key, modes.CBC(iv1), cbc_ciphertext)
ctr_restored = decrypt(key, modes.CTR(counter1), ctr_ciphertext)

assert ecb_restored == plaintext
assert cbc_restored == plaintext
assert ctr_restored == plaintext

print("ECB DECRYPTION OK:", ecb_restored == plaintext)
print("CBC DECRYPTION OK:", cbc_restored == plaintext)
print("CTR DECRYPTION OK:", ctr_restored == plaintext)

# Фінальні перевірки лабораторної роботи №8

assert len(plaintext) == 48
assert ecb_blocks[0] == ecb_blocks[1] == ecb_blocks[2]
assert len(set(cbc_blocks)) > 1
assert len(set(ctr_blocks)) > 1
assert cbc_with_other_iv != cbc_ciphertext
assert ctr_with_other_counter != ctr_ciphertext

assert decrypt(key, modes.ECB(), ecb_ciphertext) == plaintext
assert decrypt(key, modes.CBC(iv1), cbc_ciphertext) == plaintext
assert decrypt(key, modes.CTR(counter1), ctr_ciphertext) == plaintext

print("LAB8_OK")

# Висновок:
# ECB: однакові блоки початкового тексту дають однакові
# зашифровані блоки тому цей режим не приховує повтори
# і не підходить для реального захисту повідомлень
#
# CBC: блоки пов'язані між собою тому повтори початкового
# тексту не відображаються так як у ECB
# Зміна IV змінює результат шифрування навіть з тим самим ключем
#
# CTR: для шифрування використовується змінний лічильник
# тому однакові блоки повідомлення дають різні результати
# Зміна початкового counter також змінює ciphertext
# Повторно використовувати той самий потік лічильника
# з одним ключем небезпечно

