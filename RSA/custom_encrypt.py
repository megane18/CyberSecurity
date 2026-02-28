p = 97
g = 31
a = 89
b = 27

cipher = [
    33588, 276168, 261240, 302292, 343344, 328416, 242580,
    85836, 82104, 156744, 0, 309756, 78372, 18660, 253776,
    0, 82104, 320952, 3732, 231384, 89568, 100764, 22392,
    22392, 63444, 22392, 97032, 190332, 119424, 182868,
    97032, 26124, 44784, 63444
]

# Step 1: recover shared key
shared_key = pow(g, a*b, p)

# Step 2: undo multiplication
def decrypt_multiply(cipher, key):
    factor = key * 311
    out = []
    for val in cipher:
        if val == 0:
            out.append('\x00')
        else:
            out.append(chr(val // factor))
    return "".join(out)

# Step 3: undo XOR + reverse
def dynamic_xor_decrypt(cipher_text, text_key):
    temp = ""
    for i, char in enumerate(cipher_text):
        temp += chr(ord(char) ^ ord(text_key[i % len(text_key)]))
    return temp[::-1]

semi = decrypt_multiply(cipher, shared_key)
plaintext = dynamic_xor_decrypt(semi, "trudeau")

print(plaintext)
