import hashlib
import itertools

TARGET = "c33b0af4bb5df723c4bbf80f56122a7ecd78b791f4da64cf8689fa415540d78f"

def sha256_hex(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()

def hamming_distance_hex(a: str, b: str) -> int:
    # Compare bit-level distance
    return bin(int(a, 16) ^ int(b, 16)).count("1")

def common_prefix_len(a: str, b: str) -> int:
    n = 0
    for x, y in zip(a, b):
        if x == y:
            n += 1
        else:
            break
    return n

def variants(s: str):
    s = s.strip()
    return {
        s,
        s.lower(),
        s.upper(),
        s.replace(" ", ""),
        s.lower().replace(" ", ""),
    }

best_hamming = float("inf")
best_prefix = 0
best_hamming_hit = None
best_prefix_hit = None

with open("cheese_list.txt", "r", encoding="utf-8", errors="ignore") as f:
    cheeses = [line.strip() for line in f if line.strip()]

for cheese in cheeses:
    for v in variants(cheese):
        text = v.encode("utf-8")

        for salt in range(256):
            salt_hex = f"{salt:02x}"
            salt_ascii = salt_hex.encode("utf-8")
            salt_raw = bytes.fromhex(salt_hex)

            candidates = [
                salt_ascii + text,
                text + salt_ascii,
                salt_raw + text,
                text + salt_raw,
            ]

            for c in candidates:
                h = sha256_hex(c)

                # Exact match
                if h == TARGET:
                    print("✅ EXACT MATCH FOUND")
                    print("Cheese:", cheese)
                    print("Variant:", repr(v))
                    print("Salt hex:", salt_hex)
                    print("Bytes used:", c)
                    exit()

                # Hamming distance
                hd = hamming_distance_hex(h, TARGET)
                if hd < best_hamming:
                    best_hamming = hd
                    best_hamming_hit = (cheese, v, salt_hex, h)

                # Prefix similarity
                cp = common_prefix_len(h, TARGET)
                if cp > best_prefix:
                    best_prefix = cp
                    best_prefix_hit = (cheese, v, salt_hex, h)

print("❌ No exact match found.\n")

print("🟨 Closest by Hamming distance:")
print("Distance:", best_hamming)
print("Cheese:", best_hamming_hit[0])
print("Variant:", repr(best_hamming_hit[1]))
print("Salt:", best_hamming_hit[2])
print("Hash:", best_hamming_hit[3])
print()

print("🟦 Most similar by prefix:")
print("Common hex prefix length:", best_prefix)
print("Cheese:", best_prefix_hit[0])
print("Variant:", repr(best_prefix_hit[1]))
print("Salt:", best_prefix_hit[2])
print("Hash:", best_prefix_hit[3])
#flag: picoCTF{cHeEsY6f143c7d}