#!/usr/bin/env python3
"""
RSA ATTACKS COMPREHENSIVE GUIDE
================================
This guide explains different RSA attack scenarios and when to use each.
"""

import math
from sympy import isprime, factorint, mod_inverse
from gmpy2 import iroot

def print_section(title):
    """Pretty print section headers"""
    print("\n" + "="*70)
    print(f"  {title}")
    print("="*70 + "\n")


# ============================================================================
# PART 1: UNDERSTANDING RSA BASICS
# ============================================================================

print_section("PART 1: RSA BASICS - How RSA Works")

print("""
RSA ENCRYPTION FORMULA:
    c = m^e mod n
    
    Where:
    - m = plaintext message (as a number)
    - e = public exponent
    - n = modulus (n = p * q, where p and q are prime)
    - c = ciphertext

RSA DECRYPTION FORMULA:
    m = c^d mod n
    
    Where:
    - d = private exponent
    - d is calculated as: d = e^(-1) mod φ(n)
    - φ(n) = (p-1)(q-1)  [Euler's totient function]

EXAMPLE:
""")

# Simple RSA example
p, q = 61, 53
n = p * q
phi = (p - 1) * (q - 1)
e = 17
d = mod_inverse(e, phi)

message = 42
ciphertext = pow(message, e, n)
decrypted = pow(ciphertext, d, n)

print(f"  p = {p}, q = {q}")
print(f"  n = p * q = {n}")
print(f"  φ(n) = (p-1)(q-1) = {phi}")
print(f"  e = {e}")
print(f"  d = e^(-1) mod φ(n) = {d}")
print(f"\n  Original message: {message}")
print(f"  Encrypted: {message}^{e} mod {n} = {ciphertext}")
print(f"  Decrypted: {ciphertext}^{d} mod {n} = {decrypted}")


# ============================================================================
# PART 2: SMALL EXPONENT ATTACK (e is small)
# ============================================================================

print_section("PART 2: SMALL EXPONENT ATTACK")

print("""
WHEN TO USE:
    When e is VERY SMALL (like e = 3, 5, 17, 20, etc.)
    
WHY IT WORKS:
    If the message m is small enough, then m^e might be SMALLER than n.
    
    Normal RSA: c = m^e mod n  (wraps around at n)
    Attack case: c = m^e       (no wrapping! direct equality)
    
    Think of it like a clock:
    - Normal: 25 mod 12 = 1 (wraps around)
    - Attack: 8 mod 12 = 8 (no wrapping needed)

HOW TO DETECT:
    1. Check if e is small (typically e < 100)
    2. Try taking the e-th root of c
    3. If you get an exact integer, you found m!

FORMULA:
    If m^e < n, then:
    m = ⁿ√c  (the e-th root of c)

EXAMPLE:
""")

# Small exponent attack example
def small_exponent_attack(c, e, n):
    """
    Attempt small exponent attack
    Returns (success, message)
    """
    print(f"  Given: c = {c}, e = {e}, n = {n}")
    print(f"\n  Step 1: Try taking the {e}-th root of c")
    
    # Try direct root
    m, is_exact = iroot(c, e)
    
    if is_exact:
        print(f"  Step 2: Got EXACT root! m = {m}")
        print(f"  Step 3: Verify: {m}^{e} = {pow(m, e)}")
        print(f"  Step 4: Compare: c = {c}")
        
        if pow(m, e) == c:
            print(f"  ✓ SUCCESS! m^{e} < n, so c = m^{e} exactly")
            return True, m
    else:
        print(f"  Step 2: No exact root (got {m} with remainder)")
        print(f"  This means m^{e} >= n, need different attack")
        return False, None
    
    return False, None

# Example with small message
small_m = 42
small_e = 5
small_n = 1000000  # Large n
small_c = pow(small_m, small_e)  # No modulo!

print("Example where m^e < n:")
success, recovered = small_exponent_attack(small_c, small_e, small_n)


# ============================================================================
# PART 3: SMALL EXPONENT WITH PADDING (Hastad's Attack)
# ============================================================================

print_section("PART 3: SMALL EXPONENT WITH PADDING")

print("""
WHEN TO USE:
    When e is small BUT m^e > n (the simple attack didn't work)
    
WHY IT HAPPENS:
    The message was large enough that m^e wrapped around n
    So: c = m^e mod n = m^e - k*n  (for some integer k)
    
    Therefore: m^e = c + k*n

HOW TO ATTACK:
    Try different values of k until you find the right one:
    For k = 0, 1, 2, 3, ... :
        Try taking e-th root of (c + k*n)
        If you get exact integer, that's m!

EXAMPLE:
""")

def small_exponent_with_padding(c, e, n, max_k=1000):
    """
    Try small exponent attack with k*n padding
    """
    print(f"  Given: c = {c}, e = {e}")
    print(f"  n = {n}")
    print(f"\n  Trying c + k*n for different k values...")
    
    for k in range(max_k):
        candidate_value = c + k * n
        m, is_exact = iroot(candidate_value, e)
        
        if is_exact:
            print(f"\n  ✓ Found at k = {k}!")
            print(f"  m^{e} = c + {k}*n")
            print(f"  m = {m}")
            
            # Verify
            actual = pow(m, e, n)
            print(f"  Verification: {m}^{e} mod {n} = {actual}")
            print(f"  Given c = {c}")
            print(f"  Match: {actual == c}")
            return True, m
    
    print(f"  ✗ No solution found in first {max_k} values of k")
    return False, None

# Example where we need padding
p2, q2 = 1009, 1013
n2 = p2 * q2
e2 = 3
m2 = 5000  # Larger message
c2 = pow(m2, e2, n2)

print(f"Example where m^e > n (needs padding):")
print(f"  m = {m2}, m^{e2} = {pow(m2, e2)} > n = {n2}")
success2, recovered2 = small_exponent_with_padding(c2, e2, n2)


# ============================================================================
# PART 4: FACTORING N (When n is small or has small factors)
# ============================================================================

print_section("PART 4: FACTORING ATTACK")

print("""
WHEN TO USE:
    When n is small enough to factor OR has small prime factors
    
WHY IT WORKS:
    If we can factor n = p * q, we can calculate:
    - φ(n) = (p-1)(q-1)
    - d = e^(-1) mod φ(n)
    - Then decrypt: m = c^d mod n

HOW TO DETECT:
    1. Check if n is small (< 100 digits might be factorable)
    2. Try basic factorization
    3. Use online tools like factordb.com for larger numbers

EXAMPLE:
""")

def factoring_attack(c, e, n):
    """
    Factor n and decrypt normally
    """
    print(f"  Given: c = {c}, e = {e}, n = {n}")
    print(f"\n  Step 1: Try to factor n")
    
    # Try factoring (only works for small n)
    factors = factorint(n)
    print(f"  Factors found: {factors}")
    
    if len(factors) != 2:
        print("  ✗ n doesn't have exactly 2 prime factors")
        return False, None
    
    primes = list(factors.keys())
    p, q = primes[0], primes[1]
    
    print(f"\n  Step 2: Found p = {p}, q = {q}")
    print(f"  Verify: p * q = {p * q} = n")
    
    # Calculate phi
    phi = (p - 1) * (q - 1)
    print(f"\n  Step 3: Calculate φ(n) = (p-1)(q-1) = {phi}")
    
    # Calculate d
    d = mod_inverse(e, phi)
    print(f"  Step 4: Calculate d = e^(-1) mod φ(n) = {d}")
    
    # Decrypt
    m = pow(c, d, n)
    print(f"\n  Step 5: Decrypt: m = c^d mod n = {m}")
    
    # Verify
    verify = pow(m, e, n)
    print(f"  Verification: {m}^{e} mod {n} = {verify}")
    print(f"  Matches c = {c}? {verify == c}")
    
    return True, m

# Example with factorable n
p3, q3 = 307, 311
n3 = p3 * q3
e3 = 65537
m3 = 1337
c3 = pow(m3, e3, n3)

success3, recovered3 = factoring_attack(c3, e3, n3)


# ============================================================================
# PART 5: DECISION TREE - WHICH ATTACK TO USE?
# ============================================================================

print_section("PART 5: DECISION TREE - CHOOSING THE RIGHT ATTACK")

print("""
STEP-BY-STEP DECISION PROCESS:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

START: You have n, e, and c
    │
    ├─→ Is e SMALL? (e < 100, especially e = 3, 5, 17, 20, etc.)
    │   │
    │   YES → Try SMALL EXPONENT ATTACK
    │   │     1. Compute m = ⁿ√c (e-th root of c)
    │   │     2. Check if it's an exact integer
    │   │     3. If YES → Found m! ✓
    │   │     4. If NO → Try with padding: m = ⁿ√(c + k*n) for k=0,1,2...
    │   │
    │   NO → Go to next check
    │
    ├─→ Is n SMALL or potentially factorable? (< 100 digits)
    │   │
    │   YES → Try FACTORING ATTACK
    │   │     1. Factor n = p * q
    │   │     2. Calculate φ(n) = (p-1)(q-1)
    │   │     3. Calculate d = e^(-1) mod φ(n)
    │   │     4. Decrypt m = c^d mod n ✓
    │   │
    │   NO → Go to next check
    │
    ├─→ Do you have multiple related ciphertexts?
    │   │
    │   YES → Try advanced attacks:
    │   │     - Hastad's Broadcast Attack (same m, different n)
    │   │     - Common Modulus Attack (same n, different e)
    │   │
    │   NO → Go to next check
    │
    ├─→ Is d small? (Wiener's attack)
    │   │
    │   YES → Try WIENER'S ATTACK
    │   │
    │   NO → Might need quantum computer or better factoring! 😅

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

QUICK REFERENCE:
    Attack Type          | When to Use              | Formula
    ─────────────────────┼──────────────────────────┼─────────────────────
    Small Exponent       | e small, m^e < n         | m = ⁿ√c
    Small e w/ Padding   | e small, m^e >= n        | m = ⁿ√(c + k*n)
    Factoring            | n is small/factorable    | m = c^d mod n
    Common Modulus       | Same n, diff e, same m   | Use Bezout identity
    Hastad Broadcast     | Same m, diff n, small e  | Chinese Remainder
    Wiener's Attack      | d is small (d < n^0.25)  | Continued fractions
""")


# ============================================================================
# PART 6: AUTOMATED ATTACK SELECTOR
# ============================================================================

print_section("PART 6: AUTOMATED ATTACK FUNCTION")

def auto_rsa_attack(c, e, n, verbose=True):
    """
    Automatically try different RSA attacks
    Returns (attack_name, success, message)
    """
    if verbose:
        print("AUTO-ATTACK ANALYZER")
        print("-" * 70)
    
    # Check 1: Small exponent attack
    if e < 100:
        if verbose:
            print(f"[*] e = {e} is small, trying small exponent attack...")
        
        # Try direct root
        m, is_exact = iroot(c, e)
        if is_exact and pow(m, e) == c:
            if verbose:
                print(f"[✓] SUCCESS with small exponent attack!")
            return "Small Exponent (Direct)", True, int(m)
        
        # Try with padding
        if verbose:
            print(f"[*] Direct root failed, trying with padding...")
        for k in range(1, 1000):
            m, is_exact = iroot(c + k * n, e)
            if is_exact:
                if pow(m, e, n) == c:
                    if verbose:
                        print(f"[✓] SUCCESS with small exponent + padding (k={k})!")
                    return "Small Exponent (Padded)", True, int(m)
        
        if verbose:
            print(f"[✗] Small exponent attack failed")
    
    # Check 2: Try factoring (only for small n)
    if n.bit_length() < 100:  # Only try for small n
        if verbose:
            print(f"[*] n is small ({n.bit_length()} bits), trying factorization...")
        try:
            factors = factorint(n)
            if len(factors) == 2:
                primes = list(factors.keys())
                p, q = primes[0], primes[1]
                phi = (p - 1) * (q - 1)
                d = mod_inverse(e, phi)
                m = pow(c, d, n)
                if verbose:
                    print(f"[✓] SUCCESS with factoring attack!")
                return "Factoring", True, int(m)
        except:
            if verbose:
                print(f"[✗] Factoring failed")
    
    if verbose:
        print(f"[✗] No successful attack found")
    return "None", False, None

print("""
This function automatically tries different attacks in order:
1. Small exponent (direct)
2. Small exponent with padding
3. Factoring (if n is small)

Let's test it on your original challenge:
""")

# Your original challenge
original_n = 794255034746217481118036680899583713769169740477058311080577863775258905535083733037086757146665776285141378769394236594018940553611332992015235611301392435331686893327638497463451141131121854175109032847220628711604240090141702370582207267865838579903544063969512589163089703251557843902347332372479932901257678070485626866870068200954461442066498744716842052598619189342900869642847249705202850687326785008493786083785536017804222159556030751607146389742017415096897578206064602649589029346401386193933615396269328531001094449657422327455657091015449205641522121985874459964573385634331177830193716055948573290740952172295628509411813225340712749715136767338338793448769690449442584531173443102727238094033280907748584838488727998588186003349989474485509603364701677387420626344199346865242783960165832896865476356702189749705968576362856529566638597465690401839343660610364389596030231848196060093959105223835736129070873011847318314002583546380929710768043397411291121090355540904402220873838809244417090163813012960046609582422912805466612945345856725453940581347457935203572741984932571426958237545071606843118730313575533621824103053720771542108545424614567612294059227601587136824669339208845696331105502717963406115446804131
original_e = 20
original_c = 640637430810406857500566702096274079968637575083735371083428610559494246312953917690058478151815544700749263717343270608189375318041647659967907117318128547925863719412915646909472409011741637121425660944971769483646407795839386558652979547865322798857240273119228637208800827339672152896017863904278368373307140953373609489015820257671180087293246795123914811911124249667648409273234622120436841305277752315379610986699843797119339332070450522422989912187217927801952856040046343274735734136012268942541861762433046766626147798915278309790539995250335851239645434779948928005064969277695866915259424547079818225562552772162759544858077133422957528987269950191066126664890009765399948568334341698956743331274220555023207625340470481495405120528845772296710199603227433693485680593910257633268143078667439988309298976205405141305894665142891463590466673498829588844544209007238455392215569578460669771538835863104199510188197971496927867639157318426618822331560242691613668465685175187862481997395503215892109106221244693284012810373844532867413594848653804799267237833096247446369850719958286696762624107678123670990841855184955687410838557069286801

attack_type, success, message = auto_rsa_attack(original_c, original_e, original_n)

if success:
    print(f"\n[+] Attack used: {attack_type}")
    print(f"[+] Recovered message (int): {message}")
    try:
        flag = message.to_bytes((message.bit_length() + 7) // 8, 'big').decode('ascii')
        print(f"[+] FLAG: {flag}")
    except:
        print(f"[+] Message: {message}")


print_section("SUMMARY - KEY TAKEAWAYS")

print("""
1. SMALL EXPONENT ATTACK (e < 100):
   - Try: m = ⁿ√c
   - If no exact root, try: m = ⁿ√(c + k*n)
   
2. FACTORING ATTACK (small n):
   - Factor n = p * q
   - Calculate d = e^(-1) mod (p-1)(q-1)
   - Decrypt: m = c^d mod n

3. DECISION PROCESS:
   - e small? → Small exponent attack
   - n small? → Factoring attack
   - Multiple ciphertexts? → Advanced attacks
   - Otherwise? → Might be secure (or need advanced tools)

4. ALWAYS TRY IN ORDER:
   a) Small exponent (fastest)
   b) Factoring (medium speed)
   c) Advanced attacks (slower)

Good luck with your CTF challenges! 🚀
""")