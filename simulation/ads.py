def ad_pressure_score(betting_ads, bk_ads, mc_ads):
    score = betting_ads * 4 + bk_ads * 6 - mc_ads * 3
    return max(0, min(100, score))
