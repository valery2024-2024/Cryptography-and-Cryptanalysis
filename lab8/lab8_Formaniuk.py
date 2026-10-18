# ПІБ: Форманюк Валерій
# Група: КН-4/1
# Лабораторна робота №8
# Тема: Режими ECB, CBC і CTR

from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes

def encrypt(key: bytes, mode, data: bytes) -> bytes:
    cipher = Cipher(algorithms.AES(key), mode)
    encryptor = cipher.encryptor()
    return encryptor.update(data) + encryptor.finalize()

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

