import random
from .reward import calculate_reward

class SafeRouteEnv:
    def __init__(self):
        self.routes = []
        self.time_of_day = "day"
        self._state = None
        self.reset()
        
    def reset(self):
        self.time_of_day = random.choice(["day", "night"])
        self.routes = []
        for i in range(3):
            # Base features
            crime_rate = random.uniform(0.0, 1.0)
            lighting_level = random.uniform(0.0, 1.0)
            crowd_density = random.uniform(0.0, 1.0)
            distance = random.uniform(1.0, 10.0)
            
            # Dynamic risk initialized based on baseline
            base_risk = random.uniform(0.0, 0.4)
            
            # Increase risk and alter features during night
            if self.time_of_day == "night":
                base_risk += random.uniform(0.2, 0.5)
                lighting_level *= random.uniform(0.2, 0.8) # Generally worse lighting at night
                
            dynamic_risk = min(base_risk, 1.0)
            
            self.routes.append({
                "id": f"route_{i+1}",
                "crime_rate": crime_rate,
                "lighting_level": lighting_level,
                "crowd_density": crowd_density,
                "distance": distance,
                "dynamic_risk": dynamic_risk
            })
            
        self._state = {
            "time_of_day": self.time_of_day,
            "routes": self.routes
        }
        return self.state()
        
    def step(self, action):
        """
        Takes an action (e.g., 'route_1') and returns (state, reward, done, info)
        """
        # Simulate sudden unsafe events randomly
        if random.random() < 0.2: # 20% chance of sudden event across the environment
            try:
                affected_route = random.choice(self.routes)
                affected_route['dynamic_risk'] = min(1.0, affected_route['dynamic_risk'] + random.uniform(0.3, 0.6))
                self._state['routes'] = self.routes
            except IndexError:
                pass
        
        # Identify the selected route
        route = next((r for r in self.routes if r['id'] == str(action)), None)
        
        if not route:
            # Invalid action
            return self.state(), 0.0, True, {"error": "Invalid action selected."}
            
        reward = calculate_reward(route, self.time_of_day)
        
        done = True # Routing selection is a single step episode
        info = {"selected_route_stats": route}
        
        return self.state(), reward, done, info
        
    def state(self):
        """Returns the current state."""
        return self._state