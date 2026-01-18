def probability_to_moneyline(p):
    if p <= 0 or p >= 1:
        return None
    return int(-100 * (p / (1 - p))) if p > 0.5 else int(100 * ((1 - p) / p))
