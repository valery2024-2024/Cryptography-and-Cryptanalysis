# ПІБ: Форманюк Валерій
# Група: КН-4/1
# Лабораторна робота №10
# Тема: Шифрування файлів за допомогою AES-GCM

from pathlib import Path
from secrets import token_bytes
from tempfile import TemporaryDirectory

from cryptography.exceptions import InvalidTag
from cryptography.hazmat.primitives.ciphers.aead import AESGCM


MAGIC = b"EDU1"
NONCE_SIZE = 12


def encrypt_file(source: Path, target: Path, key: bytes) -> None:
    plaintext = source.read_bytes()
    nonce = token_bytes(NONCE_SIZE)

    payload = AESGCM(key).encrypt(nonce, plaintext, MAGIC)
    target.write_bytes(MAGIC + nonce + payload)

def decrypt_file(source: Path, target: Path, key: bytes) -> None:
    blob = source.read_bytes()
    minimum = len(MAGIC) + NONCE_SIZE + 16

    if not blob.startswith(MAGIC) or len(blob) < minimum:
        raise ValueError("Unknown or damaged file format")

    nonce = blob[len(MAGIC):len(MAGIC) + NONCE_SIZE]
    payload = blob[len(MAGIC) + NONCE_SIZE:]

    plaintext = AESGCM(key).decrypt(nonce, payload, MAGIC)
    target.write_bytes(plaintext)

with TemporaryDirectory() as directory:
    folder = Path(directory)

    original = folder / "request.txt"
    encrypted = folder / "request.edu"
    restored = folder / "restored.txt"

    original.write_bytes(b"Request #42: status=NEW\n")

    key = AESGCM.generate_key(bit_length=128)

    encrypt_file(original, encrypted, key)
    decrypt_file(encrypted, restored, key)

    assert restored.read_bytes() == original.read_bytes()
    print("ROUNDTRIP_OK")

    # TODO 5: змінити один байт payload.
    # TODO 6: перевірити InvalidTag.
    # TODO 7: додати результати та NOTE.
