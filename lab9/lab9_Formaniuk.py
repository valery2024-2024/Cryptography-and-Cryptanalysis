# ПІБ: Форманюк Валерій
# Група: КН-4/1
# Лабораторна робота №9
# Тема: AES-GCM: шифрування, цілісність і виявлення підміни

from secrets import token_bytes
from cryptography.exceptions import InvalidTag
from cryptography.hazmat.primitives.ciphers.aead import AESGCM

key = AESGCM.generate_key(bit_length=128)
aes = AESGCM(key)

nonce = token_bytes(12)

plaintext = b"Request #42: status=NEW"
aad = b"service-request:v1"
ciphertext = aes.encrypt(nonce, plaintext, aad)
restored = aes.decrypt(nonce, ciphertext, aad)
assert restored == plaintext
assert len(ciphertext) == len(plaintext) + 16

print("CIPHERTEXT+TAG:", ciphertext.hex())
print("RESTORED:", restored)

# AES-GCM додає до ciphertext 16-байтовий authentication tag
# Tag потрібен для перевірки цілісності та автентичності даних
# Nonce передається окремо і не входить до ciphertext

def rejected(candidate: bytes, candidate_aad: bytes) -> bool:
    try:
        aes.decrypt(nonce, candidate, candidate_aad)
    except InvalidTag:
        return True
    return False

tampered_body = bytearray(ciphertext)
tampered_body[0] ^= 1
tampered_body = bytes(tampered_body)
assert rejected(tampered_body, aad)

print("BODY_REJECTED:", rejected(tampered_body, aad))

tampered_tag = bytearray(ciphertext)
tampered_tag[-1] ^= 1
tampered_tag = bytes(tampered_tag)
assert rejected(tampered_tag, aad)

print("TAG_REJECTED:", rejected(tampered_tag, aad))

changed_aad = b"service-request:v2"
assert rejected(ciphertext, changed_aad)

print("AAD_REJECTED:", rejected(ciphertext, changed_aad))

nonce2 = token_bytes(12)
assert len(nonce2) == 12
assert nonce2 != nonce
ciphertext2 = aes.encrypt(nonce2, plaintext, aad)
restored2 = aes.decrypt(nonce2, ciphertext2, aad)
assert restored2 == plaintext
assert ciphertext2 != ciphertext

print("NEW_NONCE_DECRYPTION_OK:", restored2 == plaintext)
print("NEW_NONCE_CIPHERTEXT_DIFFERENT:", ciphertext2 != ciphertext)

# Для кожного нового шифрування AES-GCM з тим самим ключем
# потрібно використовувати новий nonce
# Повторне використання nonce з тим самим ключем небезпечне
# оскільки може порушити конфіденційність і цілісність даних

assert restored == plaintext
assert len(nonce) == 12
assert len(ciphertext) == len(plaintext) + 16
assert rejected(tampered_body, aad)
assert rejected(tampered_tag, aad)
assert rejected(ciphertext, b"service-request:v2")
assert len(nonce2) == 12
assert nonce2 != nonce
assert aes.decrypt(nonce2, ciphertext2, aad) == plaintext

print("LAB9_OK")

# Висновок:
# Authentication tag перевіряє цілісність і автентичність зашифрованих даних
# AAD дозволяє захистити додаткові дані від підміни без їх шифрування
# Якщо змінити ciphertext  tag або AAD  AES-GCM відхиляє дані через InvalidTag
# Для кожного нового шифрування з тим самим ключем потрібен новий nonce
# Повторне використання nonce може порушити конфіденційність і цілісність даних
# AES-GCM кращий за ECB для сучасних програм
# оскільки приховує повтори та перевіряє автентичність повідомлення

