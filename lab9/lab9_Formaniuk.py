# ПІБ: Форманюк Валерій
# Група: КН-4/1
# Лабораторна робота №7
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

