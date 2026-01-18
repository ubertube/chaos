from simulation.ads import ad_pressure_score
from simulation.weather import weather_severity
from simulation.referees import referee_failure_score

def heart_guard_modifier(enabled):
    return 0.75 if enabled else 1.0

def chaos_index(
    market_volatility,
    weather,
    betting_ads,
    bk_ads,
    mc_ads,
    referee_crew,
    prime_time,
    heart_guard
):
    guard = heart_guard_modifier(heart_guard)

    ad_score = ad_pressure_score(betting_ads, bk_ads, mc_ads)
    weather_score = weather_severity(weather)

    chaos_pressure = (market_volatility + ad_score + weather_score) / 100 * guard

    ref_score = referee_failure_score(referee_crew, chaos_pressure, prime_time)

    total = (
        market_volatility * 0.30 +
        weather_score * 0.25 +
        ad_score * 0.20 +
        ref_score * 0.25
    ) * guard

    return {
        "chaos_index": int(min(100, total)),
        "heart_guard": heart_guard,
        "components": {
            "market": market_volatility,
            "weather": weather_score,
            "ads": ad_score,
            "referee": ref_score,
        },
    }
