import math
import string

ALPH = string.ascii_uppercase

def modinv(a, m=26):
    a %= m
    for x in range(m):
        if (a * x) % m == 1:
            return x
    return None

def affine_encrypt(pt, a, b):
    out = []
    for ch in pt.upper():
        if 'A' <= ch <= 'Z':
            x = ord(ch) - 65
            y = (a * x + b) % 26
            out.append(chr(y + 65))
        else:
            out.append(ch)
    return "".join(out)

def affine_decrypt(ct, a, b):
    ainv = modinv(a, 26)
    if ainv is None:
        return None
    out = []
    for ch in ct.upper():
        if 'A' <= ch <= 'Z':
            y = ord(ch) - 65
            x = (ainv * (y - b)) % 26
            out.append(chr(x + 65))
        else:
            out.append(ch)
    return "".join(out)

def valid_a_values():
    return [a for a in range(26) if math.gcd(a, 26) == 1]

def find_keys_from_pair(plain, cipher):
    plain = plain.upper()
    cipher = cipher.upper()

    candidates = []
    for a in valid_a_values():
        for b in range(26):
            if affine_encrypt(plain, a, b) == cipher:
                candidates.append((a, b))
    return candidates

if __name__ == "__main__":
    # 1) Paste what the GAME actually gave you (same session)
    known_plain  = "CHEDDAR"
    known_cipher = "IXOLLCB"  # <-- replace this

    # 2) Paste the session secret ciphertext
    secret_cipher = "MCEICBVSPOJXU"

    keys = find_keys_from_pair(known_plain, known_cipher)

    print(f"Keys matching {known_plain}->{known_cipher}: {keys}")

    # If there are multiple keys, encrypt a second cheese in-game and add another filter
    # Example:
    # second_plain  = "FETA"
    # second_cipher = "PASTE_SECOND_OUTPUT"
    # keys = [k for k in keys if affine_encrypt(second_plain, k[0], k[1]) == second_cipher]

    if len(keys) == 1:
        a, b = keys[0]
        print("Confirmed key:", (a, b))
        print("Decrypted secret:", affine_decrypt(secret_cipher, a, b))
    else:
        print("If this list isn't exactly 1 key, encrypt ONE more cheese (like FETA) and filter.")
#flag: picoCTF{ChEeSy1efea9ba}