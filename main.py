from chaos.chaos_index import chaos_index

weather = {
    "temperature_f": 28,
    "wind_mph": 18,
    "precip_mm": 6
}

result = chaos_index(
    market_volatility=35,
    weather=weather,
    betting_ads=5,
    bk_ads=2,
    mc_ads=1,
    referee_crew="high_variance_crew",
    prime_time=True,
    heart_guard=True
)

print(result)
