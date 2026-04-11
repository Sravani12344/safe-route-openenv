from .reward import calculate_reward

class EasyTask:
    def evaluate(self, state, action):
        target = min(state['routes'], key=lambda x: x['crime_rate'])
        return 1.0 if target['id'] == action else 0.0

class MediumTask:
    def evaluate(self, state, action):
        def score(r):
            return (1.0 - r['crime_rate']) * 0.5 + (r['lighting_level'] * 0.3) + ((1.0 - abs(r['crowd_density'] - 0.5)) * 0.2)
        target = max(state['routes'], key=score)
        return 1.0 if target['id'] == action else 0.0

class HardTask:
    def evaluate(self, state, action):
        target = max(state['routes'], key=lambda x: calculate_reward(x, state['time_of_day']))
        return 1.0 if target['id'] == action else 0.0
