# ПІБ: Форманюк Валерій
# Група: КН-4/1
# Лабораторна робота №7
# Тема: Дослідження AES

from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes


def encrypt_block(key: bytes, block: bytes) -> bytes:
    cipher = Cipher(algorithms.AES(key), modes.ECB())
    encryptor = cipher.encryptor()
    return encryptor.update(block) + encryptor.finalize()


key = bytes.fromhex("00112233445566778899aabbccddeeff")
block1 = b"MEET AT 10:00!!!"

assert len(key) == 16
assert len(block1) == 16

c1 = encrypt_block(key, block1)

print("BLOCK1:", block1)
print("C1 HEX:", c1.hex())

assert len(c1) == 16

