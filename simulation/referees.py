NFL_REFEREE_PROFILES = {
    "low_variance_crew": {"base_error_rate": 0.02, "pressure_multiplier": 0.8},
    "average_crew": {"base_error_rate": 0.04, "pressure_multiplier": 1.0},
    "high_variance_crew": {"base_error_rate": 0.07, "pressure_multiplier": 1.3},
}

def referee_failure_score(crew_type, chaos_pressure, prime_time=False):
    profile = NFL_REFEREE_PROFILES[crew_type]
    failure = profile["base_error_rate"] * profile["pressure_multiplier"] * chaos_pressure
    if prime_time:
        failure *= 1.2
    return min(100, int(failure * 1000))
