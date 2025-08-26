import itertools
import re

def combine_tokens(tokens, separators):
    for sep in separators:
        for combo in itertools.permutations(tokens, 2):
            yield sep.join(combo)

def dob_variations(dob: str):
    """
    Generate variations of DOB (year, month, day combos).
    Supports formats:
      YYYY
      YYYYMMDD
      DDMMYYYY
      YYYY-MM-DD
      DD-MM-YYYY
      DD/MM/YYYY
    """
    if not dob:
        return []

    dob = dob.strip()
    tokens = set()

    # If only year
    if re.fullmatch(r"\d{4}", dob):
        tokens.add(dob)
        return list(tokens)

    # If continuous digits
    if re.fullmatch(r"\d{8}", dob):
        y, m, d = dob[:4], dob[4:6], dob[6:]
        tokens.update(_build_dob_tokens(y, m, d))
        return list(tokens)

    # Split with -, /, .
    parts = re.split(r"[-/.]", dob)
    if len(parts) == 3:
        # guess format
        if len(parts[0]) == 4:  # YYYY-MM-DD
            y, m, d = parts
        elif len(parts[2]) == 4:  # DD-MM-YYYY
            d, m, y = parts
        else:
            return [dob]
        tokens.update(_build_dob_tokens(y, m, d))
        return list(tokens)

    return [dob]

def _build_dob_tokens(y, m, d):
    """Helper to generate many DOB patterns"""
    tokens = set()
    # Normalize to 2-digit day/month
    m = m.zfill(2)
    d = d.zfill(2)

    yy = y[-2:]  # last 2 digits of year

    tokens.update({y, yy, m, d})
    tokens.update({
        d+m, m+d, y+m, m+y, d+y, y+d,
        d+m+y, y+m+d, m+d+y,
        yy+m+d, d+m+yy, m+d+yy
    })
    tokens.update({
        d+m+y, y+m+d, m+d+y,
        d+m+yy, yy+m+d, m+d+yy
    })
    return tokens
