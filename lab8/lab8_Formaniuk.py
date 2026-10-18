# ПІБ: Форманюк Валерій
# Група: КН-4/1
# Лабораторна робота №8
# Тема: Режими ECB, CBC і CTR

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

