def calculate_reward(route_stats, time_of_day):
    """
    Calculates safety reward explicitly matching mapping formula constraints:
    crime_rate (0.4), lighting (0.2), crowd (0.2), inverse_distance (0.2)
    """
    crime = route_stats.get('crime_rate', 0.5)
    light = route_stats.get('lighting_level', 0.5)
    crowd = route_stats.get('crowd_density', 0.5)
    dist = max(route_stats.get('distance', 1.0), 1.0)
    
    score = ((1.0 - crime) * 0.4) + (light * 0.2) + ((1.0 - abs(crowd - 0.5)) * 0.2) + ((1.0 / dist) * 0.2)
    
    return max(0.0, min(float(score), 1.0))
