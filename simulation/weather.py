def weather_severity(weather):
    score = 0
    score += min(30, weather["wind_mph"] * 1.5)
    score += min(30, weather["precip_mm"] * 3)

    if weather["temperature_f"] < 32:
        score += 15
    elif weather["temperature_f"] > 90:
        score += 10

    return min(100, int(score))
