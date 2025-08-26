import itertools
import re
from .utils import dob_variations

SYMBOLS = set('@_-.$!#%&*?')
LEET_MAP = {
    's': ['s', '$', '5'],
    'o': ['o', '0'],
    'i': ['i', '1', '!'],
    'e': ['e', '3'],
    'l': ['l', '1', '|'],
    't': ['t', '7'],
}

# Top breached/common passwords (short curated list)
BREACHED_TOP = [
    "123456", "123456789", "qwerty", "password", "1234567", "12345678", "12345",
    "111111", "123123", "abc123", "1234567890", "password1", "000000", "iloveyou",
    "admin", "welcome", "monkey", "dragon", "football", "letmein", "login",
    "princess", "sunshine", "master", "shadow"
]

def conservative_leet_variants(word: str, cap: int = 128):
    if not word:
        return set()
    variants = ['']
    for ch in word:
        opts = LEET_MAP.get(ch.lower(), [ch])
        new = []
        for base in variants:
            for sub in opts:
                new.append(base + (sub if sub != ch.lower() else ch))
        variants = new
        if len(variants) > cap:
            variants = variants[:cap]
    return set(variants)

def case_variants(word: str):
    return {word, word.lower(), word.upper(), word.capitalize()}

def ensure_charset(pw: str, need_digit: bool, need_symbol: bool, need_upper: bool, need_lower: bool):
    has_digit = any(c.isdigit() for c in pw)
    has_upper = any(c.isupper() for c in pw)
    has_lower = any(c.islower() for c in pw)
    has_symbol = any(c in SYMBOLS for c in pw)
    ok = True
    if need_digit: ok &= has_digit
    if need_symbol: ok &= has_symbol
    if need_upper: ok &= has_upper
    if need_lower: ok &= has_lower
    return ok

def generate_passwords(
    first,
    last,
    usernames,
    emails,
    pets,
    numbers,
    dob,
    limit=5000,
    min_len=6,
    max_len=24,
    need_digit=False,
    need_symbol=False,
    need_upper=False,
    need_lower=False,
    use_leet=True,
    reversals=True,
    separators=None,
    depth=3,
    breached=False
):
    separators = separators or ["", "@", "_", "-", ".", "$"]
    pool = set()

    # Names
    if first: pool.add(first)
    if last: pool.add(last)

    # Usernames
    for u in usernames:
        if u:
            pool.add(u)
            for part in re.split(r'[._\-]+', u):
                if part:
                    pool.add(part)

    # Emails → local-part
    for e in emails:
        if e and "@" in e:
            pool.add(e.split("@")[0])

    # Pets
    for p in pets:
        if p:
            pool.add(p)

    # Numbers
    for n in numbers:
        if n:
            pool.add(n)

    # DOB tokens
    for d in dob_variations(dob):
        pool.add(d)

    # Transform tokens
    transformed = set()
    for t in pool:
        transformed.update(case_variants(t))
        if use_leet:
            transformed.update(conservative_leet_variants(t))
        if reversals and len(t) > 2:
            transformed.add(t[::-1])

    generated = set()

    def safe_add(pw):
        if pw and len(generated) < limit * 20:  # soft cap
            generated.add(pw)

    # Add numbers + common suffixes
    explicit_numbers = list(numbers)
    for t in ['123','1234','12345','007']:
        if t not in explicit_numbers:
            explicit_numbers.append(t)

    for token in transformed:
        for n in explicit_numbers:
            for s in separators:
                safe_add(f"{token}{s}{n}")
                safe_add(f"{n}{s}{token}")

    # Token permutations
    tokens_no_dup = list(dict.fromkeys(list(transformed)))
    for k in range(2, min(depth, 4) + 1):
        for combo in itertools.permutations(tokens_no_dup, k):
            for s in separators:
                safe_add(s.join(combo))
        if len(generated) > limit * 20:
            break

    # Breached passwords
    if breached:
        for bp in BREACHED_TOP:
            safe_add(bp)
            for t in transformed:
                safe_add(t + bp)
                safe_add(bp + t)

    # Charset + length enforcement
    final = []
    seen = set()
    for pw in sorted(generated, key=lambda s: (len(s), s)):
        if not (min_len <= len(pw) <= max_len):
            continue
        if not ensure_charset(pw, need_digit, need_symbol, need_upper, need_lower):
            continue
        if pw in seen:
            continue
        seen.add(pw)
        final.append(pw)
        if len(final) >= limit:
            break

    return final[:limit]
