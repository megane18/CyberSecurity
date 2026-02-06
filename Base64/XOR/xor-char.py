# def xor_char_with_int(char, key):
#     return chr(ord(char) ^ key)




# char = 'label'
# key = 13
# for c in char:
#     x = ''.join(xor_char_with_int(c, key))
#     print(x, end='')



# given three random keys that have been xor'd together and with a flag
# find the flag
# first we neeed to decode from hex to bytes

# KEY1 = 'a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313'
# KEY2_XOR_KEY1 = '37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e'
# KEY2_XOR_KEY3 = 'c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1'
# FLAG_KEY1_XOR_KEY3_XOR_KEY2 = '04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf'

# from binascii import unhexlify
# # #decode the hex strings to bytes
# key1 = unhexlify(KEY1)
# key2_xor_key1 = unhexlify(KEY2_XOR_KEY1)
# key2_xor_key3 = unhexlify(KEY2_XOR_KEY3)    
# flag_xor_key1_xor_key3_xor_key2 = unhexlify(FLAG_KEY1_XOR_KEY3_XOR_KEY2)
# print(key1)
# print(key2_xor_key1)
# print(key2_xor_key3)
# print(flag_xor_key1_xor_key3_xor_key2)

# # # next we need to xor the bytes together appropriately to get the flag
# def xor_bytes(y, z):
#     for item1, item2 in zip(y,z):
#         yield item1 ^ item2
# flag_bytes = bytes(xor_bytes(flag_xor_key1_xor_key3_xor_key2, xor_bytes(key1, key2_xor_key3)))
# print(flag_bytes)

# in this single bytes find the hidden secret message
# first decode from hext to bytes
#unknown key, we need to try all 256 possible keys
#x='73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d'
# from binascii import unhexlify
# z = unhexlify(y)
# for key in range(256):
#     decryption = []
#     for byte in z:
#         decrypted = chr(byte ^ key)
#         decryption.append(decrypted)

#     pattern= "crypto"
#     if pattern in ''.join(decryption):
#         print('Key:', key, 'Decrypted:', ''.join(decryption))
from binascii import unhexlify

ct_hex = "0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104"
ct = unhexlify(ct_hex)

prefix = b"crypto{"
L = 8

def xor_repeating(data: bytes, key: bytes) -> bytes:
    return bytes(b ^ key[i % len(key)] for i, b in enumerate(data))

def score(pt: bytes) -> int:
    # Strong “English-ish flag” scoring (no leet-math needed)
    s = 0
    if pt.startswith(b"crypto{"):
        s += 50
    if pt.endswith(b"}"):
        s += 50
    # reward common expected fragments
    for token in [b"Kn0w", b"4ll", b"y0u", b"_"]:
        s += pt.count(token) * 10
    # reward printable characters
    s += sum(1 for b in pt if 32 <= b <= 126)
    return s

# Derive first 7 bytes of the key from the known prefix
known7 = bytes(ct[i] ^ prefix[i] for i in range(len(prefix)))  # b"myXORke"

best = None  # (score, key, pt)

for last in range(256):
    key = known7 + bytes([last])   # try all possibilities for the 8th byte
    pt = xor_repeating(ct, key)

    if not pt.startswith(prefix):
        continue
    if not pt.endswith(b"}"):
        continue

    sc = score(pt)
    if best is None or sc > best[0]:
        best = (sc, key, pt)

sc, key, pt = best
print("Key (ascii):", key.decode("utf-8", errors="replace"))
print("Key (hex):", key.hex())
print("Plaintext:", pt.decode("utf-8", errors="replace"))
